# List Comprehensions et Lambdas — Résumé

## List Comprehensions

Syntaxe pour créer une liste rapidement, en une ligne.

### Forme basique
```python
[expression for item in iterable]
```

Exemple :
```python
# Doubler chaque nombre
nombres = [1, 2, 3, 4]
doubles = [x * 2 for x in nombres]  # [2, 4, 6, 8]
```

### Avec condition (filter)
```python
[expression for item in iterable if condition]
```

Exemple :
```python
# Garder seulement les pairs
nombres = [1, 2, 3, 4, 5, 6]
pairs = [x for x in nombres if x % 2 == 0]  # [2, 4, 6]
```

### Avec transformation + condition
```python
[expression for item in iterable if condition]
```

Exemple :
```python
# Doubler les pairs
pairs_doubles = [x * 2 for x in nombres if x % 2 == 0]  # [4, 8, 12]
```

### Pourquoi c'est utile ?
- Plus court et lisible que des boucles `for`
- Crée la liste **une seule fois** en mémoire
- Souvent exigé dans les exercices 42

---

## Lambdas (fonctions anonymes)

Petites fonctions **sans nom**, définies en une ligne.

### Syntaxe
```python
lambda arguments: expression
```

Exemple simple :
```python
# Une fonction qui double un nombre
double = lambda x: x * 2
print(double(5))  # 10
```

### Avec plusieurs arguments
```python
add = lambda x, y: x + y
print(add(3, 5))  # 8
```

### Principale utilité : avec `filter()`, `map()`, `sorted()`

#### Avec `filter()`
```python
nombres = [1, 2, 3, 4, 5, 6]
pairs = filter(lambda x: x % 2 == 0, nombres)
print(list(pairs))  # [2, 4, 6]
```

#### Avec `map()`
```python
nombres = [1, 2, 3, 4]
doubles = map(lambda x: x * 2, nombres)
print(list(doubles))  # [2, 4, 6, 8]
```

#### Avec `sorted()`
```python
mots = ["apple", "zoo", "car"]
sorted_mots = sorted(mots, key=lambda x: len(x))
print(sorted_mots)  # ['zoo', 'car', 'apple']
```

### Pourquoi c'est utile ?
- Pas besoin de `def` pour une petite fonction d'une ligne
- Idéal avec `filter()`, `map()`, `sorted()`
- Souvent exigé dans les exercices 42

---

## Différence clé

| | List Comprehension | Lambda |
|---|---|---|
| **Crée** | Une liste | Une fonction |
| **Syntaxe** | `[... for ... in ...]` | `lambda x: ...` |
| **Utilité** | Créer/filtrer des listes rapidement | Passer une fonction simple à une autre fonction |
| **Exemple** | `[x*2 for x in [1,2,3]]` | `lambda x: x*2` |

---

## Résumé pour ex06

**List comprehension** dans `filterstring.py` :
```python
res = [word for word in filtered]
```
→ Crée une liste à partir de l'itérateur

**Lambda** dans `filterstring.py` :
```python
lambda x: len(x) > int_value
```
→ Fonction de filtrage rapide passée à `ft_filter()`