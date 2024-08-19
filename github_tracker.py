import requests

def get_github_users_list(username, list_type, token):
    """Get Follow List."""
    url = f"https://api.github.com/users/{username}/{list_type}"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return {user['login'] for user in response.json()}
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")

def find_unfollowers(username, token):
    followers = get_github_users_list(username, 'followers', token)
    following = get_github_users_list(username, 'following', token)
    unfollowers = following - followers
    if unfollowers:
        print(f"{username} has been unfollowed by: {', '.join(unfollowers)}")
    else:
        print(f"{username} has not been unfollowed by anyone.")

if __name__ == "__main__":
    # input your ID and Token
    username = input("GitHub Username: ")
    token = input("GitHub Token: ")
    find_unfollowers(username, token)
