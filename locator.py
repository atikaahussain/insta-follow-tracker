#Import Config
import config  

USERNAME = config.USERNAME

PROFILE_PAGE_LINK=(f"https://www.instagram.com/{USERNAME}/")

#navbar presence
NAVBAR_PRESENCE_MARKER = (".//*[@class='x6usi7g x18b5jzi x1lun4ml x1vjfegm']" )

#followers page link
FOLLOWER_LINK=("//a[contains(@href, '/followers/')]")

#following page link
FOLLOWING_LINK=("//a[contains(@href, '/following/')]")

#dialog box 
FOLLOW_DIALOG = ("//div[@class='x6nl9eh x1a5l9x9 x7vuprf x1mg3h75 x1lliihq x1iyjqo2 xs83m0k xz65tgg x1rife3k x1n2onr6']" )

# Usernames inside dialog
FOLLOWER_ELEMENTS = ("//div[@role='dialog']//a[contains(@href, '/') and not(img)]")

# Close button in dialog
CLOSE_BUTTON = (".//div[@role='dialog']//button" )
