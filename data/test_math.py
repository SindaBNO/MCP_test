# test_math.py
# Test avec bibliothèque math

import math

print("🔢 Tests mathématiques")
print("=" * 40)

# Racines carrées
nombres = [4, 9, 16, 25, 100]
print("\n✅ Racines carrées :")
for n in nombres:
    racine = math.sqrt(n)
    print(f"   √{n} = {racine}")

# Puissances
print("\n✅ Puissances de 2 :")
for i in range(0, 6):
    resultat = 2 ** i
    print(f"   2^{i} = {resultat}")

# Trigonométrie
angle = 45
radians = math.radians(angle)
print(f"\n✅ Trigonométrie pour {angle}° :")
print(f"   sin({angle}°) = {math.sin(radians):.4f}")
print(f"   cos({angle}°) = {math.cos(radians):.4f}")
print(f"   tan({angle}°) = {math.tan(radians):.4f}")

# Constantes
print("\n✅ Constantes mathématiques :")
print(f"   π (pi) = {math.pi:.6f}")
print(f"   e = {math.e:.6f}")

# Arrondi et valeur absolue
valeurs = [3.7, -5.2, 8.9, -2.1]
print("\n✅ Arrondis :")
for v in valeurs:
    print(f"   floor({v}) = {math.floor(v)}, ceil({v}) = {math.ceil(v)}, abs({v}) = {abs(v)}")

print("\n" + "=" * 40)
print("✅ Tests mathématiques réussis !")
