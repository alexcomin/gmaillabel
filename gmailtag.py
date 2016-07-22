import imaplib
from time import sleep

login = 'name@gmail.com'
password = 'you_pas'

labels = ['you_label', 'you_label', 'you_label']

gmail = imaplib.IMAP4_SSL('imap.gmail.com', '993')
gmail.login(login, password)


def write_file(name_file, arg):
    with open(name_file, 'w') as writes_file:
        writes_file.write(arg)


while True:
    count = 0
    for label in labels:
        unseen = gmail.status(label, '(UNSEEN)')
        parse = unseen[1][0].decode('utf-8')
        parse = int(parse.replace('(','').replace(')','').split(' ')[2])
        count += parse
    if (count == 0):
        write_file('text.txt', '')
    else:
        write_file('text.txt', str(count))
    sleep(5.0)
