### 11.1
In dieser Aufgabe sollen Ihre Funktionsdeffinitionen außer einer return-Anweisung keine weiteren Zeilen enthalten, oder 
wie im Hinweis als Variable mit Funktionswert deffiniert werden.
Schreiben Sie eine Funktion compose, die eine einstellige Funktion f und eine zweistellige* Funktion g als Argument 
nimmt und die Funktionskomposition f◦g zurückgibt.
Beispiel:
````python
inc = lambda x: x + 1
mul = lambda x, y: x * y
assert compose(inc, mul)(4, 2) == 9
````

* Eine zweistellige Funktion ist eine Funktion, die zwei Argumente entgegennimmt, wie z.B. Addition.

### 10.2
In dieser Aufgabe sollen Ihre Funktionsdeffinitionen auÿer einer return-Anweisung keine weiteren Zeilen enthalten, oder 
wie im Hinweis als Variable mit Funktionswert deffiniert werden.

#### a)
Schreiben Sie eine Funktion my_filter, welche zwei sets xs und ys entgegen-nimmt und ein neues set mit Elementen 
zurückgibt, welche nur in xs, aber nicht in ys vorkommen.
Beispiel:
````python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
assert my_filter(set1, set2) == {1, 2}
````

#### b)
Schreiben Sie nun eine Funktion my_diff, die wieder zwei sets entgegennimmt und mithilfe von my_filter genau die 
Elemente zurückgibt, welche exakt ein-mal in beiden sets vorkommen.
Beispiel:
````python
set1 = {1, 2, 3}
set2 = {2, 3, 4}
assert my_diff(set1, set2) == {1, 4}
````

### 11.3
In dieser Aufgabe sollen Ihre Funktionsdeffinitionen, außer einer return-Anweisung, keine weiteren Anweisungen 
enthalten, oder wie im Hinweis als Variable mit Funk-tionswert deffiniert werden.
In unixoiden Systemen wie Linux, macOS, FreeBSD, usw. gibt es für Dateien verschiedene Rechte, die sogenannten 
Unix-Dateirechte2. Diese Rechte werden durch Oktalzahlen dargestellt, die im Gegensatz zum Dezimalsystem nicht 10, 
sondern 8 zur Basis haben. Um Verwechslungen zu vermeiden schreibt man Oktalzahlen mit führender 0.
Soll nun der Dateieigentümer Lese- und Schreibzugri˙, alle anderen aber nur Lesezugriff haben, so ist das entsprechende 
Recht mit 0644 kodiert. Diese Oktalzahlen wollen wir nun in Dezimalzahlen umwandeln.
Schreiben Sie eine Funktion octs_to_int, die eine Liste von Oktalziffern als Argu-ment nimmt und die zugehörige postive 
ganze Zahl zurückgibt.
Wie auch im Dezimalsystem werden die Oktalzahlen so interpretiert, dass die erste Zi˙er wie gewohnt den größten 
Exponenten besitzt.
Beispiel:
````python
assert octs_to_int([6, 4, 4]) == 420
````
Verwenden Sie hierfür die reduce-Funktion aus dem Modul functools.

### 11.4
Die Ableitung einer Funktion f : R → R an einer Stelle x0 ist bekanntermaßen der
Grenzwert des Differenzenquotienten limh→0((f(x_0+h)−f(x_0))/h). Durch diese Festlegung erhalten wir eine Funktion D(f), 
die x0 ∈ R jeweils auf diesen Grenzwert abbildet, falls er existiert. Die Funktion D ist offensichtlich eine Funktion 
höherer Ordnung, weil sowohl ihr Argument f als auch ihr Ergebnis eine Funktion ist!
Genauso verhält es sich mit der Integration, nur dass hierbei weitere Argumente ins Spiel kommen.

#### a)
Deffinieren Sie eine Funktion, die aus der Funktion f und der Schrittweite h eine Funktion berechnet, die bei Anwendung 
auf x_0 den zentralen Differenzen-quotienten von f bezüglich x_0 und h berechnet:

D(f, h)(x_0) = ((f(x_0 + h) - f(x_0 - h)) / 2h)

Beispiel:

``differentiate(lambda x: 1 / 2 * x ** 2, 1e-2)(0)`` ``entspricht (lambda x: x)(0)``

Verwenden Sie folgende Signatur für Ihre Implementierung:

``differentiate(f: Callable[[float], float], h: float) -> Callable[[float], float].``

#### b)
Deffinieren Sie nun eine Funktion, die zu einer gegebenen Funktion f und Schrittanzahl n > 0 eine Funktion berechnet, 
die aus ihren beiden Parametern
a und b, mit a < b, eine Approximation des bestimmten Integrals 
$$
\int_{a}^{b} f(x) \, dx
$$

berechnet.
Verwenden Sie zur Approximation des Integrals die Simpsonregel. Setzen Sie
dazu

h = (b-a)/n
x_i = a + ih                                0<=i<=n
$$
s_i = \frac{h}{6} \left[ f(x_i) + 4f\left( \frac{x_i + x_{i+1}}{2} \right) + f(x_{i+1}) \right] \quad 0 \leq i < n
$$

Die gesuchte Approximation ist die Summe der 
$$
s_i \colon I(f, n)(a, b) = \sum_{i=0}^{n-1} s_i
$$

Beispiel:

``integrate(lambda x: math.exp(x), 5)(0, 1)`` entspricht ``(lambda x: math.exp(x) - 1)(1)``

Verwenden Sie die folgende Signatur für Ihre Implementierung:

``integrate(f: Callable[[float], float], n: int) -> Callable[[float, float], float]``.

#### c)
Schreiben Sie für beide Aufgabenteile jeweils einen aussagekräftigen Test. Da Sie hierbei Werte vom Typ float vergleichen 
(siehe Floating-Point-Arithmetik3), verwenden Sie beispielsweise die Funktion approx aus dem Paket pytest.