import random

# ===== CONFIG =====
ACCESS_CODE = "python124"

# ===== FONCTION DE PRÉDICTION =====
def nouvelle_prediction():
    valeur = round(random.uniform(1.00, 60.00), 2)
    print(f"\n🚀 Nouvelle prédiction Lucky Jet : {valeur}x\n")

# ===== INTERFACE SIMPLIFIÉE =====
def main():
    print("👋 Bienvenue sur Lucky Predictor !")
    
    # Demande du code d'accès
    code = input("🔐 Veuillez entrer votre code d'accès : ").strip()
    
    if code != ACCESS_CODE:
        print("❌ Code incorrect. Redémarre l'application et réessaie.")
        return
    
    print("✅ Code correct ! Accès autorisé.\n")
    
    # Simulation d'un bouton "Recevoir une prédiction"
    input("📊 Appuie sur Entrée pour recevoir une prédiction...")
    nouvelle_prediction()

if __name__ == "__main__":
    main()

