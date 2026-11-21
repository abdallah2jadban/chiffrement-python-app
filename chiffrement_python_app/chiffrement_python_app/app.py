"""
Application Flask pour l'interface de chiffrement
"""

from flask import Flask, render_template, request, jsonify
from chiffrement import (
    chiffrer_chaine_cesar,
    dechiffrer_chaine_cesar,
    vernam_chiffrement,
    vernam_dechiffrement
)
import re

app = Flask(__name__)


@app.route('/')
def index():
    """Page d'accueil"""
    return render_template('index.html')


@app.route('/traiter', methods=['POST'])
def traiter():
    """Traite les requêtes de chiffrement/déchiffrement"""
    try:
        data = request.get_json()
        
        methode = data.get('methode')
        operation = data.get('operation')
        texte = data.get('texte', '').upper()
        cle = data.get('cle', '')
        
        # Validation
        if not texte:
            return jsonify({'erreur': 'Veuillez entrer un texte'}), 400
        
        if not cle:
            return jsonify({'erreur': 'Veuillez entrer une clé'}), 400
        
        # Nettoyer le texte (garder seulement A-Z)
        texte_clean = re.sub(r'[^A-Z]', '', texte)
        
        if not texte_clean:
            return jsonify({'erreur': 'Le texte doit contenir au moins une lettre (A-Z)'}), 400
        
        # Traitement selon la méthode
        if methode == 'cesar':
            # Validation de la clé César
            try:
                clef_num = int(cle)
            except ValueError:
                return jsonify({'erreur': 'La clé César doit être un nombre entier'}), 400
            
            # Chiffrement/Déchiffrement César
            if operation == 'chiffrer':
                resultat, etapes = chiffrer_chaine_cesar(texte_clean, clef_num)
            else:
                resultat, etapes = dechiffrer_chaine_cesar(texte_clean, clef_num)
        
        else:  # Vernam
            # Validation de la clé Vernam
            cle_clean = re.sub(r'[^A-Z]', '', cle.upper())
            
            if len(cle_clean) != len(texte_clean):
                return jsonify({
                    'erreur': f'La clé Vernam doit avoir la même longueur que le texte ({len(texte_clean)} lettres)'
                }), 400
            
            # Chiffrement/Déchiffrement Vernam
            if operation == 'chiffrer':
                resultat, etapes = vernam_chiffrement(texte_clean, cle_clean)
            else:
                resultat, etapes = vernam_dechiffrement(texte_clean, cle_clean)
        
        return jsonify({
            'resultat': resultat,
            'etapes': etapes
        })
    
    except Exception as e:
        return jsonify({'erreur': f'Erreur lors du traitement : {str(e)}'}), 500


if __name__ == '__main__':
    print("=" * 60)
    print("🔐 SERVEUR DE CHIFFREMENT DÉMARRÉ")
    print("=" * 60)
    print("📍 Ouvrez votre navigateur à l'adresse :")
    print("   http://127.0.0.1:5000")
    print("=" * 60)
    app.run(debug=True, host='0.0.0.0', port=5000)
