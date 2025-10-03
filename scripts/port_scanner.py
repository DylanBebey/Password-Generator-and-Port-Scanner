import socket

def scan_ports(target="127.0.0.1", ports=None, timeout=1.0):
    if ports is None:
        # ports courants utiles pour tests
        ports = [22, 80, 443, 3389, 8080]
    print(f"=== Scan des ports sur {target} ===")
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            try:
                res = sock.connect_ex((target, port))
                if res == 0:
                    print(f"[OUVERT] Port {port}")
                else:
                    print(f"[FERMÉ]   Port {port}")
            except Exception as e:
                print(f"[ERREUR] Port {port} -> {e}")

if __name__ == "__main__":
    target = input("IP ou domaine (par défaut 127.0.0.1): ").strip() or "127.0.0.1"
    scan_ports(target)
