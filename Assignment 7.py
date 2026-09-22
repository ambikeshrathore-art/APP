import re

def find_emails(text):
    pattern = r'\S+@\S+'
    emails = re.findall(pattern, text)
    return emails


# Main program
text = input("Enter the text: ")

emails = find_emails(text)

if emails:
    print("\nEmail addresses found:")
    for email in emails:
        print(email)
else:
    print("\nNo email addresses found.")
