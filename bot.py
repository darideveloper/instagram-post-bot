import os
import json
from time import sleep
from threading import Thread
from datetime import datetime
from scraping.web_scraping import WebScraping
from spreadsheets.google_sheets import GoogleSheets

# Constants and enviroment variables
CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

class Bot (WebScraping):
    
    def __init__ (self, posts_data:dict, google_sheets:GoogleSheets):
        """ Create bot and post image

        Args:
            posts_data (dict): data of the post to upload
            google_sheets (GoogleSheets): google sheets object to manage spreadsheet
        """
        
        # Variables
        self.pages = {
            "login": "https://www.instagram.com/accounts/login/",
            "home": "https://www.instagram.com/",
        }
        self.selectors = {
            "btn_create": '.xh8yej3.x1iyjqo2 div:nth-child(7) .x1n2onr6 a',
            "input_image": '[type="file"][multiple]',
            "btn_show_size": '._abfo div:first-child [type="button"]',
            "btn_original_size": '._ac36._ac38 [type="button"]:first-child',
            "btn_next": '._ac76 [role="button"]',
            "input_caption": '[role="textbox"]',
        }
        self.posts_data = posts_data
        self.index = posts_data["index"]
        self.row = posts_data["row"]
        self.google_sheets = google_sheets
        
        # Open browser and login
        super().__init__ ()
        self.__login__ ()
 
        # Post image with threading
        post_image_path = os.path.join (self.posts_data["path"], self.posts_data["image"])
        thread_obj = Thread (
            target=self.__post_image__, 
            args=(
                post_image_path, 
                self.posts_data["caption"], 
                self.posts_data["time"]
                )
            )
        thread_obj.start ()
        
    def __save_error__ (self, error:str):
        """ Save errror in log file

        Args:
            error (str): error details
        """
        with open (os.path.join (CURRENT_FOLDER, ".log"), "w") as file:
            file.write (str (error))         
                
    def __login__ (self):
        """ Load cookies to instagram to avoid login
        """
        
        with open (os.path.join (CURRENT_FOLDER, "cookies.json")) as file:
            cookies = json.load (file)
        
        # Start browser
        print (f"{self.index}. Login...")
        self.set_page (self.pages["login"])
        self.set_cookies (cookies)
    
    def __update_status__ (self):
        """ Update status of current post in google sheets 
        """
        
        try:
            self.google_sheets.write_cell ("TRUE", self.row + 1, 6)
        except Exception as err:
            
            # Save error in log fgile
            print (f"{self.index}. Error updating status in google sheet. check .log file.")
            self.__save_error__ (err)
            
    
    def __post_image__ (self, image_path:str, caption:str, time:str):
        """_summary_

        Args:
            image_path (str): image path to post
            caption (str): text of the post. 
            time (str): time to post in format HH:MM
        """
        
        # Convert time string to datetime
        post_time = datetime.strptime (time, "%H:%M")
        now = datetime.now ()
        post_time = post_time.replace (year=now.year, month=now.month, day=now.day, second=0, microsecond=0)
        
        # Skip if post time is lost
        if now > post_time:
            print (f"{self.index}. Post time {time} lost. Skipping...")
            return
        
        # Wait until post time comes
        print (f"{self.index}. Waiting until {self.posts_data['time']}...")
        while now < post_time:
            now = datetime.now ()
            sleep (5) # wait time to check again
        
        # Show status
        print (f'{self.index}. Posting...')
        
        # Catch errors posting image
        try:
            
            # Load page
            self.set_page (self.pages["home"])
            
            # Open post modal
            self.click (self.selectors["btn_create"])
            self.refresh_selenium ()
            
            # Upload image
            self.send_data (self.selectors["input_image"], image_path)
            self.refresh_selenium ()
            
            # Set size
            self.click (self.selectors["btn_show_size"])
            self.refresh_selenium ()
            self.click (self.selectors["btn_original_size"])
            self.click (self.selectors["btn_next"])
            self.refresh_selenium ()
            
            # Skip fiters
            self.click (self.selectors["btn_next"])
            self.refresh_selenium ()
            
            # Write caption
            self.send_data (self.selectors["input_caption"], caption)
            # self.click (self.selectors["btn_next"])
            sleep (5)
            
        except Exception as err:
            
            # Save error in log fgile
            print (f"{self.index}. Error posting image. check .log file.")
            self.__save_error__ (err)
             
                                         
        else:
            print (f"{self.index}. Done.")
            
            # Update ststus in google sheets
            self.__update_status__ ()