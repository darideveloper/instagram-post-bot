# Instagram Post Bot

Bot for post on Instagram with data from Google Sheets

Start date: **2023-05-19**

Last update: **2023-05-23**

Project type: **client&#x27;s project**

![Logo](https://github.com/darideveloper/instagram-post-bot/blob/master/logo.png?raw=true)

## Media

![google sheets](https://github.com/darideveloper/instagram-post-bot/blob/master/screenshots/google-sheets.png?raw=true)

![running 1](https://github.com/darideveloper/instagram-post-bot/blob/master/screenshots/running-1.png?raw=true)

![running 2](https://github.com/darideveloper/instagram-post-bot/blob/master/screenshots/running-2.png?raw=true)

![running 3](https://github.com/darideveloper/instagram-post-bot/blob/master/screenshots/running-3.png?raw=true)

# Details

This project can post images (in original sizes) on Instagram, at specific date and time, and with custom caption.

Each time you run the bot, it get the post of today, at the current hour, wait the required time and post the images.

# Install

## Third party modules

Install all modules from pip: 

``` bash
$ pip install -r requirements.txt
```

## Programs

To run the project, the following software must be installed:: 

* [Google Chrome](https://www.google.com/intl/es/chrome) last version
* Python &gt;= 3.10

# Settings

## Setup google sheets

### Api Key

For use the project, you should setup an api key, in your google console acccount. 

1. You can follow  [This tutorial](https://github.com/darideveloper/tutorials/blob/master/generate google sheets api key/README.md)
2. When you finish the steps, you will have a json file. **Place the file in the project folder** and name it as **crdentials.py**

## Share google sheet

You should create a shwre link with edit permissions


1. For do it, follow the next [This tutorial](https://github.com/darideveloper/tutorials/blob/master/share google sheet with edit permissions/README.md)
2. Save the link for the next steps

## Enviroment variables

1. Copy [this template](https://docs.google.com/spreadsheets/d/1CDUQe4LM-_koQv9mx1RjHdKM8skL0a_K41y3gE5MjR8/edit?usp=sharing) to your google drive (you can rename it, but be sure to keep the same column names and the same sheet name)
2. In the root folder, create an a file &quot;.env&quot;
3. Save the shared link:
```shell
SHEET_SHARED_LINK ={your-google-sheet-with-edit-permissions}
```

## Cookies

You should login with your instagram account, and get your cookies (in order to avoid login)

1. Install the extension [EditThisCookie](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg?hl=es)
2. Open a Incognito window 
2. Go to your Instagram account (with user and password)
3. Click on the EditThisCookie icon
4. Click on button &quot;Export&quot; (the cookies will be copy to your clipboard)
5. Create a file **cookies.json** in the project folder
6. Paste the cookies
7. Save the file

# Run

Run the project folder with python: 
```sh
python .
```

Or run the main file:
```sh
python __main__.py
```

## Run in loop

If you want to tun the bot in loop, you can use tools to run the script all days at specific time, like [Task Scheduler](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page) for windows, [Cron](https://www.google.com/search?q=linux+cronjobs&amp;oq=linux+cronjobs&amp;aqs=chrome..69i57.3719j0j1&amp;sourceid=chrome&amp;ie=UTF-8) for Linux or [Jenkins](https://www.jenkins.io/) for both systems

# Roadmap

* [x] Login with cookies
* [x] Post images
* [x] Get post from google sheets
* [x] Post with threading and wait to post time
* [x] Show post index
* [x] Filter today posts
* [x] Update google sheet after post
* [x] Run with main file

