### 4.1 assertions
#### a)
Schreiben Sie eine Funktion reverse, die eine Liste als Argument nimmt und eine Liste mit den gleichen Elementen in 
umgedrehter Reihenfolge zurückgibt. Verwenden sie dabei nicht die Funktion reversed die Python bereits zu Verfügung 
stellt, son-dern schreiben Sie die Funktion selbst.

#### b)
Testen Sie die Funktion wie folgt:
```
assert reverse([]) == []
assert reverse([1, 2, 3]) == [3, 2, 1]
assert reverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
```

#### c)
Schreiben Sie eine Funktion only_positive, die eine Liste von ganzen Zahlen als Argument nimmt und eine Liste der Zahlen 
zurückgibt, die positiv sind. Positiv bedeutet, dass die Zahl größer als 0 ist.

#### d)
Testen Sie die Funktion wie folgt:
```
assert only_positive([]) == []
assert only_positive([1, 2, 3]) == [1, 2, 3]
assert only_positive([-8, 1, -5, -9, 2, -7, 3, -6, 0]) == [1, 2, 3]
```

#### e)
Schreiben Sie eine Funktion average, die eine Liste von Gleitkommazahlen als Argument nimmt und den Durchschnitt der 
Zahlen zurückgibt.

#### f)
Testen Sie die Funktion wie folgt:
```python
from math import isclose

eps = 1e-4
assert isclose(average([]), 0.0, abs_tol=eps, rel_tol=eps)
assert isclose(average([1.0]), 1.0, rel_tol=eps)
assert isclose(average([5.0, 10.0, 15.0, 20.0]), 12.5, rel_tol=eps)
```

### 4.2
Schreiben Sie eine Funktion calculate_pi, welche eine ganze Zahl n als Argument nimmt und die Kreiszahl π anhand der 
folgenden Formel annähert:

![img.png](../resources/formular_for_exercise_4_2.png)

Beachten Sie, dass die obige Formel alle Zahlen von 1 bis n einschließt, während in python range(n) alle Zahlen von 0 
bis n − 1 einschließt. Vergessen Sie nicht, die Formel nach π umzustellen. Die Formel geht auf den Mathematiker 
Leonard Euler zurück.

Testen Sie die Funktion wie folgt:
```python
from math import isclose

eps=1e-4
assert isclose(calculate_pi(-3), 0.0, abs_tol=eps, rel_tol=eps) 
assert isclose(calculate_pi(1), 2.44948, rel_tol=eps)
assert isclose(calculate_pi(7), 3.01177, rel_tol=eps)
assert isclose(calculate_pi(1000), 3.14063, rel_tol=eps)
assert isclose(calculate_pi(10000), 3.14149, rel_tol=eps)
```

### 4.3
Primzahlen sind natürliche Zahlen, die durch genau zwei Zahlen teilbar sind: durch 1 und durch sich selbst. 
Insbesondere ist 2 die kleinste Primzahl, eine größte Prim-zahl existiert nicht. Implementieren Sie eine Funktion 
primes, die eine ganze Zahl n als Argument nimmt, sukzessiv alle Primzahlen kleiner oder gleich n berechnet 
und diese in aufsteigender Reihenfolge als Liste zurückgibt. Implementieren Sie dazu die folgende Idee: 
Um zu überprüfen, ob eine Zahl n prim ist, reicht es, diese auf Teil-barkeit durch alle zuvor erzeugten 
Primzahlen ≤ n zu überprüfen. Bereits erzeugte Primzahlen können (und sollten) in einer Liste zwischengespeichert 
werden.

Sie können dabei wie folgt vorgehen:

#### a)
Implementieren Sie zunächst eine Funktion is_prime, die eine ganze Zahl x und eine Liste von ganzen Zahlen ps als 
Argumente nimmt und zurückgibt ob x eine Primzahl ist. Dabei wird angenommen, dass ps die Liste aller Primzahlen 
kleiner x ist.

#### b)
Implementieren Sie dann die Funktion primes unter Verwendung von is_prime.

Testen Sie die Funktion wie folgt:
```python
assert primes(1) == []
assert primes(3) == [2, 3]
assert primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]
```