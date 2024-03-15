### 6.1
In dieser Aufgabe sollen Sie die Lagerbestände eines Supermarkts modellieren. Der Lagerbestand einer Ware ist entweder 
verzehrbar oder nicht-verzehrbar.

Sie können die gesamte Funktionalität mit dem beigefügten Skript test_supermarket.py testen. Das Testskript soll nicht 
verändert werden.

#### a)
Erstellen Sie zunächst zwei Datenklassen Food und NonFood, wobei NonFood ei-ne leere Klasse ist und Food ein 
Mindesthaltbarkeitsdatum enthält. Modellieren Sie das Datum dabei als einen String, der für den 14. Februar 2021 das 
Format "2021-02-14" hat1. Dieses Format erlaubt es, die lexikographische Ordnung zu verwenden, um herauszufinden ob eines 
von zwei Daten weiter in der Zukunft liegt als das andere.

Erstellen Sie die Datenklasse Stock mit folgenden Feldern: Namen der Ware name, Anzahl der gelagerten Waren units, 
Stückpreis in Cents price_per_unit sowie kind. Das Feld kind soll eine Instanz der Datenklassen Food oder NonFood 
enthalten, definieren Sie es also als Union-Typ über die beiden Datenklassen.

#### b)
Schreiben Sie eine Funktion is_expired, die einen Lagerbestand und ein Datum als Argumente nimmt und zurückgibt, ob 
der Lagerbestand zu diesem Datum abgelaufen ist. Verzehrbare Waren gelten dabei ab einem Tag nach ihrem 
Mindesthaltbarkeitsdatum als abgelaufen. Nichtverzehrbare Waren gelten nie als abgelaufen. Verwenden Sie Pattern 
Matching, um den Inhalt des Feldes kind zu prüfen.

#### c)
Schreiben Sie eine Funktion get_expired, die eine Liste von Lagerbeständen und ein Datum als Argumente nimmt und eine 
Liste derjenigen Lagerbestände zurückgibt, die zu dem Datum abgelaufen sind.

#### d)
Schreiben Sie eine Funktion buy, die einen Lagerbestand und eine Stückzahl als Argumente nimmt, den Lagerbestand um die 
Stückzahl der Waren verringert, und die Anzahl der gekauften Waren zurückgibt.

Der Lagerbestand soll dabei nie weniger als 0 Waren enthalten, d.h. wenn mehr Waren gefordert werden als im Lagerbestand 
verfügbar sind, so sollen nur die verfügbaren Waren verbucht werden.

### 6.2
In dieser Aufgabe sollen Sie den Versand von E-Mails zwischen mehreren Mailservern modellieren.

Eine E-Mail-Adresse MailAddress besteht aus einem Namen name und einer Domain domain.

Eine E-Mail Mail besteht aus den E-Mail-Adressen von Absender sender und Emp-fänger receiver, einem Betreff subject und 
dem Nachrichtenkörper body.

Ein E-Mail-Account MailAccount besteht aus einem Namen name und jeweils einer Liste von E-Mails für den Posteingang 
inbox und den Postausgang outbox.

Ein Mailserver MailServer besteht aus einer Domain domain und einer Liste von E-Mail-Accounts accounts.

Sie können die gesamte Funktionalität mit dem beigefügten Skript test_mail.py testen. Das Testskript soll nicht 
verändert werden.

#### a)
Modellieren Sie das oben beschriebene Szenario mit 4 Datenklassen.

#### b)
Schreiben Sie Funktionen show_mail_address, show_mail, show_mail_account, und show_mail_server, die eine Instanz der 
jeweiligen Datenklassen als Argu-ment nehmen, zu einem lesbaren String umwandeln und diesen zurückgegeben. Hierbei sollen 
alle Felder der Datenklasse im String dargestellt werden.

Die Funktionen show_mail_address und show_mail sollen sich dabei exakt wie im folgenden Beispiel verhalten

```
>>> print(show_mail_address(MailAddress("me", "mydomain.com"))) me@mydomain.com
>>> mail = Mail(
            MailAddress("me", "mydomain.com"),
            MailAddress("you", "yourdomain.com"),
            "Important!!1",
            "Hi you,\n\nmaybe it's not that important after all...")
>>> print(show_mail(mail))
From: me@mydomain.com
To: you@yourdomain.com
Subject: Important!!1
Hi you,
maybe it's not that important after all...
```

#### c)
Schreiben Sie eine Funktion find_server, die eine Domain und eine Liste von Mailservern als Argumente nimmt und die 
Liste nach einem Mailserver durch-sucht, der die gefragte Domain hat. Wird solch ein Server gefunden, so soll dieser 
zurückgegeben werden, ansonsten soll als Alternative None zurückgegeben werden. Denken Sie daran, die Alternative im 
Rückgabetyp zu berücksichtigen. Schreiben Sie eine Funktion find_account, die analog zu find_server einen Mailserver 
nach einem Account mit einem bestimmten Namen durchsucht.

#### d)
Schreiben Sie eine Funktion deliver_mail, die eine E-Mail und eine Liste von Mailservern als Argumente nimmt, und 
versucht die E-Mail ihrem Empfänger zuzustellen. Wird der Empfänger gefunden, so soll die E-Mail im Posteingang des 
Empfänger-Accounts hinzugefügt werden und True zurückgegeben werden. Wird der Empfänger nicht gefunden, soll False 
zurückgegeben werden.

#### e)
Schreiben Sie eine Funktion deliver_all_mail, die eine Liste von Mailservern als Argument nimmt, und versucht, die 
E-Mails in den Postausgängen aller Ac-counts mit deliver_mail zuzustellen. Die Zustellung wird nur versucht, wenn die 
Absenderadresse authentisch ist, d.h. wenn der Name der Adresse mit dem Accountnamen übereinstimmt und die Domain der 
Adresse mit der Domain des Servers. E-Mails, deren Absenderadresse nicht authentisch ist, werden gelöscht. Nach 
erfolgreicher Zustellung wird die E-Mail aus dem Postausgang entfernt. Andernfalls verbleibt sie im Postausgang.