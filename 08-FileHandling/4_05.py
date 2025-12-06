import re

def email_sender():
    with open('email.txt') as f:
        text = f.read()
    return re.search(r'From:\s*(\S+@\S+)', text).group(1)

def email_recipient():
    with open('email.txt') as f:
        text = f.read()
    return re.search(r'To:\s*(\S+@\S+)', text).group(1)

def email_subject():
    with open('email.txt') as f:
        text = f.read()
    return re.search(r'Subject:\s*(.*)', text).group(1)

def email_body():
    with open('email.txt') as f:
        text = f.read()
    return re.search(r'\n\n(.*)', text, re.DOTALL).group(1)
