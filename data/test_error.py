# test_error.py
# Test de gestion d'erreur

print("🧪 Test de gestion d'erreur")
print("=" * 40)

# Test 1 : Code qui fonctionne
print("\n✅ Test 1 - OK :")
x = 10
y = 5
print(f"   {x} / {y} = {x / y}")

# Test 2 : Division par zéro
print("\n⚠️ Test 2 - Division par zéro :")
try:
    resultat = 10 / 0
    print(f"   Résultat : {resultat}")
except ZeroDivisionError as e:
    print(f"   ❌ Erreur capturée : {e}")

# Test 3 : Variable non définie
print("\n⚠️ Test 3 - Variable non définie :")
try:
    print(variable_inexistante)
except NameError as e:
    print(f"   ❌ Erreur capturée : {e}")

# Test 4 : Conversion impossible
print("\n⚠️ Test 4 - Conversion impossible :")
try:
    nombre = int("abc")
except ValueError as e:
    print(f"   ❌ Erreur capturée : {e}")

print("\n" + "=" * 40)
print("✅ Tests de gestion d'erreur terminés !")
