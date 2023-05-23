import os
import json
from scraping.web_scraping import WebScraping

CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

class Bot (WebScraping):
    
    def __init__ (self):
        
        # Variables
        pages = {
            "login": "https://www.instagram.com/accounts/login/",
        }
        
        # Start browser
        print ("login...")
        cookies = self.__get_cookies__ ()
        super().__init__ ()
        self.set_page (pages["login"])
        self.set_cookies (cookies)
        
        input ("end?")
        
    def __get_cookies__ (self):
        with open (os.path.join (CURRENT_FOLDER, "cookies.json")) as file:
            cookies = json.load (file)
        return cookies
    
if __name__ == "__main__":
    bot = Bot ()