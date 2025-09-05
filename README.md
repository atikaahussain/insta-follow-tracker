# INSTA FOLLOW CHECKER

A simple Python automation tool that uses Selenium to log into Instagram, scrape your followers and followings, and tell you who is not following you back.
Results are saved into text files for easy reference.

## Features

- Logs into Instagram automatically
- Collects all followers and followings
- Saves results into separate .txt files
- Shows who is not following you back


## Requirements

- Python 3.x
- Google Chrome browser
- Python Package
 ```bash
pip install selenium
```

## Setup

- Clone this repo or download the files
  
## How to Run (Step by Step)

-Open a terminal inside the project folder.
-Run the script:
 ```bash
 python main.py
 ```

-Script will:

  - Open Instagram in Chrome
  - Log in with your credentials
  - Go to your profile page
  - Collect all followers and followings
  - Save results into the username_files/ folder

## Oputput Files

-After running, you’ll find these files in username_files/:
  - followers.txt → list of your followers
  - followings.txt → list of your followings
  - not_following_back.txt → people you follow who don’t follow you back

## Note
- Instagram changes its UI often → if the script breaks, update the XPaths in locator.py.
- Don’t run too frequently to avoid Instagram login restrictions.
