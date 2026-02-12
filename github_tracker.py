import requests
import getpass

def get_github_users_list(username, list_type, token):
    """Get Follow List with pagination."""
    users = set()
    page = 1
    while True:
        url = f"https://api.github.com/users/{username}/{list_type}?page={page}"
        headers = {"Authorization": f"token {token}"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            if not data:
                break
            users.update(user['login'] for user in data)
            page += 1
        elif response.status_code == 401:
            raise Exception("Error: 401 - Bad credentials. Please check your token.")
        elif response.status_code == 403:
            raise Exception("Error: 403 - Forbidden. You may have hit the rate limit.")
        elif response.status_code == 404:
            raise Exception(f"Error: 404 - User '{username}' not found.")
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")
    return users

def unfollow_user(username, user_to_unfollow, token):
    """Unfollow a user."""
    url = f"https://api.github.com/user/following/{user_to_unfollow}"
    headers = {"Authorization": f"token {token}"}
    response = requests.delete(url, headers=headers)
    
    if response.status_code == 204:
        print(f"✓ Successfully unfollowed {user_to_unfollow}")
        return True
    elif response.status_code == 401:
        raise Exception("Error: 401 - Bad credentials. Please check your token.")
    elif response.status_code == 403:
        raise Exception("Error: 403 - Forbidden. You may have hit the rate limit.")
    else:
        print(f"✗ Failed to unfollow {user_to_unfollow}: {response.status_code}")
        return False

def find_unfollowers(username, token):
    try:
        followers = get_github_users_list(username, 'followers', token)
        following = get_github_users_list(username, 'following', token)
        
        unfollowers = following - followers
        
        if unfollowers:
            print(f"\n[찾은 언팔자] {username}를 언팔한 사람 {len(unfollowers)}명:")
            for unfollower in sorted(unfollowers):
                print(f"- {unfollower}")
            
            # 언팔 옵션
            while True:
                choice = input("\n자동으로 언팔하시겠습니까? (y/n): ").lower().strip()
                if choice in ['y', 'yes']:
                    print("\n언팔 시작...")
                    unfollowed_count = 0
                    for unfollower in sorted(unfollowers):
                        if unfollow_user(username, unfollower, token):
                            unfollowed_count += 1
                    print(f"\n완료: {unfollowed_count}명 언팔")
                    break
                elif choice in ['n', 'no']:
                    print("언팔을 취소했습니다.")
                    break
                else:
                    print("y 또는 n을 입력하세요.")
        else:
            print(f"\n모든 팔로워가 {username}를 팔로우하고 있습니다.")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    username = input("Enter the GitHub Username: ")
    try:
        token = getpass.getpass("Enter your GitHub Personal Access Token (for private repos): ")
    except Exception as error:
        print('ERROR', error)
        # Fallback for environments where getpass is not available
        token = input("Enter your GitHub Personal Access Token (for private repos): ")

    find_unfollowers(username, token)
