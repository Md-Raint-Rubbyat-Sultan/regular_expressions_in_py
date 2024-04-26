import re

def main():
    url = input("What's the twitter url> ").strip()
    print(get_user_name_from_url(url))

def get_user_name_from_url(url):
    user_name = re.search(r"^(?:https?://)?(?:www.)?twitter\.com/([a-z_]+)", url)
    return user_name.group(1)

if __name__ == "__main__":
    main()