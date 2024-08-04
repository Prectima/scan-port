import socket


def scanner_port(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)  # Définir un délai d'attente pour la connexion
        result = s.connect_ex((host, port))  # Tenter de se connecter au port
        return result == 0  # Retourne True si le port est ouvert


def scanner_ports(host, start_port, end_port):
    open_ports = []  # Liste pour stocker les ports ouverts
    for port in range(start_port, end_port + 1):
        if scanner_port(host, port):
            open_ports.append(port)  # Ajouter le port ouvert à la liste
            print(f"Port {port} est ouvert.")
        else:
            print(f"Port {port} est fermé.")

    return open_ports  # Retourner la liste des ports ouverts


def url_to_ip(url):
    try:
        return socket.gethostbyname(url)
    except socket.error as err:
        print(f"Erreur lors de la résolution de l'URL : {err}")
        return None


def main():
    url = input("Entrez l'adresse IP ou l'URL : ")
    host = url_to_ip(url) if not url.replace('.', '').isdigit() else url

    if host is None:
        return  # Si l'URL ne peut pas être résolue, arrêter l'exécution

    start_port = int(input("Entrez le port de début : "))
    end_port = int(input("Entrez le port de fin : "))

    print(f"Scanning ports from {start_port} to {end_port} on {host}...")
    open_ports = scanner_ports(host, start_port, end_port)

    if open_ports:
        print("\nRésumé des ports ouverts :")
        for port in open_ports:
            print(f"Port {port} est ouvert.")
    else:
        print("\nAucun port ouvert détecté.")


if __name__ == "__main__":
    main()
