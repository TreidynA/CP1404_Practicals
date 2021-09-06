from typing import Dict, Any


def get_name_from_email(email):
    name = email.split("@")
    name = name[0]
    if "." in name:
        name = name.split(".")
        name = " ".join(name)

    return str(name).title()



EMAILS_AND_NAMES = {}
stop = False
while not stop:
    email = input("Email: ")
    if email == "":
        stop = True
    else:
        yes_or_no = input(f"Is your name {get_name_from_email(email)}? (Y/n) ").lower()
        if yes_or_no == "" or yes_or_no == 'y' or yes_or_no == "yes":
            EMAILS_AND_NAMES[email] = get_name_from_email(email)
        elif yes_or_no == "n" or yes_or_no == "no":
            name = input("Name: ")
            EMAILS_AND_NAMES[email] = name

for emails in EMAILS_AND_NAMES.items():
    print(f"{emails[1]} ({emails[0]})")




