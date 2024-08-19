# github_unfollow_tracker

This repository contains a script to manage and track your GitHub followers. The tool helps you follow and unfollow users easily using GitHub's API.

## Features
- Follow and Unfollow Users: Seamlessly manage your GitHub followers with ease.
- Track User Profiles: Access and manage user data with selected permissions.

## Requirements
Python 3.x: Ensure you have Python 3.x installed.
Requests Library: Install the required Python library using the following command:
```bash
pip3 install requests
```
## Setup Guide
1. Generate a Personal Access Token
To interact with the GitHub API, you need a personal access token. Follow these steps:

- Go to your GitHub Personal Access Tokens page.
- Under "Note," provide a meaningful description of the token's purpose.
- Set an expiration for the token. (In the example, it's set to 7 days)

2. Assign the Required Scopes
To use the follow/unfollow feature, make sure you select the appropriate scopes:

- user
   : Follow and unfollow users.
- user.email (Optional): Access user email addresses (read-only).
![image](https://github.com/user-attachments/assets/3a3a4ce7-26cb-4064-8904-2c474fae12f3)

![image](https://github.com/user-attachments/assets/1e3d895c-6944-4228-967c-f18a767cde45)

3. Run the Script


