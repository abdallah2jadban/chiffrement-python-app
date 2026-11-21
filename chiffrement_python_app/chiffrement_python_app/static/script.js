// Variables globales
let methodeActuelle = 'cesar';
let operationActuelle = 'chiffrer';

// ==================== FONCTIONS D'INTERFACE ====================

// Sélection de la méthode
function selectMethod(methode) {
    methodeActuelle = methode;
    
    // Mise à jour des boutons
    document.getElementById('btnCesar').classList.toggle('active', methode === 'cesar');
    document.getElementById('btnVernam').classList.toggle('active', methode === 'vernam');
    
    // Mise à jour du label de la clé
    const labelCle = document.getElementById('labelCle');
    const inputCle = document.getElementById('inputCle');
    
    if (methode === 'cesar') {
        labelCle.textContent = 'CLÉ (nombre entier)';
        inputCle.placeholder = 'Ex: 3';
    } else {
        labelCle.textContent = 'CLÉ (même longueur que le texte)';
        inputCle.placeholder = 'Ex: CLEF';
    }
    
    // Mise à jour du texte d'information
    const infoText = document.getElementById('infoText');
    if (methode === 'cesar') {
        infoText.innerHTML = '<strong>ℹ️ Info :</strong> Le chiffrement César décale chaque lettre de la clé numérique dans l\'alphabet.';
    } else {
        infoText.innerHTML = '<strong>ℹ️ Info :</strong> Le chiffrement Vernam utilise une clé de même longueur pour chiffrer chaque lettre.';
    }
    
    // Masquer les résultats
    cacherResultats();
}

// Sélection de l'opération
function selectOperation(operation) {
    operationActuelle = operation;
    
    // Mise à jour des boutons
    document.getElementById('btnChiffrer').classList.toggle('active', operation === 'chiffrer');
    document.getElementById('btnDechiffrer').classList.toggle('active', operation === 'dechiffrer');
    
    // Mise à jour du texte du bouton principal
    const btnText = document.getElementById('btnText');
    btnText.textContent = operation === 'chiffrer' ? '🔒 Chiffrer' : '🔓 Déchiffrer';
    
    // Masquer les résultats
    cacherResultats();
}

// Afficher une erreur
function afficherErreur(message) {
    const zoneErreur = document.getElementById('zoneErreur');
    zoneErreur.textContent = '⚠️ ' + message;
    zoneErreur.classList.remove('hidden');
}

// Cacher les résultats
function cacherResultats() {
    document.getElementById('zoneErreur').classList.add('hidden');
    document.getElementById('zoneResultat').classList.add('hidden');
    document.getElementById('zoneEtapes').classList.add('hidden');
    document.getElementById('loader').classList.add('hidden');
}

// Afficher le résultat
function afficherResultat(resultat, etapes) {
    // Masquer l'erreur et le loader
    document.getElementById('zoneErreur').classList.add('hidden');
    document.getElementById('loader').classList.add('hidden');
    
    // Afficher le résultat
    document.getElementById('resultatTexte').textContent = resultat;
    document.getElementById('zoneResultat').classList.remove('hidden');
    
    // Afficher les étapes
    if (etapes && etapes.length > 0) {
        const etapesGrid = document.getElementById('etapesGrid');
        etapesGrid.innerHTML = '';
        
        etapes.forEach(etape => {
            const div = document.createElement('div');
            div.className = 'step-item';
            div.textContent = etape;
            etapesGrid.appendChild(div);
        });
        
        document.getElementById('zoneEtapes').classList.remove('hidden');
    }
}

// ==================== FONCTION PRINCIPALE ====================

// Traiter le chiffrement/déchiffrement avec Python Backend
async function traiter() {
    cacherResultats();
    
    // Récupérer les valeurs
    const texte = document.getElementById('inputTexte').value;
    const cle = document.getElementById('inputCle').value;
    
    // Afficher le loader
    document.getElementById('loader').classList.remove('hidden');
    
    try {
        // Appel à l'API Python Flask
        const response = await fetch('/traiter', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                methode: methodeActuelle,
                operation: operationActuelle,
                texte: texte,
                cle: cle
            })
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            // Afficher l'erreur retournée par Python
            afficherErreur(data.erreur || 'Erreur lors du traitement');
            return;
        }
        
        // Afficher le résultat
        afficherResultat(data.resultat, data.etapes);
        
    } catch (error) {
        console.error('Erreur:', error);
        afficherErreur('Erreur de communication avec le serveur Python');
    }
}

// Réinitialiser le formulaire
function reinitialiser() {
    document.getElementById('inputTexte').value = '';
    document.getElementById('inputCle').value = '';
    cacherResultats();
}

// ==================== ÉVÉNEMENTS ====================

// Permettre la validation avec la touche Entrée
document.addEventListener('DOMContentLoaded', function() {
    const inputTexte = document.getElementById('inputTexte');
    const inputCle = document.getElementById('inputCle');
    
    inputTexte.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            traiter();
        }
    });
    
    inputCle.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            traiter();
        }
    });
});
