### 7.1
In dieser Aufgabe werden wir uns mit Ausdrucksbäumen einer kleinen, arithmetischen Sprache beschäftigen. Die Sprache 
soll dabei Variablen, ganze Zahlen, Addition und Multiplikation unterstützen.

Ziel der Aufgabe ist es ein Programm zu schreiben, welches Ausdrücke dieser arithmetischen Sprache als Strings von der 
Kommandozeile einliest, diese in mehreren Schritten nach bestimmten Regeln umformt und dann wieder ausgibt. Zum Beispiel
soll für die Eingabe ((x + x) + (x + x)) folgende Ausgabe erzeugt werden:

```
> ((x + x) + (x + x)) 
= (2 * (x + x))
= (2 * (2 * x))
= ((2 * 2) * x)
= (4 * x)
```
Solche Transformationen finden auch in echten Compilern statt, um den Code vor der Ausführung effizienter zu machen, und 
laufen grob in drei Schritten ab:

- Die Eingabe ist ein String, der durch einen sogenannten Parser in einen Ausdrucksbaum umgewandelt wird. Entspricht der 
- Eingabestring keinem Ausdrucksbaum, so wird ein Syntax-Fehler ausgegeben.
- Der Ausdrucksbaum wird wiederholt umgeformt, wodurch ein neuer Ausdrucksbaum entsteht.
- Wenn keine weiteren Umformungen mehr möglich sind, wird der Ausdrucks-baum wieder zu einem String umgewandelt und ausgegeben.

Der Parser und die Datenstruktur für die Ausdrucksbäume sind bereits vorgegeben und lauten wie folgt:
tree.py
````python
from dataclasses import dataclass
from typing import Optional
from enum import Enum


class OpSym(Enum):
    ADD = "+"
    MUL = "*"


@dataclass
class Var:
    name: str


@dataclass
class Val:
    value: int


@dataclass
class Op:
    sym: OpSym
    left: 'Node'
    right: 'Node'


Node = Var | Val | Op
````

parser.py

````python
from typing import Optional
from exercises_from_proglang.solutions_chatgpt_3_5.sheet_07.tree import Node, Var, Val, Op, OpSym
from ast import NodeTransformer
import ast


# Python comes with the library `ast` to parse python expressions.
# As our arithmetic language is a subset of python, we first parse them as
# python code and then transform the python tree to a `Node`.


class AstToNode(NodeTransformer):
    def visit_Name(self, node):
        return Var(node.id)

    def visit_Constant(self, node):
        return Val(node.value)

    def visit_Add(self, node):
        return OpSym.ADD

    def visit_Mult(self, node):
        return OpSym.MUL

    def visit_BinOp(self, node):
        op = self.visit(node.op)
        left = self.visit(node.left)
        right = self.visit(node.right)
        if isinstance(left, Node) and isinstance(right, Node) and type(op) is OpSym:
            return Op(op, left, right)

    def visit_Expr(self, node):
        return self.visit(node.value)

    def visit_Module(self, node):
        if len(node.body) == 1:
            return self.visit(node.body[0])


def parse(s: str) -> Optional[Node]:
    try:
        n = AstToNode().visit(ast.parse(s))
        if isinstance(n, Node):
            return n
        return None
    except Exception:
        return None
````

Die Umformungen der Ausdrucksbäume und das Konvertieren der Ausdrucksbäume zu Strings müssen Sie aber selbst implementieren.

Bevor wir zur eigentlichen Aufgabenstellung kommen, wollen wir aber zunächst noch etwas darüber nachdenken wie wir am 
besten die Ausdrucksbäume als Python-Datenstruktur modellieren.

Der Baum für den Ausdruck 2 ∗ x + 5 sieht z.B. wie folgt aus:

![img.png](../resources/graph_for_excercise_7_1.png)

Mit der Node-Klasse aus der Vorlesung, können wir diesen Baum wie folgt in Python modellieren:

e = Node(OpSym.ADD, Node(OpSym.MUL, leaf(2), leaf('x')), leaf(5))

Mit dieser Klasse wäre das Pattern Matching aber etwas unschön:

````python
match e:
    case Node(int(i), None, None):
        # This case-branch matches leaf nodes of integer values. 
    case Node(str(x), None, None):
        # This case-branch matches leaf nodes of variables. 
    case Node(str(op), e1, e2):
        # This case-branch matches inner nodes of operators like
        # `e1 + e2` and `e1 * e2` for arbitrary sub-trees e1 and e2.
        # If we wouldn't match for variables before, it would also match variables...
````
Viel besser wäre es wenn wir einfach folgendes schreiben könnten:
````python
e = Op(OpSym.ADD, Op(OpSym.MUL, Val(2), Var('x')), Val(5)) 
match e:
    case Val(i):
        # This case-branch matches leaf nodes of integer values. 
    case Var(x):
        # This case-branch matches leaf nodes of variables. 
    case Op(op, e1, e2):
        # This case-branch matches inner nodes of operators like
        # `e1 + e2` and `e1 * e2` for arbitrary sub-trees e1 and e2.
````
Um dies zu ermöglichen, definieren wir für jede Art von Knoten (Variable, int-Wert, Operator) eine eigene dataclass und 
fassen die Knoten dann als Union-Type zusammen. Da wir genau zwei Operatoren unterstützen (+ und *) definieren wir für 
die Operator-Symbole einen Aufzählungstyp (Enum):

````python
@dataclass 
class Var
    name: str
@dataclass 
class Val:
    value: int
@dataclass
class OpSym(Enum):
    ADD = "+" 
    MUL = "*"
@dataclass 
class Op:
    sym: OpSym 
    left: 'Node' 
    right: 'Node'
Node = Var | Val | Op
````

Ein Objekt vom Typ Node ist also entweder
- ein Objekt vom Typ Var, das einen Variablennamen als String enthält;
- ein Objekt vom Typ Val, das einen Wert vom Typ int enthält; oder
- ein Objekt vom Typ Op, das ein Operatorsymbol (OpSym.ADD oder OpSym.MUL) und dessen Argumente enthält, wobei die Argumente selbst wieder beliebige Ausdrucksbäume vom Typ Node sein können.

Der von uns bereitgestellte Parser versucht Strings in Ausdrucksbäume dieser Form umzuwandeln, und gibt None zurück 
falls der String keinen gültigen Ausdrucksbaum darstellt. Beispiel:

````python
from exercises_from_proglang.solutions_chatgpt_3_5.sheet_07.tree import Node, Var, Val, Op
from exercises_from_proglang.solutions_chatgpt_3_5.sheet_07.parser import parse

# def parse(source_code: str) -> Optional[Node]: [...]

assert parse("2 * x + 5") == Op(OpSym.ADD, Op(OpSym.MUL, Val(2), Var('x')), Val(5))
assert parse("invalid input") == None
````

Implementieren Sie das zu Beginn beschriebene Programm in folgenden Schritten:

#### a)
Schreiben Sie eine Funktion node_to_str, die einen Ausdrucks-baum als Argument nimmt und dessen Darstellung als String 
zurückgibt. Ma-chen Sie die Klammerung von Operatoren explizit und verwenden Sie genau ein Leerzeichen um Operatoren 
von Argumenten zu trennen. Beispiel:

````python
e = Op(OpSym.ADD, Op(OpSym.MUL, Val(2), Var('x')), Val(5))
assert node_to_str(e) == '((2 * x) + 5)'
assert node_to_str(Var('x')) == 'x'
assert node_to_str(Val(2)) == '2'
````

Verwenden Sie hierzu Pattern Matching und keine if-Verzweigungen.

Hinweis. Die Alternativen von Aufzählungstypen haben ein Feld value, welches den Wert der Alternative zurückgibt. Beispiel:
````python
assert OpSym.ADD.value == "+"
````

#### b)
Schreiben Sie zum Vergleich eine alternative Implementierung von node_to_str, die if-Verzweigungen aber kein Pattern 
Matching verwendet. Nennen Sie diese Funktion node_to_str_if.

#### c)
Schreiben Sie eine Funktion optimize_step, die einen Ausdrucks-baum e als Argument nimmt und versucht den Ausdrucksbaum 
durch Anwenden einer Regel umzuformen. Ist dies möglich, so soll der umgeformte Ausdrucksbaum zurückgegeben werden, 
ansonsten None.

Die Regeln sind wie folgt:
- Ist e ein Operator, der auf zwei Zahlen angewendet wird, so soll das Ergebnis der Berechnung zurückgegeben werden. Beispiel:
````python
assert optimize_step(Op(OpSym.MUL, Val(5), Val(3))) == Val(15)
````
- Ist e ein +-Operator, der auf zwei gleiche Argumente angewendet wird, so soll stattdessen eine Multiplikation mit 2 
zurückgegeben werden. Beispiel:
````python
assert optimize_step(Op(OpSym.ADD, Var('x'), Var('x'))) == Op(OpSym.MUL, Val(2), Var('x'))
assert optimize_step(Op(OpSym.ADD, Var('x'), Var('y'))) == None
e = Op(OpSym.MUL, Val(3), Var('x'))
assert optimize_step(Op(OpSym.ADD, e, e)) == Op(OpSym.MUL, Val(2), e)
````
Hinweis: Verwenden Sie Pattern Guards!

- Stellt e einen Ausdruck der Form e1 + (e2 + e3) dar, so soll das Assoziativgesetz angewandt werden, also der Ausdruck 
(e1 + e2) + e3 zurückgegeben werden. Analog für * statt +.
- Trifft keine der vorherigen Regeln zu und e ist die Anwendung eines Operators, so soll versucht werden optimize_step 
auf die Argumente des Operators anzuwenden.

Da es sich bei optimize_step um die Anwendung einer einzelnen Regel handelt, soll erst versucht werden das erste 
Argument umzuformen, und nur wenn das erste Argument nicht umgeformt werden konnte, soll
versucht werden das zweite Argument umzuformen. Beispiel:

````python
e1 = Op(OpSym.MUL, Val(2), Val(3))
e2 = Op(OpSym.MUL, Val(3), Val(2))
assert optimize_step(Op(OpSym.ADD, e1, e2)) == Op(OpSym.ADD, Val(6), e2) 
assert optimize_step(Op(OpSym.ADD, Val(6), e2)) == Op(OpSym.ADD, Val(6), Val(6)) 
assert optimize_step(Op(OpSym.ADD, Val(6), Val(6))) == Val(12)
assert optimize_step(Val(12)) == None
````

Versuchen Sie die Regeln in der hier angegebenen Reihenfolge anzuwenden. Verwenden Sie zur Unterscheidung der einzelnen 
Regeln Pattern Matching und keine if-Verzweigungen.

#### d)
Schreiben Sie zum Vergleich eine alternative Implementierung von optimize_step, die if-Verzweigungen aber kein Pattern 
Matching verwendet. Nennen Sie diese Funktion optimize_step_if.

#### e)
Schreiben Sie eine Funktion optimize, die einen Ausdrucksbaum e als Argument nimmt, diesen so lange mit optimize_step 
umformt bis keine Regeln mehr greifen und dann eine Liste aller Zwischenergebnisse inklusive e zurückgibt.
Beispiel:
````python
assert optimize(parse('(x + x) + (x + x)')) == [
    parse('(x + x) + (x + x)'), 
    parse('(2 * (x + x))'), 
    parse('(2 * (2 * x))'), 
    parse('((2 * 2) * x)'), 
    parse('(4 * x)')
]
````

#### f)
Verwenden Sie die Funktionen parse, optimize und node_to_str, um eine “Optimizer REPL”3 zu implementieren, wie im 
Einleitungsbeispiel beschrieben. Bevor die Benutzereingabe zu einem Baum umgewandelt wird, soll dabei überprüft werden, 
ob diese gleich "quit" ist und in diesem Fall das Programm beendet werden. Ungültige Benutzereingaben sollen mit einer 
Fehlermeldung ignoriert werden. Die Ausgabe soll dabei exakt die Form wie im folgenden Beispiel haben.

Beispiel:
````
$ python3 optimizer.py
> (x + x) + (x + x) = ((x + x) + (x + x)) = (2 * (x + x))
= (2 * (2 * x))
= ((2 * 2) * x)
= (4 * x)

> 5 ( 23
Syntax error.

> (5 + 3) * (2 + 8) 
= ((5 + 3) * (2 + 8)) 
= (8 * (2 + 8))
= (8 * 10)
= 80

> quit
Good bye!
````