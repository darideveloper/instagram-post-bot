import os
from datetime import datetime
from dotenv import load_dotenv
from spreadsheets.google_sheets import GoogleSheets
from bot import Bot

load_dotenv ()

# Constants and enviroment variables
CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))
SHEET_SHARED_LINK = os.getenv ("SHEET_SHARED_LINK")

class Bots ():
    def __init__ (self):
        """ Create bots and post images
        """
                
        # Get posts to upload
        posts_data = self.__get_posts_data__ ()

        # Create botss
        for post_data in posts_data:
            Bot (post_data)
    
    def __get_posts_data__ (self) -> list:
        """ Get posts data from google sheets, and filter only post of the current hour

        Returns:
            list: post data to upload
        """
        
        # Connect to google sheets
        try:
            self.google_sheets = GoogleSheets (SHEET_SHARED_LINK, os.path.join (CURRENT_FOLDER, "credentials.json"), "post")
            post_data = self.google_sheets.get_data ()
        except Exception as err:
            print ("Error connecting to google sheets. Check .log file.")
            self.__save_error__ (err)
            quit ()
       
        # Filter posts
        post_filtered = []
        post_counter = 0
        now = datetime.now ()
        current_hour = now.strftime ("%H")
        today = now.replace (hour=0, minute=0, second=0, microsecond=0)
        for post in post_data:
            
            # Filter by hour
            post_hour = post["time"].split (":")[0]
            if post_hour != current_hour:
                continue
            
            # Filter by date
            post_date = datetime.strptime (post["date"], "%d/%m/%Y")
            if post_date != today:
                continue
            
            # Add index to post and save
            post_counter += 1 
            post["index"] = post_counter
            post_filtered.append (post)
                
        if post_filtered:
            print (f"Post found to upload at this hour: {len (post_filtered)}")
            for post in post_filtered:
                print (f'\t{post["index"]}. time: {post["time"]}, caption: "{post["caption"][0:15] + "..."}", image: "{post["image"]}"')
        else:            
            # Detect not post
            print ("There are not post to upload at this hour.")
            quit ()
        
        return post_filtered     
    
if __name__ == "__main__":
    Bots ()