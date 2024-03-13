from mail import Mail, MailAddress, MailAccount, MailServer, \
    deliver_all_mail, show_mail_server


def test_mail():
    # test Mail and MailAddress
    subject: str = "Super important stuff!"
    body: str = "Actually... it's not that important.\n\nSincerely,\nMe"
    my_mail = Mail(
        MailAddress("me", "mymail.com"),
        MailAddress("you", "yourmail.com"),
        subject, body)
    assert my_mail.sender.name == "me"
    assert my_mail.sender.domain == "mymail.com"
    assert my_mail.receiver.name == "you"
    assert my_mail.receiver.domain == "yourmail.com"
    assert my_mail.subject == subject
    assert my_mail.body == body

    # test MailServer
    servers = [
        MailServer("mymail.com", [
            MailAccount("me", [], [my_mail])
        ]),
        MailServer("yourmail.com", [
            MailAccount("you", [], [])
        ]),
    ]
    assert servers[0].accounts[0].name == "me"
    assert servers[1].accounts[0].name == "you"

    assert len(servers[0].accounts[0].inbox) == 0
    assert servers[0].accounts[0].outbox[0].subject == subject
    assert len(servers[1].accounts[0].inbox) == 0
    assert len(servers[1].accounts[0].outbox) == 0

    # test show_mail_server and deliver_all_mail
    print("–– Before delivery ––––––––––––––––––––––––––––––––––")
    for server in servers:
        print(show_mail_server(server) + "\n")

    deliver_all_mail(servers)

    print("–– After delivery ––––––––––––––––––––––––––––––––––")
    for server in servers:
        print(show_mail_server(server) + "\n")

    assert len(servers[0].accounts[0].inbox) == 0
    assert len(servers[0].accounts[0].outbox) == 0
    assert servers[1].accounts[0].inbox[0].subject == subject
    assert len(servers[1].accounts[0].outbox) == 0


if __name__ == "__main__":
    test_mail()
