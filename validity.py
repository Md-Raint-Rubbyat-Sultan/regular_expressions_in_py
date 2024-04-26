import re

def main():
    email = input("What's email> ").strip()
    verify = email_validate(email)

    print(is_valid(verify))

def email_validate(email):
    return re.search(r"^(?:(?![A-Z])\w)+@([a-z]+\.)?[a-z]+\.[a-z]{2,3}$", email)

def is_valid(i):
    return "valid" if i else "invalid"

if __name__ == "__main__":
    main()