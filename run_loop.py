from time import sleep
from datetime import datetime

from bots import Bots

while True:
    
    Bots ()
    
    # Calculate minutes left to the next houw
    now = datetime.now ()
    minutes_left = 60 - now.minute
    
    # Sleep until the next hour
    print (f"Waiting {minutes_left} minutes, to the next run...\n")
    sleep (minutes_left * 60)