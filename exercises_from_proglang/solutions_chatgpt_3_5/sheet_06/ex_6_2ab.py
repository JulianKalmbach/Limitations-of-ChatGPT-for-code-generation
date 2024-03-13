class MailAddress:
    def __init__(self, name, domain):
        self.name = name
        self.domain = domain

class Mail:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body

class MailAccount:
    def __init__(self, name, inbox, outbox):
        self.name = name
        self.inbox = inbox
        self.outbox = outbox

class MailServer:
    def __init__(self, domain, accounts):
        self.domain = domain
        self.accounts = accounts

def show_mail_address(address):
    return f"{address.name}@{address.domain}"

def show_mail(mail):
    return f"From: {show_mail_address(mail.sender)}\nTo: {show_mail_address(mail.receiver)}\nSubject: {mail.subject}\n{mail.body}"

def show_mail_account(account):
    inbox = ", ".join([show_mail(mail) for mail in account.inbox])
    outbox = ", ".join([show_mail(mail) for mail in account.outbox])
    return f"Mail Account: {account.name}\nInbox:\n{inbox}\nOutbox:\n{outbox}"

def show_mail_server(server):
    accounts_info = "\n".join([show_mail_account(account) for account in server.accounts])
    return f"Mail Server: {server.domain}\n{accounts_info}"