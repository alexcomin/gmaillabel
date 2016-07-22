import imaplib
from time import sleep

login = 'name@gmail.com'
password = 'you_pass'

label = 'CodeCademy'

gmail = imaplib.IMAP4_SSL('imap.gmail.com', '993')
gmail.login(login, password)


def write_file(name_file, arg):
    with open(name_file, 'w') as writes_file:
        writes_file.write(arg)


while True:
    unseen = gmail.status(label, '(UNSEEN)')
    parse = unseen[1][0].decode('utf-8')
    parse = parse.replace('(','').replace(')','').split(' ')[2]
    if (parse == '0'):
        write_file('text.txt', '')
    else:
        write_file('text.txt', parse)
    sleep(5.0)
