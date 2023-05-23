import os
import json
from scraping.web_scraping import WebScraping

CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

class Bot (WebScraping):
    
    def __init__ (self):
        
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
        
        # Open browser and login
        super().__init__ ()
        self.__login__ ()
 
        # Post image
        self.__post__ (r"C:\Users\daria\Downloads\imgjhashgdsa3.jpeg", "test")
                
    def __login__ (self):
        
        with open (os.path.join (CURRENT_FOLDER, "cookies.json")) as file:
            cookies = json.load (file)
        
        # Start browser
        print ("login...")
        self.set_page (self.pages["login"])
        self.set_cookies (cookies)
            
    def __post__ (self, image_path:str, caption:str=""):
        """_summary_

        Args:
            image_path (str): image path to post
            caption (str, optional): text of the post. Defaults to "".
        """
        
        print (f"posting image {os.path.basename(image_path)} with caption {caption}...")
        
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
            
        except Exception as err:
            
            # Save error in log fgile
            print ("\terror posting image. check .log file.")
            with open (os.path.join (CURRENT_FOLDER, ".log"), "w") as file:
                file.write (str (err))       
                                         
        else:
            print ("\tdone.")
        
        
    
if __name__ == "__main__":
    bot = Bot ()