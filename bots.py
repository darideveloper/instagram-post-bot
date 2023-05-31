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
        
        self.google_sheets = None
                
        # Get posts to upload
        posts_data = self.__get_posts_data__ ()

        # Create botss
        for post_data in posts_data:
            Bot (post_data, self.google_sheets)
    
    def __get_posts_data__ (self) -> list:
        """ Get posts data from google sheets, and filter only post of the current hour

        Returns:
            list: post data to upload
        """
        
        # Show system data
        print (f'System date: {datetime.now ().strftime ("%d/%m/%Y")}')
        print (f'System time: {datetime.now ().strftime ("%H:%M:%S")}')
        print () 
        
        # Connect to google sheets
        try:
            self.google_sheets = GoogleSheets (SHEET_SHARED_LINK, os.path.join (CURRENT_FOLDER, "credentials.json"), "post")
            post_data = self.google_sheets.get_data ()
        except Exception as err:
            print ("Error connecting to google sheets. Check your credentials and shared link.")
            print (f"Details: {err}")
            quit ()
            
        print (f"Total post found in sheet: {len (post_data)}")
        
        # Add row to each post
        row_counter = 0
        for post in post_data:
            row_counter += 1
            post["row"] = row_counter
       
        # Filter posts by date
        posts_today = []
        for post in post_data:
            post_date = datetime.strptime (post["date"], "%d/%m/%Y").date ()
            today = datetime.now ().date ()
            if post_date == today:
                posts_today.append (post)
                
        print (f"Total post found for today today: {len (posts_today)}")
        
        # Filter posts by hour
        posts_hour = []
        for post in posts_today:
            post_hour = post["time"].split (":")[0]
            current_hour = datetime.now ().strftime ("%H")
            if post_hour == current_hour:
                posts_hour.append (post)
        
        print (f"Total post found for this hour: {len (posts_hour)}")
        print ()
        
        # Add index to each post
        index_counter = 0
        for post in posts_hour:
            index_counter += 1
            post["index"] = index_counter
        
        if posts_hour:
            
            print ("Post to upload:")
            
            # Show posts data
            for post in posts_hour:
                index = post["index"]
                time = post["time"]
                caption = post["caption"].replace('\n', ' ')[0:15]
                image = post["image"]
                print (f'\t{index}. {time} - {caption} - {image}')
            return posts_hour     
        else:            
            # Detect not post
            print ("There are not post to upload at this hour.")
            return []
        
    
if __name__ == "__main__":
    Bots ()