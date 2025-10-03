import secrets
import string

def generate_password(length=16, use_specials=True):
    """Génère un mot de passe fort cryptographiquement sûr."""
    alphabet = string.ascii_letters + string.digits
    if use_specials:
        specials = "!@#$%^&*()-_=+[]{};:,.<>?/|"
        alphabet += specials
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def main():
    print("=== Générateur de mots de passe sécurisés ===")
    try:
        length = int(input("Longueur du mot de passe (ex: 16): ").strip() or "16")
    except ValueError:
        print("Entrée invalide — longueur par défaut 16")
        length = 16
    choice = input("Inclure caractères spéciaux ? (o/n) [o]: ").strip().lower() or "o"
    use_specials = (choice == "o")
    pwd = generate_password(length, use_specials)
    print("\nMot de passe généré :\n" + pwd)

if __name__ == "__main__":
    main()
