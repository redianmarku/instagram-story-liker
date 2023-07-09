# Instagram Story Liker

This script allows you to automatically like the stories of Instagram users using Selenium and ChromeDriver.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python (version 3.6 or later)
- Selenium (`pip install selenium`)
- ChromeDriver

## Setup

1. Clone or download this repository to your local machine.

2. In the same directory as the script, create a file named `followers.txt`. This file should contain the usernames of the Instagram users whose stories you want to like, with each username on a new line.

3. Install Requirements with this command: `pip install -r requirements.txt`

## Usage

1. Open a terminal or command prompt and navigate to the directory where the script is located.

2. Run the script using the following command: `python run.py`

3. The script will prompt you to enter your Instagram username and password. Enter the required information and press Enter.

4. The script will start liking the stories of each user in the `followers.txt` file. It will open a Chrome window and automatically navigate to each user's story. If the user has a story, the script will click the "Like" button. If the user doesn't have a story, the script will move on to the next user.

5. The script will remove each username from the `followers.txt` file after liking their story.

6. Once the script finishes running, you can check the terminal or command prompt for output messages indicating the status of each action (liking a story or failing to like a story).

7. Customize the script as needed. You can uncomment the `chrome_options.add_argument("--headless")` line to run Chrome in headless mode (without opening a visible browser window). Make sure to comment out the line again if you want to see the browser window.

## Disclaimer

Please use this script responsibly and respect Instagram's terms of service. Automating interactions on Instagram may violate the platform's usage policies, so use this script at your own risk.
