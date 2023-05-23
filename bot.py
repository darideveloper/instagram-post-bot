import os
import json
from time import sleep
from scraping.web_scraping import WebScraping

# Constants and enviroment variables
CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

class Bot (WebScraping):
    
    def __init__ (self, posts_data:dict):
        """ Create bot and post image

        Args:
            posts_data (dict): data of the post to upload
        """
        
        # Variables
        self.pages = {
            "login": "https://www.instagram.com/accounts/login/",
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
        
        # Open browser and login
        super().__init__ ()
        self.__login__ ()
 
        # Post image
        post_image_path = os.path.join (self.posts_data["path"], self.posts_data["image"])
        self.__post__ (post_image_path, "test")
        
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
        print ("Login...")
        self.set_page (self.pages["login"])
        self.set_cookies (cookies)
            
    def __post__ (self, image_path:str, caption:str=""):
        """_summary_

        Args:
            image_path (str): image path to post
            caption (str, optional): text of the post. Defaults to "".
        """
        
        print (f"Posting image {os.path.basename(image_path)} with caption {caption}...")
        
        # Catch errors posting image
        try:
            
            # Load page
            self.set_page (self.pages["login"])
            
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
            self.click (self.selectors["btn_next"])
            sleep (5)
            
        except Exception as err:
            
            # Save error in log fgile
            print ("\tError posting image. check .log file.")
            self.__save_error__ (err)
             
                                         
        else:
            print ("\tDone.")