# test_pandas.py
# Test avec pandas (si disponible dans PyScript/Pyodide)

try:
    import pandas as pd
    print("✅ Pandas importé avec succès !")
    print("=" * 40)
    
    # Créer un DataFrame simple
    data = {
        'Nom': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'Âge': [25, 30, 35, 28],
        'Ville': ['Paris', 'Lyon', 'Marseille', 'Toulouse'],
        'Score': [85, 92, 78, 95]
    }
    
    df = pd.DataFrame(data)
    
    print("\n📊 DataFrame créé :")
    print(df)
    
    # Statistiques
    print("\n📈 Statistiques sur l'âge :")
    print(f"   Moyenne : {df['Âge'].mean():.1f} ans")
    print(f"   Médiane : {df['Âge'].median():.1f} ans")
    print(f"   Min : {df['Âge'].min()} ans")
    print(f"   Max : {df['Âge'].max()} ans")
    
    print("\n📈 Statistiques sur les scores :")
    print(f"   Moyenne : {df['Score'].mean():.1f}")
    print(f"   Score total : {df['Score'].sum()}")
    
    # Filtrage
    print("\n🔍 Personnes avec score > 85 :")
    filtre = df[df['Score'] > 85]
    for idx, row in filtre.iterrows():
        print(f"   {row['Nom']} : {row['Score']} points")
    
    # Tri
    print("\n📋 Trié par âge (décroissant) :")
    df_trie = df.sort_values('Âge', ascending=False)
    for idx, row in df_trie.iterrows():
        print(f"   {row['Nom']} : {row['Âge']} ans")
    
    print("\n" + "=" * 40)
    print("✅ Tests pandas réussis !")
    
except ImportError:
    print("❌ Pandas n'est pas disponible")
    print("💡 PyScript/Pyodide peut ne pas inclure pandas par défaut")
