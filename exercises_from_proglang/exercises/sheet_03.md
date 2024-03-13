### 3.1 Importieren von eigenen Modulen
In dieser Aufgabe sollen Sie Ihre Lösung zur Berechnung der Mantelfläche eines Kegels aus Aufgabe 2.3 des letzten 
Übungsblattes umschreiben und dabei Funktionen und mehrere Dateien verwenden. Falls Sie die Aufgabe auf dem vorherigen 
Übungsblatt nicht gelöst haben, können Sie die Musterlösung als Ausgangspunkt verwenden.
#### a)
Erstellen Sie die Datei cone_area_lib.py und definieren Sie dort
eine Funktion cone_area, welche den Radius und die Höhe eines Kegels als Argumente vom Typ float entgegen nimmt und die 
Mantelfläche des Kegels
als Wert vom Typ float zurückgibt.
Die Funktion soll keine Seiteneffekte haben, d.h. sie soll ausschließlich die Ar-gumente verwenden um die Mantelfläche 
zu berechnen und diese zurückgeben, aber keine Funktionen wie print oder input aufrufen.
Beispielaufruf:

```
>>> cone_area(3.0, 5.0)
54.96
```

#### b)
Erstellen Sie die Datei cone_area_app.py und importieren Sie dort
die Funktion cone_area aus der Datei cone_area_lib.py.

Verwenden Sie die Funktionen cone_area, input und print um das gleiche Verhalten wie bei Aufgabe 2.3 zu erzeugen, d.h. 
das Ausführen von cone_area_app.py soll für einen Kegel mit Radius 3 und Höhe 5 folgende Ausgabe erzeugen:
```
$ python3 cone_area_app.py
Radius: 3.0
Höhe: 5.0
Mantelfläche: 54.96
```
Die if-Verzweigung mit der Variable __name__ ist hier nicht notwendig, da die cone_area_app.py keine Definitionen 
bereitstellt und es daher auch keinen Sinn ergibt sie in eine anderen Python-Datei zu importieren.

### 3.2 Importieren von eigenen Modulen
In dieser Aufgabe sollen Sie ein Programm schreiben, welches eine Temperatur in Celsius (C), Fahrenheit (F) oder 
Kelvin (K) entgegen nimmt und diese zu einer ande-ren Temperatureinheit konvertiert und ausgibt.
Ruft man das Programm auf, um 42 Grad Celsius nach Kelvin zu konvertieren, soll dabei exakt die folgende Ein- und Ausgabe 
erscheinen (Benutzereingaben in blau hervorgehoben):
```
$ python3 temperature.py
Enter source unit [C / F / K]: C
Enter source value: 42.0
Enter target unit [C / F / K]: K
42.0 C corresponds to 315.15 K.
```

Gehen Sie dabei wie folgt vor:

#### a)
Definieren Sie die folgenden Funktionen:
- celsius_to_fahrenheit
- fahrenheit_to_celsius
- celsius_to_kelvin
- kelvin_to_celsius

Die Funktionen sollen die Temperatur als Argument vom Typ float entgegennehmen und die entsprechend konvertierte 
Temperatur als Wert vom Typ float zurückgeben.
Wie in der vorherigen Aufgabe, sollen diese Funktionen keine Seiteneffekte haben.
Beispielaufruf:
```
>>> celsius_to_fahrenheit(42.0)
107.6
```

#### b)
 Definieren Sie die Funktionen
- fahrenheit_to_kelvin
- kelvin_to_fahrenheit

Rufen Sie hierzu mehrere Funktionen aus dem vorherigen Aufgabenteil auf, anstatt die mathematischen Formeln zur 
Konvertierung direkt zu verwenden.

#### c)
Verwenden Sie die Funktionen aus den vorherigen Aufgabenteilen zusammen mit input, print und if-Verzweigungen, um das 
gewünschte Verhalten zu erzeugen (wie im Einleitungstext der Aufgabe beschrieben).
Verwenden Sie die Technik mit der __name__-Variable, um sicherzustellen, dass dieser Code nur ausgeführt wird, wenn die 
Datei auch als Programm ausgeführt wird (und nicht importiert wird).