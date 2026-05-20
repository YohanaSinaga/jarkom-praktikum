import socket
import threading
import os
import struct
import sys

# ================= KONFIG =================
TCP_PORT = 5000
UDP_MCAST_PORT = 5001
UDP_BCAST_PORT = 5002
MCAST_GROUP = "224.0.0.1"
BUFFER_SIZE = 4096

print("\n=== CLIENT START ===")
server_ip = input("IP Server: ")
username = input("Username: ")

# ================= TCP =================
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect((server_ip, TCP_PORT))
tcp_socket.send((username + "\n").encode())

def receive_header(conn):
    data = b""
    while not data.endswith(b"\n"):
        chunk = conn.recv(1)
        if not chunk:
            return None
        data += chunk
    return data.decode().strip()

def tcp_receiver():
    while True:
        try:
            header = receive_header(tcp_socket)
            if not header:
                break

            if header.startswith("FILE"):
                _, fname, fsize = header.split("|")
                fsize = int(fsize)

                print(f"\n📥 File diterima: {fname}")

                data = b""
                while len(data) < fsize:
                    data += tcp_socket.recv(min(BUFFER_SIZE, fsize - len(data)))

                os.makedirs("client_files", exist_ok=True)
                with open(f"client_files/{fname}", "wb") as f:
                    f.write(data)

                print(f"✔ Disimpan: {fname}\n")

            else:
                print(header)

        except Exception as e:
            print("[TCP ERROR]", e)
            break

threading.Thread(target=tcp_receiver, daemon=True).start()

# ================= UDP =================
def udp_send(addr, label):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    if label == "BROADCAST":
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    msg = input("Pesan: ")
    sock.sendto(f"[{label}] {username}: {msg}".encode(), addr)
    sock.close()


def udp_send_file(addr, label):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    if label == "BROADCAST":
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    path = input("Path file: ")
    if not os.path.exists(path):
        print("File tidak ditemukan")
        return

    fname = os.path.basename(path)

    sock.sendto(f"FILE|{fname}".encode(), addr)

    with open(path, "rb") as f:
        while True:
            chunk = f.read(BUFFER_SIZE)
            if not chunk:
                break
            sock.sendto(chunk, addr)

    sock.sendto(b"[EOF]", addr)
    sock.close()
    print("✔ File terkirim")


def udp_receive(addr, label, mcast_ip=None):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", addr[1]))

    if mcast_ip:
        mreq = struct.pack("4sl", socket.inet_aton(mcast_ip), socket.INADDR_ANY)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    print(f"Listening {label}...")

    file_data = b""
    receiving = False
    filename = ""

    while True:
        data, _ = sock.recvfrom(BUFFER_SIZE)

        if data == b"[EOF]":
            with open(f"udp_{filename}", "wb") as f:
                f.write(file_data)
            print(f"✔ File diterima: {filename}")
            file_data = b""
            receiving = False

        elif data.startswith(b"FILE|"):
            filename = data.decode().split("|")[1]
            receiving = True
            print(f"📥 Menerima file {filename}")

        elif receiving:
            file_data += data

        else:
            print(data.decode(errors="ignore"))

# ================= UNICAST =================
def send_text_unicast():
    target = input("Ke user: ")

    print("\nJenis teks:")
    print("1. 1-5 kata")
    print("2. Kalimat panjang")
    print("3. Paragraf")

    pilihan = input("Pilih: ")

    if pilihan == "1":
        msg = input("Masukkan 1-5 kata: ")
    elif pilihan == "2":
        msg = input("Masukkan kalimat panjang: ")
    elif pilihan == "3":
        msg = input("Masukkan paragraf: ")
    else:
        print("Salah")
        return

    tcp_socket.sendall(f"MESSAGE|UNICAST|{target}|{msg}\n".encode())


def send_file_unicast():
    target = input("Ke user: ")

    print("\nJenis file:")
    print("1. Dokumen")
    print("2. Gambar")
    print("3. Audio")
    print("4. Video")

    input("Pilih: ")

    path = input("Path file: ")

    if not os.path.exists(path):
        print("File tidak ditemukan")
        return

    data = open(path, "rb").read()
    fname = os.path.basename(path)

    tcp_socket.sendall(f"FILE|UNICAST|{target}|{fname}|{len(data)}\n".encode())
    tcp_socket.sendall(data)

# ================= MULTICAST =================
def send_text_multicast():
    udp_send((MCAST_GROUP, UDP_MCAST_PORT), "MULTICAST")

def send_file_multicast():
    udp_send_file((MCAST_GROUP, UDP_MCAST_PORT), "MULTICAST")

# ================= BROADCAST =================
def send_text_broadcast():
    udp_send(("255.255.255.255", UDP_BCAST_PORT), "BROADCAST")

def send_file_broadcast():
    udp_send_file(("255.255.255.255", UDP_BCAST_PORT), "BROADCAST")

# ================= MENU =================
while True:
    print("\n" + "="*50)
    print("📡 SISTEM KOMUNIKASI")
    print("="*50)

    print("\n1. UNICAST (A -> B)")
    print("2. MULTICAST (A -> B,C)")
    print("3. BROADCAST (A -> semua)")
    print("0. Keluar")

    main = input("Pilih: ")

    # ===== UNICAST =====
    if main == "1":
        print("\n1. Single Thread")
        print("2. Multi Thread")
        input("Pilih mode (info saja): ")

        print("\n1. Kirim Teks")
        print("2. Kirim File")
        jenis = input("Pilih: ")

        if jenis == "1":
            send_text_unicast()
        elif jenis == "2":
            send_file_unicast()

    # ===== MULTICAST =====
    elif main == "2":
        print("\n1. Kirim Teks")
        print("2. Kirim File")
        print("3. Terima")

        pilihan = input("Pilih: ")

        if pilihan == "1":
            send_text_multicast()
        elif pilihan == "2":
            send_file_multicast()
        elif pilihan == "3":
            udp_receive((MCAST_GROUP, UDP_MCAST_PORT), "MULTICAST", MCAST_GROUP)

    # ===== BROADCAST =====
    elif main == "3":
        print("\n1. Kirim Teks")
        print("2. Kirim File")
        print("3. Terima")

        pilihan = input("Pilih: ")

        if pilihan == "1":
            send_text_broadcast()
        elif pilihan == "2":
            send_file_broadcast()
        elif pilihan == "3":
            udp_receive(("255.255.255.255", UDP_BCAST_PORT), "BROADCAST")

    elif main == "0":
        tcp_socket.close()
        print("Keluar...")
        sys.exit()

    else:
        print("Pilihan salah")