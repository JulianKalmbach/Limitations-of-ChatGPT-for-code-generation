from dataclasses import dataclass
from typing      import Optional

## Data Types ##################################################################

@dataclass
class MailAddress:
    name:   str
    domain: str

@dataclass
class Mail:
    sender:   MailAddress
    receiver: MailAddress
    subject:  str
    body:     str

@dataclass
class MailAccount:
    name:     str
    inbox:    list[Mail]
    outbox:   list[Mail]

@dataclass
class MailServer:
    domain:   str
    accounts: list[MailAccount]

## Pretty Printing #############################################################

# Insert `n` spaces at the beginning of each line in `s`.
def indent(n: int, s: str) -> str:
    new_lines = []
    for line in s.split('\n'):
        new_lines += [' ' * n + line]
    return '\n'.join(new_lines)

def show_mail_address(ma: MailAddress) -> str:
    return ma.name + '@' + ma.domain

def show_mail(m: Mail) -> str:
    return '\n'.join([ 'From: ' + show_mail_address(m.sender)
                     , 'To: ' + show_mail_address(m.receiver)
                     , 'Subject: ' + m.subject
                     , ''
                     , m.body
                     ])

def show_mail_account(ma: MailAccount) -> str:
    inbox_str = ''
    for m in ma.inbox:
        inbox_str += '\n' + show_mail(m)
    outbox_str = ''
    for m in ma.outbox:
        outbox_str += '\n' + show_mail(m)
    return '\n'.join([ 'Name: ' + ma.name,
                       'Inbox:' + indent(4, inbox_str),
                       'Outbox:' + indent(4, outbox_str)
                     ])

def show_mail_server(ms: MailServer) -> str:
    accounts_str = ''
    for a in ms.accounts:
        accounts_str +='\n' + show_mail_account(a)
    return '\n'.join([ 'Server: ' + ms.domain,
                         'Accounts:' + indent(4, accounts_str)
                       ])

## Mail Delivery ###############################################################

def find_server(domain: str, servers: list[MailServer]) -> Optional[MailServer]:
    for server in servers:
        if server.domain == domain:
            return server
    return None

def find_account(name: str, server: MailServer) -> Optional[MailAccount]:
    for acc in server.accounts:
        if acc.name == name:
            return acc
    return None

def deliver_mail(mail: Mail, servers: list[MailServer]) -> bool:
    server = find_server(mail.receiver.domain, servers)
    if server == None:
        return False
    acc = find_account(mail.receiver.name, server)
    if acc == None:
        return False
    acc.inbox += [mail]
    return True

def deliver_all_mail(servers: list[MailServer]):
    for server in servers:
        for acc in server.accounts:
            undeliverable = []
            for mail in acc.outbox:
                # Emails with fake senders get deleted.
                if mail.sender == MailAddress(acc.name, server.domain):
                    if not deliver_mail(mail, servers):
                        undeliverable = undeliverable + [mail]
            acc.outbox = undeliverable

## Example #####################################################################

if __name__ == '__main__':

    my_mail = Mail(
        MailAddress('me', 'mymail.com'),
        MailAddress('you', 'yourmail.com'),
        'Super important stuff!',
        '\n'.join(["Actually... it's not that important.",
                   '',
                   'Sincerely,',
                   'Me'
                  ])
    )

    servers = [
        MailServer('mymail.com', [
            MailAccount('me', [], [my_mail])
        ]),
        MailServer('yourmail.com', [
            MailAccount('you', [], [])
        ]),
    ]

    print('–– Before delivery ––––––––––––––––––––––––––––––––––')
    for server in servers:
        print(show_mail_server(server) + "\n")

    deliver_all_mail(servers)

    print('–– After delivery ––––––––––––––––––––––––––––––––––')
    for server in servers:
        print(show_mail_server(server) + "\n")
