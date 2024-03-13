### 2.1
Die Funktion input stellt das Gegenstück zu print dar und ermöglicht es den Benutzer nach einer Text-Eingabe zu fragen:
```
>>> s = input("Geben Sie etwas ein: ")
Geben Sie etwas ein: foo123
>>> s
'foo123'
```
Der Aufruf von input erzeugt dabei zunächst die Ausgabe

Geben Sie etwas ein:

und wartet dann bis der Benutzer eine beliebige Tasteneingabe tätigt (hier foo123) und mit einem Zeilenumbruch (Enter) 
die Eingabe beendet. Die vom Benutzer ein-gegebenen Zeichen werden dann als String zurückgegeben (hier ’foo123’).

### 2.2
Schreiben Sie ein Python-Script fahrenheit.py, welches den Benutzer dazu auffordert einen Celsius-Wert (Fließkommazahl) 

einzugeben und anschließend den entsprechenden, auf zwei Nachkommastellen gerundeten, Fahrenheit-Wert ausgibt.
Der Aufruf des Scripts, bei dem der Benutzer den Celsius-Wert -12.715 eingibt, soll dabei folgende Ausgabe erzeugen:

Celsius: -12.715 
Fahrenheit: 9.11

Hinweis. Zum Runden können Sie die Funktion round verwenden. Konsultieren Sie hierzu help(round) im Python Interpreter.
Hinweis. Strings können wie folgt zu Fließkommazahlen konvertiert werden:
```
>>> float('2.3450')
2.345
```
Versucht man einen String, der keiner Fließkommazahl entspricht, zu konvertieren, wird die Ausführung des Programms 
durch eine Ausnahme zum Absturz gebracht:
```
>>> float('not a number')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: 'not a number'
```
In Ihrem Python-Script dürfen Sie dies ignorieren. Sie können also annehmen, dass der Benutzer stehts eine Fließkommazahl 
eingibt.

### 2.3
Schreiben Sie ein Python-Script kegel.py, welches den Benutzer dazu auffordert die Höhe und den Radius eines Kegels als 
Gleitkommazahlen einzugeben und anschlie-ßend die Mantelfläche des Kegels, auf zwei Nachkommastellen gerundet, ausgibt.

Der Aufruf des Scripts, bei dem der Benutzer den Radius 3.0 und die Höhe 5.0 eingibt, soll dabei folgende Ausgabe erzeugen:

```
Radius: 3.0
Höhe: 5.0
Mantelfläche: 54.96
```

### 2.4
Schreiben Sie ein Python-Script abrunden.py, welches den Benutzer dazu auffor-dert eine beliebige Fließkommazahl einzugeben. 
Anschließend soll die Zahl quadriert werden und das Ergebnis ausgegeben werden.
Die quadrierte Zahl soll nun abgerundet werden. Implementieren sie hierfür minde-stens 3 verschiedene Möglichkeiten. 
Es soll also mindestens dreimal hintereinander die Zahl abgerundet und das Ergebnis ausgegeben werden, jeweils mit einer 
anderen Berechnung. Sie dürfen hierfür nur Methoden aus den bisherigen Vorlesungen 1-2 sowie den Übungsblättern 1-2 benutzen.

Der Aufruf des Scripts bei dem der Benutzer die Zahl 4.5 eingibt, soll dabei folgende Ausgabe erzeugen:

```
Kommazahl: 4.5
Quadriert: 20.25
Methode 1: 20.0
Methode 2: 20.0
Methode 3: 20.0
```