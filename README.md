Port Scanner en Python
Description
Ce programme est un scanner de ports simple écrit en Python. Il permet de tester la disponibilité des ports sur une adresse IP ou une URL spécifiée. Le programme résout l'URL en adresse IP, puis scanne les ports dans une plage donnée et affiche les ports ouverts ainsi qu'un résumé à la fin.

Fonctionnalités
Résolution d'URL : Convertit une URL en adresse IP.
Scan de Ports : Vérifie l'état (ouvert/fermé) des ports dans une plage spécifiée.
Résumé des Ports Ouverts : Affiche un récapitulatif des ports ouverts à la fin du scan.
Prérequis
Python 3.x
Aucune bibliothèque externe n'est requise. Le programme utilise uniquement les modules standards de Python.

Installation
Aucune installation spécifique n'est nécessaire. Clonez ou téléchargez simplement le fichier main.py.

bash
Copier le code
git clone <url-du-dépôt>
cd <dépôt>
Utilisation
Exécutez le script Python :

bash
Copier le code
python main.py
Lorsque vous y êtes invité, entrez l'adresse IP ou l'URL que vous souhaitez scanner.

Spécifiez la plage de ports à scanner (le port de début et le port de fin).

Le programme affichera les ports ouverts et fermés, suivi d'un résumé des ports ouverts.

Exemple
bash
Copier le code
Entrez l'adresse IP ou l'URL : www.example.com
Entrez le port de début : 20
Entrez le port de fin : 80
Scanning ports from 20 to 80 on <adresse-ip>
Port 20 est fermé.
Port 21 est fermé.
...
Port 80 est ouvert.

Résumé des ports ouverts :
Port 80 est ouvert.
