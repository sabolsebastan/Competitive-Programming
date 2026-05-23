# Competitive Programming — Zenit 2026

## Pocas sutaze — rychla navigacia

| Co hladaz | Subor |
|-----------|-------|
| Hash counter, dictionary | `drills/week01_hash_counter.py` |
| String search, split() | `solutions/zenit/2025_skolske/uloha_d.py` |
| Stack zatvorky | `solutions/zenit/2025_skolske/uloha_e.py` |
| Fast I/O | `import sys; input = sys.stdin.readline` |

## Vzory ktore sa opakuju

```python
# Counter pattern
count = {}
count[x] = count.get(x, 0) + 1

# Split vstup — cisla
cisla = list(map(int, input().split()))

# Split vstup — text
slova = sys.stdin.read().split()

# Vystup listu
print(*result)

# Otocenie stringu
text[::-1]

# Palindrom
text == text[::-1]

# Najvacsi prvok + index
maximum = max(cisla)
idx = cisla.index(maximum)
```

## Python Built-ins

| Funkcia | Co robi |
|---------|---------|
| `max(z)` | najvacsi prvok |
| `min(z)` | najmensi prvok |
| `sum(z)` | sucet |
| `sorted(z)` | zoradeny novy zoznam |
| `z.index(x)` | index prveho vyskytu x |
| `len(z)` | dlzka |
| `enumerate(z)` | (index, hodnota) pary |
| `zip(a, b)` | spoji dva zoznamy |
| `Counter(z)` | pocitanie vyskytov |

## Progres

| Tyzden | Tema | Uloha |
|--------|------|-------|
| 1 | Hash counter | zenit25sk_g |
| 1 | String search | zenit25sk_d |
| 2 | Stack zatvorky | zenit25sk_e |
| 2 | Samohlasky | zenit25sk_f |
| 2 | Sucet cisel | zenit25sk_a |
| 2 | Otocenie stringu | drills/test01 |
| 2 | Palindrom | drills/test02 |
| 2 | Najvacsi prvok | drills/test03 |
