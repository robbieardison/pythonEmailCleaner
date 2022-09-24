import imaplib
import email
from email.header import decode_header

#account credentials
username = "youremail@provider.com"
password = "youremailpassword"

#create an IMAP class with SSL
imap = imaplib.IMAP4_SSL("imap.gmail.com")
#authenticate
imap.login(username, password)

# select the mailbox I want to delete in
# if you want SPAM, use imap.select("SPAM") instead
imap.select("FLOAT")

# search for specific mails by sender
status, messages = imap.search(None, 'FROM "notification@koinworks.com"')

#The comments below are examples of using other imap.search criterias. You should only use one search line per script.
# to get mails by subject
#status, messages = imap.search(None, 'SUBJECT "Thanks for Subscribing to our Newsletter !"')
# to get mails after a specific date
#status, messages = imap.search(None, 'SINCE "01-JAN-2020"')
# to get mails before a specific date
#status, messages = imap.search(None, 'BEFORE "01-JAN-2020"')
# to get all mails
#status, messages = imap.search(None, "ALL")

# convert messages to a list of email IDs
messages = messages[0].split(b' ') 

print("Deleting mails")
count = 1
for mail in messages:
    # mark the mail as deleted
    imap.store(mail, "+FLAGS", "\\Deleted")

    print(count, "mail(s) deleted")
    count +=1

print("All selected mails have been deleted")

# permanently remove mails that are marked as deleted
# from the selected mailbox (in this case, INBOX)
imap.expunge()
# close the mailbox
imap.close()
# logout from the account
imap.logout()

