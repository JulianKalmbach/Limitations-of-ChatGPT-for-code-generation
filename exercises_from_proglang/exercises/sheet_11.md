### 10.1
In dieser Aufgabe sollen Ihre Funktionsdeffnitionen außer einer return-Anweisung keine weiteren Zeilen enthalten, oder 
wie im Hinweis als Variable mit Funktionswert deffniert werden.
Schreiben Sie eine Funktion compose, die eine einstellige Funktion f und eine zweistellige* Funktion g als Argument 
nimmt und die Funktionskomposition f◦g zurückgibt.
Beispiel:
````python
inc = lambda x: x + 1
mul = lambda x, y: x * y
assert compose(inc, mul)(4, 2) == 9
````

* Eine zweistellige Funktion ist eine Funktion, die zwei Argumente entgegennimmt, wie z.B. Addition.