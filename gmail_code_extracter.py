import imaplib
import email
import re

host = 'imap.gmail.com'
username = 'danchuk204@gmail.com'
password = 'Fdan917635'


def get_inbox():
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")
    _, search_data = mail.search(None, 'UNSEEN')
    my_message = []
    for num in search_data[0].split():
        email_data = {}
        _, data = mail.fetch(num, '(RFC822)')
        _, b = data[0]
        email_message = email.message_from_bytes(b)
        for header in ['subject', 'to', 'from', 'date']:
            print("{}: {}".format(header, email_message[header]))
            email_data[header] = email_message[header]
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                email_data['body'] = body.decode()
            elif part.get_content_type() == "text/html":
                html_body = part.get_payload(decode=True)
                email_data['html_body'] = html_body.decode()
        my_message.append(email_data)
    return my_message
    




my_inbox = get_inbox()
#my_inbox = my_inbox[0]
#my_inbox = str(my_inbox)
#print(my_inbox)

#pattern = re.compile(">\d\d\d\d\d\d<")

#matchs= pattern.finditer(my_inbox)

#for match in matchs:
    #match = str(match)
    #match = match[45:51]
    #print(match)
   



