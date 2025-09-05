import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import locators
import locator

#Import Config
import config  

USERNAME = config.USERNAME
PASSWORD = config.PASSWORD

# --- Setup driver ---
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

def get_follow_list(driver, list_type="followers"):

    username_dict = {"usernames": []}

    if list_type == "followers":
        link =wait.until(EC.element_to_be_clickable((By.XPATH, locator.FOLLOWER_LINK)))
    else:
        link =wait.until(EC.element_to_be_clickable((By.XPATH, locator.FOLLOWING_LINK)))
    link.click()
    time.sleep(5)

    #Scroll through the followings list
    dialog = driver.find_element(By.XPATH, locator.FOLLOW_DIALOG)
    last_height = driver.execute_script("return arguments[0].scrollHeight", dialog)

    while True:
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
        time.sleep(5)
        new_height = driver.execute_script("return arguments[0].scrollHeight", dialog)
        if new_height == last_height:  # reached the end
            break
        last_height = new_height

    time.sleep(2)
    #Collect usernames
    follower_elements = driver.find_elements(By.XPATH,locator.FOLLOWER_ELEMENTS)
    for elem in follower_elements:
        username_text = elem.text.strip()

        username_dict["usernames"].append(username_text)

    return username_dict


try:
    # opening instagram web
    driver.get("https://www.instagram.com")

    #wait wait wait
    wait = WebDriverWait(driver, 15)

    #Log in
    username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_input = driver.find_element(By.NAME, "password")
    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)

    #Wait for successful login
    wait.until(EC.presence_of_element_located((By.XPATH, locator.NAVBAR_PRESENCE_MARKER)))
    print("login successful")

    #going to profile page
    driver.get(locator.PROFILE_PAGE_LINK)
    print("Profile page opened")

    # --- Call the function ---
    #1st function call for the followers
    followers = get_follow_list(driver, "followers")

    #closing the followers dialog box after collecting the followers
    close_btn = driver.find_element(By.XPATH,locator.CLOSE_BUTTON)
    close_btn.click()
    time.sleep(2)

    # 2nd function call for the followings
    followings = get_follow_list(driver, "following")

    #collecting the number of followers and followings
    no_of_followers= len(followers["usernames"])
    no_of_followings= len(followings["usernames"])


    #doing some math (eh)
    followers_set = set(followers["usernames"])
    followings_set = set(followings["usernames"])

    not_following_back = followings_set - followers_set
    no_of_not_following_back= len(not_following_back)

    #printing number of followers and follwoings
    print("Followers:",no_of_followers)
    print("Followings:",no_of_followings)
    print("Not Following you back:",no_of_not_following_back)
    

    ####### saving usernames in their specified files ######

    # Followers file
    with open("username_files/followers.txt", "w", encoding="utf-8") as f:
        f.write(f"Total followers: {no_of_followers}\n\n")
        for idx, user in enumerate(sorted(followers["usernames"]), start=1):
            f.write(f"{idx}. {user}\n")

    # Followings file
    with open("username_files/followings.txt", "w", encoding="utf-8") as f:
        f.write(f"Total followings: {no_of_followings}\n\n")
        for idx, user in enumerate(sorted(followings["usernames"]), start=1):
            f.write(f"{idx}. {user}\n")

    # Not following back file
    with open("username_files/not_following_back.txt", "w", encoding="utf-8") as f:
        f.write(f"Not following you back: {len(not_following_back)}\n\n")
        for idx, user in enumerate(sorted(not_following_back), start=1):
            f.write(f"{idx}. {user}\n")


    print("Data fetching done!")

finally:
    driver.quit()
