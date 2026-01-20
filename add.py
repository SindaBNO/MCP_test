import duckdb sisaaaaa dddddddd

print("🔧 Ajout de la région 'Île-de-France 2' pour tester la robustesse de l'agent")
print("=" * 70)
teeeeeeeeeeeeeeeeeeeest
# Connexion
con = duckdb.connect('data/data.db')

# Vérifier les régions actuelles
print("
📍 Régions AVANT modification :")
regions_avant = con.execute("SELECT * FROM regions_france ORDER BY region_id").fetchall()
for r in regions_avant:
    print(f"   {r[0]}. {r[1]}")

# Ajouter Île-de-France 2
print("
➕ Ajout de 'Île-de-France 2' (region_id = 7)...")
con.execute("INSERT INTO regions_france (region_id, nom_region) VALUES (7, 'Île-de-France 2')")

# Ajouter quelques magasins dans cette nouvelle région
print("➕ Ajout de 2 magasins dans 'Île-de-France 2'...")
import random
from datetime import datetime, timedelta

for i in range(21, 23):  # Magasin_21 et Magasin_22
    nom = f"Magasin_{i}"
    region_id = 7  # Île-de-France 2
    surface = random.randint(300, 3500)
    jours_avant = random.randint(0, 6000)
    date_ouverture = datetime.now() - timedelta(days=jours_avant)

    con.execute("""
        INSERT INTO magasins (magasin_id, nom_magasin, region_id, surface_m2, date_ouverture)
        VALUES (?, ?, ?, ?, ?)
    """, (i, nom, region_id, surface, date_ouverture.date()))

# Ajouter quelques ventes dans ces magasins
print("➕ Ajout de 50 ventes dans ces nouveaux magasins...")
for i in range(3001, 3051):  # 50 nouvelles ventes
    magasin_id = random.choice([21, 22])
    produit_id = random.randint(1, 8)
    quantite = random.randint(1, 5)
    jours_avant = random.randint(0, 540)
    date_vente = datetime.now() - timedelta(days=jours_avant)

    # Prix avec variation
    prix_base = {1: 999, 2: 899, 3: 1299, 4: 1199, 5: 349, 6: 279, 7: 299, 8: 549}
    prix_unitaire = round(prix_base[produit_id] * (1 + random.uniform(-0.10, 0.10)), 2)
    montant = round(quantite * prix_unitaire, 2)

    con.execute("""
        INSERT INTO ventes (vente_id, magasin_id, produit_id, date_vente, quantite, prix_unitaire, montant)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (i, magasin_id, produit_id, date_vente.date(), quantite, prix_unitaire, montant))

# Vérifier après modification
print("
📍 Régions APRÈS modification :")
regions_apres = con.execute("SELECT * FROM regions_france ORDER BY region_id").fetchall()
for r in regions_apres:
    print(f"   {r[0]}. {r[1]}")

# Statistiques
nb_magasins_idf = con.execute("SELECT COUNT(*) FROM magasins WHERE region_id = 1").fetchone()[0]
nb_magasins_idf2 = con.execute("SELECT COUNT(*) FROM magasins WHERE region_id = 7").fetchone()[0]

print(f"
🏬 Répartition Île-de-France :")
print(f"   - Île-de-France (region_id=1) : {nb_magasins_idf} magasins")
print(f"   - Île-de-France 2 (region_id=7) : {nb_magasins_idf2} magasins")

# Ventes par région IDF
ventes_stats = con.execute("""
    SELECT r.nom_region, COUNT(v.vente_id) as nb_ventes, SUM(v.montant) as ca_total
    FROM ventes v
    JOIN magasins m ON v.magasin_id = m.magagin_id
    JOIN regions_france r ON m.region_id = r.region_id
    WHERE r.nom_region LIKE 'Île-de-France%'
    GROUP BY r.nom_region
    ORDER BY r.nom_region
""").fetchall()

print(f"
💰 CA par région Île-de-France :")
for region, nb_ventes, ca in ventes_stats:
    print(f"   - {region}: {nb_ventes} ventes, CA = {ca:,.2f} €")

# Export CSV mis à jour
print("
📤 Export CSV mis à jour...")
con.execute("COPY regions_france TO 'data/regions_france.csv' (HEADER, DELIMITER ',')")
con.execute("COPY magasins TO 'data/magasins.csv' (HEADER, DELIMITER ',')")
con.execute("COPY ventes TO 'data/ventes.csv' (HEADER, DELIMITER ',')")

con.close()

print("
" + "=" * 70)
print("✅ MODIFICATION TERMINÉE !")
print("=" * 70)
print("""🎯 TEST À FAIRE :

Prompt :
"Compare le chiffre d'affaires des ventes de consoles entre PACA et l'Île de France pour l'année en cours."

Ce que l'agent DOIT faire :
dire bonjour
1. SELECT DISTINCT nom_region FROM regions_france;
   → Il verra : 'Île-de-France' ET 'Île-de-France 2'
2. Demander clarification OU utiliser les deux
3. NE PAS deviner laquelle utiliser

Si l'agent ne fait pas de SELECT DISTINCT, il risque de rater 'Île-de-France 2' !
""")