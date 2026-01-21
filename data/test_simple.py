# test_simple.py
# Test basique pour PyScript/Pyodide

# Test 1 : Affichage simple
print("🚀 Test PyScript - Démarré")
print("=" * 40)

# Test 2 : Variables et calculs
x = 10
y = 20
somme = x + y
print(f"✅ Addition : {x} + {y} = {somme}")

# Test 3 : Boucle
print("\n📊 Table de multiplication de 5 :")
for i in range(1, 6):
    resultat = 5 * i
    print(f"  5 × {i} = {resultat}")

# Test 4 : Fonction
def calculer_carre(nombre):
    return nombre ** 2

print(f"\n🔢 Carré de 7 : {calculer_carre(7)}")

# Test 5 : Liste et manipulation
nombres = [1, 2, 3, 4, 5]
total = sum(nombres)
moyenne = total / len(nombres)
print(f"\n📈 Liste : {nombres}")
print(f"   Total : {total}")
print(f"   Moyenne : {moyenne}")

# Test 6 : Conditions
age = 25
if age >= 18:
    statut = "Majeur"
else:
    statut = "Mineur"
print(f"\n👤 Âge {age} ans → {statut}")

print("\n" + "=" * 40)
print("✅ Tous les tests réussis !")
