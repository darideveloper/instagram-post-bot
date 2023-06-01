<div><a href='https://github.com/github.com/darideveloper/blob/master/LICENSE' target='_blank'>
            <img src='https://img.shields.io/github/license/github.com/darideveloper.svg?style=for-the-badge' alt='MIT License' height='30px'/>
        </a><a href='https://www.linkedin.com/in/francisco-dari-hernandez-6456b6181/' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=LinkedIn&color=0A66C2&logo=LinkedIn&logoColor=FFFFFF&label=' alt='Linkedin' height='30px'/>
            </a><a href='https://t.me/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Telegram&color=26A5E4&logo=Telegram&logoColor=FFFFFF&label=' alt='Telegram' height='30px'/>
            </a><a href='https://github.com/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=GitHub&color=181717&logo=GitHub&logoColor=FFFFFF&label=' alt='Github' height='30px'/>
            </a><a href='https://www.fiverr.com/darideveloper?up_rollout=true' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Fiverr&color=222222&logo=Fiverr&logoColor=1DBF73&label=' alt='Fiverr' height='30px'/>
            </a><a href='https://discord.com/users/992019836811083826' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Discord&color=5865F2&logo=Discord&logoColor=FFFFFF&label=' alt='Discord' height='30px'/>
            </a><a href='mailto:darideveloper@gmail.com?subject=Hello Dari Developer' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Gmail&color=EA4335&logo=Gmail&logoColor=FFFFFF&label=' alt='Gmail' height='30px'/>
            </a></div><div align='center'><br><br><img src='https://github.com/darideveloper/instagram-post-bot/blob/master/logo.png?raw=true' alt='Instagram Post Bot' height='80px'/>

# Instagram Post Bot

Bot for post on Instagram with data from Google Sheets

Start date: **2023-05-19**

Last update: **2023-05-23**

Project type: **client's project**

</div><br><details>
            <summary>Table of Contents</summary>
            <ol>
<li><a href='#buildwith'>Build With</a></li>
<li><a href='#media'>Media</a></li>
<li><a href='#details'>Details</a></li>
<li><a href='#install'>Install</a></li>
<li><a href='#settings'>Settings</a></li>
<li><a href='#run'>Run</a></li>
<li><a href='#roadmap'>Roadmap</a></li></ol>
        </details><br>

# Build with

<div align='center'><a href='https://www.python.org/' target='_blank'> <img src='https://cdn.svgporn.com/logos/python.svg' alt='Python' title='Python' height='50px'/> </a><a href='https://www.selenium.dev/' target='_blank'> <img src='https://cdn.svgporn.com/logos/selenium.svg' alt='Selenium' title='Selenium' height='50px'/> </a><a href='https://sheets.google.com/' target='_blank'> <img src='https://www.gstatic.com/images/branding/product/1x/sheets_2020q4_48dp.png' alt='Google Sheets' title='Google Sheets' height='50px'/> </a></div>

# Media

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
* Python >= 3.10

# Settings

## Setup google sheets

### Api Key

For use the project, you should setup an api key, in your google console acccount. 

1. You can follow  [This tutorial](https://github.com/darideveloper/tutorials/blob/master/generate%20google%20sheets%20api%20key/README.md)
2. When you finish the steps, you will have a json file. **Place the file in the project folder** and name it as **crdentials.py**

## Share google sheet

You should create a shwre link with edit permissions


1. For do it, follow the next [This tutorial](https://github.com/darideveloper/tutorials/blob/master/share%20google%20sheet%20with%20edit%20permissions/README.md)
2. Save the link for the next steps

## Enviroment variables

1. Copy [this template](https://docs.google.com/spreadsheets/d/1CDUQe4LM-_koQv9mx1RjHdKM8skL0a_K41y3gE5MjR8/edit?usp=sharing) to your google drive (you can rename it, but be sure to keep the same column names and the same sheet name)
2. In the root folder, create an a file ".env"
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
4. Click on button "Export" (the cookies will be copy to your clipboard)
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

If you want to tun the bot in loop, I suggest you to use tools to run the script all days at specific time, like [Task Scheduler](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page) for windows, [Cron](https://www.google.com/search?q=linux+cronjobs&oq=linux+cronjobs&aqs=chrome..69i57.3719j0j1&sourceid=chrome&ie=UTF-8) for Linux or [Jenkins](https://www.jenkins.io/) for both systems

In other hand, you can do it too with the file **run_loop.py**, who run the main script each hour (NOTE: if any errors happends, like internet issues, the bot will stop working until you restart it)

# Roadmap

* [x] Login with cookies
* [x] Post images
* [x] Get post from google sheets
* [x] Post with threading and wait to post time
* [x] Show post index
* [x] Filter today posts
* [x] Update google sheet after post
* [x] Run with main file


