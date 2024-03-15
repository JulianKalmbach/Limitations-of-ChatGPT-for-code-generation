### 10.1
Die Studierenden des Kurses Einführung in die Programmierung haben eine Klausur geschrieben. Um die Auswertung der Noten 
zu automatisieren, werden die Punkte jedes einzelnen Studierenden in einem dictionary als ganze Zahl gespeichert. 
Dieses Dictionary speichert die Namen der Studierenden in den Schlüsseln (keys) und die erreichten Punkte in den 
zugehörigen Werten (values). Beispiel:
````
>>> student_points = {"Adam": 63, "John": 112, "Donald": 43}
````
#### a)

Bei der Erstkorrektur sind den Tutoren ein paar Fehler unterlaufen. So kann es sein, dass manche Studierenden noch 
Zusatzpunkte bekommen, manche jedoch auch Punkte verlieren. Ein übermotivierter Assistent der Vorlesung legt aus diesem 
Grund ein zweites Dictionary an, das die Änderungen (sowohl negative wie auch positive) speichert. Schreiben Sie eine 
Funktion update_points die beide Dictionary als Eingabe bekommt und die neue Gesamtpunktzahl be-rechnet. Beispiel:

```
>>> changes = {"Adam": 3, "John": -7}
>>> update_points(student_points, changes)
>>> student_points
{ 'Adam': 66, 'John': 105, 'Donald': 43}
```

Nehmen Sie an die maximale Punktzahl sei 120. Wenn die neu berechneten Punkte über 120 oder unter 0 liegen sollten, 
soll ein ValueError mit der Fehler-meldung "Die Gesamtpunktzahl muss zwischen 0 und 120 liegen" geworfen werden.
Sollte in changes ein Name vorkommen, der nicht in den student_points vorkommt, soll ein KeyError mit der Fehlermeldung 
"[Name] wurde nicht ge-funden" geworfen werden. Hierbei ist [Name] der Platzhalter für den Namen des Studierenden.

#### b)
Schreiben Sie eine Funktion compute_grade(student_points: dict[str, int], max_points: int, student_name: str) -> int, 
welche die Note für einen beliebigen Studierenden berechnet. Es gibt die Noten 1, 2, 3, 4 und 5. Diese werden wie folgt 
aus der Maximalpunktzahl der Klausur (max_points), der ge-sondert zu berechnenden Mindestpunktzahl zum Bestehen 
(pass_points) und den vom Studierenden erreichten Punkte (student_points) berechnet:

- Der Studierende hat nicht bestanden (Note 5), wenn weniger Punkte erreicht wurden als die Mindestpunktzahl (pass_points) angibt.
- Die anderen 4 Noten sind gleich unter den restlichen Punkten verteilt, sprich, weniger als 25% der Punkte entsprechen 
einer 4. Mehr, aber weniger als 50% einer 3 usw... Beispiel: Bei 120 maximalen Punkten und einer Mindestpunktzahl von 
60, bekommt man für 60 - 74 Punkte eine 4, für 75 - 89 Punkte eine 3, für 90 - 104 Punkte eine 2 und für mehr als 104 
Punkte eine 1.
- Die Mindestpunktzahl wird wie folgt berechnet: ```pass_points = max_points // 2```
- Zur Unterstützung seines Wahlkampfs fordert Ex-Präsident T., dass die Durchfallquote aller Klausuren bei höchstens 40% 
liegen darf. Sollte das in dieser Klausur nicht der Fall sein, werden die pass_points so weit nach unten angepasst, 
bis die Forderung erfüllt ist.

Als Eingabe soll die Funktion wie gehabt das student_points Dictionary bekommen, ebenso wie die max_points und den 
Namen des Studierenden als String.
````
>>> student_points = {"Adam": 63, "John": 112, "Donald": 43}
>>> compute_grade(student_points, 120, "Adam")
4
````
Hinweis: Um den Code übersichtlich zu gestalten ist es hier sinnvoll Hilfsfunktionen zu schreiben. Diese können dann 
auch in der nächsten Teilaufgabe wiederverwendet werden.

#### c)
Implementieren Sie die Funktion cluster_by_grade, welche ein Dictionary mit Noten (keys) und Listen von Studierenden(values) 
zurückgibt. Die Eingabe-parameter sollen student_points und max_points sein. pass_points werden hier auch wieder initial 
auf max_points // 2 gesetzt und bei einer zu hohen Durchfallquote angepasst.
````
>>> student_points = {"Mira": 80, "Olivia": 95, "Emily": 83}
>>> cluster_by_grade(student_points, 120)
{3: ['Mira', 'Emily'], 2: ['Olivia']}
````
Hinweis: Die Reihenfolge, wie die Noten in der Ausgabe erscheinen, spielt keine Rolle. Noten sollen aber nur dann 
angezeigt werden, wenn es mindestens einen Studierenden gibt der diese erzielt hat.

### 10.2
Das Sierpinski-Dreieck ist ein Fraktal, welches als 0L-System wie folgt beschrieben werden kann:
V = {F, G, +, −}
w = F − G − G
P = {F → F − G + F + G − F, G → GG}

Hierbei entsprechen F und G dem Vorwärtszeichnen einer Strecke, + entspricht einer Drehung um 120 nach links und − entspricht einer Drehung um 120 nach rechts.
Implementieren Sie eine Funktion sierpinski(size: int, n: int) zum Zeichnen eines Sierpinski-Dreiecks mit Hilfe des 
turtle-Moduls (siehe Vorlesung), wobei size die jeweilige Streckenlänge und n die Rekursionstiefe 
(bzw. Anzahl Generationen) angibt (analog zur Vorlesung). Das Ergebnis für n = 2 sollte so, oder so ähnlich aussehen 
(die Ausrichtung spielt keine Rolle):

\[Abbildung des Sierpinski-Dreiecks]

### 10.3
In dieser Aufgabe betrachten wir Polynomfunktionen über ganzen Zahlen. Das heißt, Funktionen der Form 

$$
f(x) = \sum_{i=0}^{n} a_ix^i
$$

wobei n ≥ 0 ist, ai eine ganze Zahl für 0 ≤ i ≤ n und an a_n = 0. Auch für x sollen nur ganze Zahlen eingesetzt werden. 
Die Zahl n bezeichnet den Grad der Polynomfunktion.
Die Aufgabe ist nun wie folgt: Gegeben eine geheime Funktion f: int → int, von der nur bekannt ist, dass sie eine 
Polynomfunktion vom Grad n ist. Finden Sie die Koe°zienten a_0, a_1, ..., a_n.
Diese Aufgabe gehen wir Schritt für Schritt an:
#### a)
Ein (ganzzahliges) Polynom vom Grad 1 ist eine lineare Funktion der Form

f (x) = a_0 + a_1x,
wobei a_0 und a_1 ganze Zahlen sind. Hier sind zwei Beispiele für solche Funktionen:
````python
def f10(x: int) → int:
    return 1 + 2 * x
def f11(x: int) → int: 
    return -1 + 3 * x
````

Schreiben Sie eine Funktion def crack_1(f) → list[int]:, sodass
````python
assert crack_1(f10) == [1, 2]
assert crack_1(f11) == [-1, 3]
````
Hinweis: Die crack_1 Funktion kann ihre Argumentfunktion f nur auf ausgewählte Argumente anwenden. Überlegen Sie, 
welche Argumente Ihnen weiter-helfen. Was ergibt sich z.B., wenn Sie die Polynomfunktion f auf Null anwenden? 
Betrachten Sie die Differenzen der Funktionswerte.

#### b)
Betrachten Sie nun ganzzahlige Polynomfunktionen vom Grad 2 wie die folgenden Beispiele:
````python
def f20(x: int) → int:
    return 1 + 2*x + x*x
def f21(x: int) → int:
    return -1 - 4*x + 2 * x * x
def f22(x: int) → int:
    return (x + 1) * (x - 1)
````
Schreiben Sie eine Funktion def crack_2(f) → list[int]:, sodass
````python
assert crack_2(f20) == [1, 2, 1]
assert crack_2(f21) == [-1, -4, 2]
assert crack_2(f22) == [-1, 0, 1]
````
Hinweis: Die crack_2 Funktion muss ihre Argumentfunktion f auf mindestens drei verschiedene, ausgewählte Argumente anwenden.

#### c)
Erweitern Sie den Ansatz auf Polynomfunktionen vom Grad 3, d.h., implementieren Sie crack_3 (f) → list[int], sodass 
````python
def f30(x: int) → int:
    return x * (x + 10) * (x - 5)
assert crack_3(f30) == [0, -50, 5, 1]
````
Zur Kontrolle Ihrer Lösungen verwenden Sie die Funktionen in der zur Verfügung gestellten Datei polynom_test.py wie folgt:
````
>>> from polynom_test import test_many_cracker_n
>>> test_many_cracker_n(1, crack_1)
Passed 1000 tests
>>> test_many_cracker_n(2, crack_2)
Passed 1000 tests
>>> test_many_cracker_n(3, crack_3)
passed 1000 tests
````
polynom_test sieht folgendermaßen aus:
````python
from random import randint
from typing import Callable


def polynom_n(p: list[int]) -> Callable[[int], int]:
    def f(x: int) -> int:
        result = 0
        for a in reversed(p):
            result = x * result + a
        return result
    return f


def test_one_cracker_n(n: int, cracker_n):
    p = []
    for _ in range(n + 1):
        p = p + [randint(-100, 100)]
    print("checking", p)
    c = cracker_n(polynom_n(p))
    assert c == p, f"failed for polynomial {p} found {c}"


def test_many_cracker_n(n: int, cracker_n):
    for _ in range(1000):
        test_one_cracker_n(n, cracker_n)
    print("Passed 1000 tests")
````