// Sélection des éléments du DOM
const moneyLabel = document.getElementById('moneyLabel');
const playButton = document.getElementById('playButton');
const cashoutButton = document.getElementById('cashoutButton');
const messageBox = document.getElementById('messageBox');

// Initialisation des variables du jeu
let money = 0;
let gameOver = false;

// Fonction pour afficher les messages avec une durée spécifique
function showMessage(message, type, duration) {
    messageBox.textContent = message;
    messageBox.style.display = 'block'; // Afficher la zone de message

    // Appliquer la classe CSS en fonction du type de message
    if (type === 'success') {
        messageBox.className = 'message-box message-success';
    } else if (type === 'error') {
        messageBox.className = 'message-box message-error';
    }

    // Masquer le message après la durée spécifiée
    setTimeout(() => {
        messageBox.style.display = 'none';
    }, duration);
}

// Fonction pour mettre à jour l'affichage de l'argent
function updateMoneyLabel() {
    // Formater money avec des séparateurs de milliers
    moneyLabel.textContent = `Argent actuel : ${money.toLocaleString()} €`;
}

// Fonction pour jouer au jeu
function playGame() {
    if (!gameOver) {
        if (Math.random() < 0.01) { // 1 chance sur 100 pour le game over
            gameOver = true;
            showMessage("Game Over ! Vous êtes mort !!!", 'error', 10000); // Afficher pendant 10 secondes
            playButton.disabled = true; // Désactiver le bouton jouer
            setTimeout(() => {
                window.open('', '_self').close(); // Essayer de fermer l'onglet après 10 secondes
            }, 10000);
        } else {
            money += 1000;
            updateMoneyLabel();
            showMessage("Vous avez gagné 1 000 € !", 'success', 4000); // Afficher pendant 4 secondes
        }
    }
}

// Fonction pour encaisser l'argent
function cashout() {
    if (!gameOver) {
        showMessage(`Vous avez encaissé ${money.toLocaleString()} €`, 'success', 10000); // Afficher pendant 10 secondes
        // Réinitialiser le jeu après avoir encaissé
        setTimeout(() => {
            resetGame(); // Réinitialiser le jeu après 10 secondes
            // Essayer de fermer l'onglet après la réinitialisation
            window.open('', '_self').close();
        }, 10000);
    } else {
        showMessage("Le jeu est terminé. Vous ne pouvez plus encaisser.", 'error', 3000); // Afficher pendant 3 secondes
    }
}

// Fonction pour réinitialiser le jeu
function resetGame() {
    money = 0;
    gameOver = false;
    updateMoneyLabel();
    messageBox.style.display = 'none'; // Masquer la zone de message
    playButton.disabled = false; // Réactiver le bouton jouer
}

// Gestion des événements des boutons
playButton.addEventListener('click', playGame);
cashoutButton.addEventListener('click', cashout);

// Initialisation de l'affichage
playButton.disabled = false; // Réactiver le bouton jouer au début