// Sélection des éléments du DOM
const moneyLabel = document.getElementById('moneyLabel');
const playButton = document.getElementById('playButton');
const cashoutButton = document.getElementById('cashoutButton');
const retryButton = document.getElementById('retryButton');
const quitButton = document.getElementById('quitButton');
const messageBox = document.getElementById('messageBox');

// Initialisation des variables du jeu
let money = 0;
let gameOver = false;

// Fonction pour afficher les messages
function showMessage(message) {
    messageBox.textContent = message;
    messageBox.style.display = 'block'; // Afficher la zone de message
    setTimeout(() => messageBox.style.display = 'none', 3000); // Masquer après 3 secondes
}

// Fonction pour mettre à jour l'affichage de l'argent
function updateMoneyLabel() {
    moneyLabel.textContent = `Argent actuel : ${money} €`;
}

// Fonction pour jouer au jeu
function playGame() {
    if (!gameOver) {
        if (Math.random() < 0.01) { // 1 chance sur 100 pour le game over
            gameOver = true;
            showMessage("Game Over ! Vous avez perdu.");
            retryButton.style.display = 'inline-block'; // Afficher le bouton pour réessayer
            playButton.disabled = true; // Désactiver le bouton jouer
        } else {
            money += 1000;
            updateMoneyLabel();
            showMessage("Vous avez gagné 1 000 € !");
        }
    }
}

// Fonction pour encaisser l'argent
function cashout() {
    if (!gameOver) {
        showMessage(`Vous avez encaissé ${money} €`);
        resetGame(); // Réinitialiser le jeu après avoir encaissé
    } else {
        showMessage("Le jeu est terminé. Vous ne pouvez plus encaisser.");
    }
}

// Fonction pour quitter le jeu
function quitGame() {
    if (!gameOver) {
        showMessage(`Vous avez quitté le jeu avec ${money} €`);
    } else {
        showMessage("Le jeu est terminé.");
    }
    setTimeout(() => {
        window.close(); // Attendre 5 secondes avant de fermer la fenêtre
    }, 5000);
}

// Fonction pour réinitialiser le jeu
function resetGame() {
    money = 0;
    gameOver = false;
    updateMoneyLabel();
    retryButton.style.display = 'none'; // Masquer le bouton réessayer
    playButton.disabled = false; // Réactiver le bouton jouer
}

// Gestion des événements des boutons
playButton.addEventListener('click', playGame);
cashoutButton.addEventListener('click', cashout);
retryButton.addEventListener('click', resetGame);
quitButton.addEventListener('click', quitGame);

// Initialisation de l'affichage
retryButton.style.display = 'none'; // Masquer le bouton réessayer au début
