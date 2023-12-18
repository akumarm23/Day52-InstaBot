# Instagram Follower Bot using Python, Selenium v0.1

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Version](https://img.shields.io/badge/Version-0.1-green.svg)](https://github.com/akumarm23/Day52-InstaBot/releases/tag/v0.1)

An Instagram bot built in Python for automating the process of logging in, finding followers of a specified account, and following them.

## Dependencies

- [Selenium](https://selenium-python.readthedocs.io/)
- [WebDriver for Chrome](https://sites.google.com/chromium.org/driver/)

## Configuration

1. Update the constants in the script:
   - `TARGET_ACCOUNT`: Set this to the username of the Instagram account whose followers you want to follow.
   - `YOUR_USERNAME`: Your Instagram username.
   - `YOUR_PASSWORD`: Your Instagram password.

## Usage

1. Install dependencies:

   ```bash
   pip install selenium
   ```

2. Download the [ChromeDriver](https://sites.google.com/chromium.org/driver/) and place it in your project directory.

3. Run the script:

   ```bash
   python main.py
   ```

## Bot Actions

### 1. Log In

The bot will open the Instagram login page, fill in your username and password, and log in.

### 2. Find Followers

The bot will navigate to the followers page of the specified Instagram account and scroll through the list to load more followers.

### 3. Follow Users

The bot will attempt to follow users listed on the followers page. If a user is already being followed, it will handle the dialog (e.g., Unfollow/Cancel).

## Important Notes

- **Avoid Excessive Usage:** Be cautious not to run the script too frequently to prevent bot-like behavior and potential account issues.

- **Customization:** Check and update the script as needed, especially if Instagram's HTML structure changes over time.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
