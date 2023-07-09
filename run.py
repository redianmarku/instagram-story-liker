import time
import os
import fileinput
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException


def save_credentials(username, password):
    with open("credentials.txt", "w") as file:
        file.write(f"{username}\n{password}")


def load_credentials():
    if not os.path.exists("credentials.txt"):
        return None

    with open("credentials.txt", "r") as file:
        lines = file.readlines()
        if len(lines) >= 2:
            return lines[0].strip(), lines[1].strip()

    return None


def prompt_credentials():
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")
    save_credentials(username, password)
    return username, password


def read_usernames_from_file(file_path):
    with open(file_path, "r") as file:
        usernames = [line.strip() for line in file]
    return usernames

def remove_username_from_file(username, file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if line.strip() != username:
                file.write(line)


def like_stories(username, password, usernames):
    # Set up ChromeDriver options
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Set up ChromeDriver service
    service = Service(ChromeDriverManager().install())

    # Set up ChromeDriver instance
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Log in to Instagram
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)

    username_input = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
    password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")

    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)

    # Like stories of each follower
    for follower in usernames:
        story_url = f"https://www.instagram.com/stories/{follower}"
        driver.get(story_url)
        time.sleep(2)

        # Check if the "View Story" button exists
        view_story_button = driver.find_elements(By.XPATH, "//div/div/div[2]/div/div/div/div[1]/div[1]/section/div[1]/div/section/div/div[1]/div/div/div/div/div[3]/div")
        if view_story_button:
            print("[TRUE] User -> " + follower + " has story up.")
            view_story_button[0].click()                
            time.sleep(4)
            
            try:
                like_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/section/div[1]/div/section/div/div[3]/div/div/div[2]/span/div")
                # Click on the like button or perform desired action
                like_button.click()
                print("Liked the story successfuly!")
                time.sleep(2)
            except NoSuchElementException:
                try:
                    like_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/section/div[1]/div/section/div/div[3]/div/div/div[1]/span/div")
                    # Click on the like button or perform desired action
                    like_button.click()
                    print("Liked the story successfuly!")
                    time.sleep(2)
                except NoSuchElementException:
                    # Both XPaths failed, skip to the next action or user
                    print("Failed to like the story.")
                    continue  # Assuming this is inside a loop

            # like_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/section/div[1]/div/section/div/div[3]/div/div/div[2]/span/div")
            # like_button.click()
            # time.sleep(2)
        else:
            print("[FALSE] User -> " + follower + " has no story up.")
            continue


    remove_username_from_file(follower, followers_file)

    # Close the ChromeDriver instance
    driver.quit()


if __name__ == "__main__":
    credentials = load_credentials()

    if credentials is None:
        username, password = prompt_credentials()
    else:
        username, password = credentials

    followers_file = "followers.txt"
    usernames = read_usernames_from_file(followers_file)

    like_stories(username, password, usernames)
