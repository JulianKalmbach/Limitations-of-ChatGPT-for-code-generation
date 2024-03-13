from typing import Optional, List
from exercises_from_proglang.solutions_chatgpt_4_0.sheet_06.ex_6_2ab import MailServer, MailAccount, Mail  # this was added manually, not by chatgpt, to fit the data structure


def find_server(domain: str, servers: List[MailServer]) -> Optional[MailServer]:
    for server in servers:
        if server.domain == domain:
            return server
    return None

def find_account(account_name: str, server: MailServer) -> Optional[MailAccount]:
    for account in server.accounts:
        if account.name == account_name:
            return account
    return None

def deliver_mail(mail: Mail, servers: List[MailServer]) -> bool:
    receiver_domain = mail.receiver.domain
    receiver_name = mail.receiver.name

    # Finde den Server des Empfängers
    server = find_server(receiver_domain, servers)
    if server is None:
        return False  # Kein Server für die Domain des Empfängers gefunden

    # Finde den Account des Empfängers auf dem Server
    account = find_account(receiver_name, server)
    if account is None:
        return False  # Kein Account für den Empfänger auf dem Server gefunden

    # Füge die Mail zum Posteingang des Empfängers hinzu
    account.inbox.append(mail)
    return True

def deliver_mail(mail: Mail, servers: List[MailServer]) -> bool:
    receiver_domain = mail.receiver.domain
    receiver_name = mail.receiver.name

    # Finde den Server des Empfängers
    server = find_server(receiver_domain, servers)
    if server is None:
        return False  # Kein Server für die Domain des Empfängers gefunden

    # Finde den Account des Empfängers auf dem Server
    account = find_account(receiver_name, server)
    if account is None:
        return False  # Kein Account für den Empfänger auf dem Server gefunden

    # Füge die Mail zum Posteingang des Empfängers hinzu
    account.inbox.append(mail)
    return True
