# Password-Generator-and-Port-Scanner
Scripts Python orientés cybersécurité : générateur de mots de passe sécurisés et scanner de ports TCP. Projet pratique pour progresser en automatisation et en sécurité réseau.

# 🔐 Password Generator & Port Scanner — Projet Cybersécurité

## 📌 Introduction
Ce dépôt contient deux outils pédagogiques développés en Python pour s'exercer aux bonnes pratiques en cybersécurité et scripting :  
- un **générateur de mots de passe sécurisés** (`password_generator.py`) ;  
- un **scanner de ports TCP simple** (`port_scanner.py`).  

Le projet vise à documenter la conception, les tests et les difficultés rencontrées (notamment liées aux environnements Windows : encodage UTF-8 et problème LF/CRLF). Tous les scripts sont pensés pour un usage en **laboratoire** uniquement (ne scanner que des cibles autorisées).

---

## 🎯 Objectifs
- Développer des scripts Python simples et robustes appliqués à la sécurité.  
- Comprendre la génération sûre de mots de passe (module `secrets`) et la programmation socket (module `socket`).  
- Mettre en place une organisation de projet reproductible (README, captures, commits GitHub).  
- Rédiger une documentation complète, prête à être présentée à un recruteur.

---

## ❗ Pourquoi ce projet est utile en cybersécurité / réseau
- La génération de mots de passe robustes est une première ligne de défense contre les compromissions de comptes.  
- Le scan de ports est une étape fondamentale de reconnaissance et d'audit (comprendre quels services sont exposés).  
- Savoir automatiser ces tâches en Python est une compétence pratique recherchée pour des postes junior en sécurité/opérations.

---

## 🧭 Niveau & Temps estimé
- **Niveau :** Débutant → Intermédiaire (Python de base).  
- **Temps estimé :** 1–4 heures pour mettre en place, tester et documenter (selon le niveau).

---

## ⚙️ Prérequis (Matériel & Logiciels)
- Système : Windows 10/11, Linux ou macOS.  
- Python 3.8+ installé (vérifier avec `python --version` ou `py --version`).  
- Éditeur de code (Visual Studio Code recommandé).  
- (Optionnel) Git pour versionner et pousser sur GitHub.  

---

## 🗂️ Organisation du dépôt
Password-Generator-and-Port-Scanner/
├── scripts/
│ ├── password_generator.py # Générateur de mots de passe
│ └── port_scanner.py # Scanner de ports simple
├── captures/ # Captures d'écran (exécution + code)
│ ├── capture_tree.png
│ ├── capture_gen_code.png
│ ├── capture_gen_run.png
│ ├── capture_scan_code.png
│ └── capture_scan_run.png
├── README.md
└── LICENSE
