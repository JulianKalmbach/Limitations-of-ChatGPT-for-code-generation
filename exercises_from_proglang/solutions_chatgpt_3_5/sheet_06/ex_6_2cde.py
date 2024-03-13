def find_server(domain, servers):
    for server in servers:
        if server.domain == domain:
            return server
    return None

def find_account(name, server):
    for account in server.accounts:
        if account.name == name:
            return account
    return None

def deliver_mail(email, servers):
    receiver_domain = email.receiver.domain
    receiver_server = find_server(receiver_domain, servers)
    if receiver_server is not None:
        receiver_account = find_account(email.receiver.name, receiver_server)
        if receiver_account is not None:
            receiver_account.inbox.append(email)
            return True
    return False

def deliver_all_mail(servers):
    for server in servers:
        for account in server.accounts:
            for email in account.outbox[:]:  # Iterate over a copy of the outbox to allow removal
                if email.sender.name == account.name and email.sender.domain == server.domain:
                    if deliver_mail(email, servers):
                        account.outbox.remove(email)
                else:
                    account.outbox.remove(email)