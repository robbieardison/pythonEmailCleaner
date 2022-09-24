import imaplib
import email
from email.header import decode_header

#account credentials
username = "your@emailaddress.com"
password = "yomamasofat"

#create an IMAP class with SSL
imap = imaplib.IMAP4_SSL(imaplib.gmail.com)
#authenticate
imap.login(username, password)

