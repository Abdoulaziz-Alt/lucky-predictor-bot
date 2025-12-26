// Code d'accès correct
const ACCESS_CODE = "python124";

// Vérification du code d'accès
function verifyCode() {
    const input = document.getElementById("access-code").value;
    const message = document.getElementById("access-message");

    if (input === ACCESS_CODE) {
        message.textContent = "✅ Code correct ! Accès autorisé.";
        document.getElementById("access-section").style.display = "none";
        document.getElementById("prediction-section").style.display = "block";
    } else {
        message.textContent = "❌ Code incorrect. Réessaie.";
    }
}

// Générer une prédiction aléatoire entre 1.00 et 60.00
function generatePrediction() {
    const result = (Math.random() * 59 + 1).toFixed(2);
    document.getElementById("prediction-result").textContent =
        `🚀 Nouvelle prédiction Lucky Jet : ${result}x`;
}

