from dataclasses import dataclass, field
from typing import List

@dataclass
class MailAddress:
    name: str
    domain: str

@dataclass
class Mail:
    sender: MailAddress
    receiver: MailAddress
    subject: str
    body: str

@dataclass
class MailAccount:
    name: str
    inbox: List[Mail] = field(default_factory=list)
    outbox: List[Mail] = field(default_factory=list)

@dataclass
class MailServer:
    domain: str
    accounts: List[MailAccount] = field(default_factory=list)

def show_mail_address(mail_address: MailAddress) -> str:
    return f"{mail_address.name}@{mail_address.domain}"

def show_mail(mail: Mail) -> str:
    return (f"From: {show_mail_address(mail.sender)}\n"
            f"To: {show_mail_address(mail.receiver)}\n"
            f"Subject: {mail.subject}\n"
            f"{mail.body}")

def show_mail_account(mail_account: MailAccount) -> str:
    inbox_str = '\n'.join([show_mail(mail) for mail in mail_account.inbox])
    outbox_str = '\n'.join([show_mail(mail) for mail in mail_account.outbox])
    return (f"Account Name: {mail_account.name}\n"
            f"Inbox:\n{inbox_str}\n"
            f"Outbox:\n{outbox_str}")

def show_mail_server(mail_server: MailServer) -> str:
    accounts_str = '\n'.join([show_mail_account(account) for account in mail_server.accounts])
    return f"Mail Server: {mail_server.domain}\nAccounts:\n{accounts_str}"