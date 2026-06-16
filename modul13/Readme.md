# Laporan Praktikum Jaringan Komputer - Modul 13

## Analisis Ethernet dan Address Resolution Protocol (ARP) Menggunakan Wireshark

### Identitas Praktikan

| Item      | Keterangan |
| --------- | ---------- |
| **Nama**  | Yohana Sinaga |
| **NIM**   | 103072400009 |
| **Kelas** | IF 04-01 |

---

# Pendahuluan

Ethernet merupakan teknologi jaringan yang bekerja pada layer Data Link dalam model OSI. Ethernet bertugas mengirimkan data dalam bentuk frame antar perangkat yang terhubung dalam jaringan lokal (LAN).

Selain Ethernet, terdapat Address Resolution Protocol (ARP) yang berfungsi untuk menerjemahkan alamat IP menjadi MAC Address. Protokol ini memungkinkan perangkat dalam jaringan lokal mengetahui alamat fisik perangkat tujuan sebelum proses komunikasi dilakukan.

Pada praktikum ini dilakukan pengamatan terhadap frame Ethernet dan proses ARP menggunakan aplikasi Wireshark. Selain itu dilakukan pemeriksaan ARP Cache menggunakan Command Prompt untuk melihat hubungan antara alamat IP dan MAC Address yang tersimpan pada komputer.

---

# Tujuan Praktikum

1. Memahami konsep dasar Ethernet.
2. Memahami fungsi dan cara kerja ARP.
3. Menggunakan Wireshark untuk menangkap dan menganalisis frame Ethernet.
4. Mengamati isi ARP Cache pada komputer.
5. Menganalisis proses ARP yang terjadi dalam jaringan.

---

# Tools yang Digunakan

| Tools                  | Fungsi                                        |
| ---------------------- | --------------------------------------------- |
| Wireshark              | Melakukan capture dan analisis paket jaringan |
| Command Prompt         | Menjalankan perintah ARP                      |
| Sistem Operasi Windows | Lingkungan praktikum                          |

---

# Langkah-Langkah Praktikum

## 1. Menangkap dan Menganalisis Frame Ethernet

Langkah pertama dilakukan dengan membuka aplikasi Wireshark dan memilih interface jaringan yang aktif. Setelah proses capture berjalan, dilakukan aktivitas jaringan sehingga Wireshark dapat menangkap frame Ethernet yang melewati interface tersebut.

Selanjutnya salah satu frame Ethernet dipilih untuk dianalisis. Pada bagian detail paket dapat dilihat informasi seperti Source MAC Address, Destination MAC Address, dan EtherType yang menunjukkan jenis protokol yang dibawa oleh frame tersebut.

**URL yang diakses:**
```
http://gaia.cs.umass.edu/wireshark-labs/HTTP-ethereal-lab-file3.html
```

### Screenshot Hasil Analisis Frame Ethernet

![Gambar 1. Hasil URL dan menjalankan di wireshark](<assets/gambar1.png>)
> *Gambar 1. Hasil akses URL Bill of Rights dan capture di Wireshark.*

![Gambar 2. Hasil analisis frame Ethernet pada Wireshark](<assets/gambar2.png>)
> *Gambar 2. Analisis Frame 1107 - HTTP GET Request*

**Detail Frame 1107 yang dianalisis:**

- **Frame Number:** 1107
- **Time:** 8.036029500 detik
- **Source IP:** 192.168.1.210
- **Destination IP:** 128.119.245.12 (gaia.cs.umass.edu)
- **Protocol:** HTTP
- **Length:** 550 bytes
- **Info:** GET /wireshark-labs/HTTP-ethereal-lab-file3.html HTTP/1.1

**Ethernet Frame Details:**
- **Destination MAC:** zte_a6:b2:03 (6c:11:ba:a6:b2:03)
  - LG bit: Globally unique address (factory default)
  - IG bit: Individual address (unicast)
  
- **Source MAC:** LiteonTechno_2f:b9:2f (c0:35:32:2f:b9:2f)
  - LG bit: Globally unique address (factory default)
  - IG bit: Individual address (unicast)

- **Type:** IPv4 (0x0800)

**Internet Protocol Version 4:**
- Source: 192.168.1.210
- Destination: 128.119.245.12

**Transmission Control Protocol:**
- Source Port: 60935
- Destination Port: 80
- Seq: 1, Ack: 1, Len: 496

**Hypertext Transfer Protocol:**
- GET /wireshark-labs/HTTP-ethereal-lab-file3.html HTTP/1.1

---

## 2. Melihat Isi ARP Cache

Untuk melihat daftar alamat IP dan MAC Address yang tersimpan pada komputer, dibuka Command Prompt kemudian menjalankan perintah berikut:

```bash
arp -a
```

Perintah tersebut digunakan untuk menampilkan ARP Cache yang berisi hasil pemetaan alamat IP dengan MAC Address yang telah diketahui oleh komputer.

### Screenshot Hasil Perintah ARP

![Gambar 3. Hasil perintah arp -a pada Command Prompt](<assets/gambar3.png>)
> *Gambar 3. ARP Cache pada Command Prompt*

**Hasil ARP Cache Analysis:**

**Interface: 169.254.97.1 --- 0xb**
- Berisi entri-entri multicast dan broadcast addresses

**Interface: 192.168.1.210 --- 0x11** (Interface aktif yang digunakan)

| Internet Address | Physical Address | Type |
|------------------|------------------|------|
| 192.168.1.1 | 6c-11-ba-a6-b2-03 | dynamic |
| 192.168.1.255 | ff-ff-ff-ff-ff-ff | static |
| 224.0.0.2 | 01-00-5e-00-00-02 | static |
| 224.0.0.22 | 01-00-5e-00-00-16 | static |
| 224.0.0.251 | 01-00-5e-00-00-fb | static |
| 224.0.0.252 | 01-00-5e-00-00-fc | static |
| 239.255.255.250 | 01-00-5e-7f-ff-fa | static |
| 255.255.255.255 | ff-ff-ff-ff-ff-ff | static |

**Catatan Penting:** 
- Alamat **192.168.1.1** adalah gateway/router dengan MAC Address **6c-11-ba-a6-b2-03**
- MAC Address ini sama dengan destination MAC pada Frame 1107 (zte_a6:b2:03)
- Ini menunjukkan bahwa paket HTTP dikirim melalui gateway/router

---

## 3. Mengamati Paket ARP Menggunakan Wireshark

Setelah melihat ARP Cache, dilakukan pengamatan terhadap paket ARP yang tertangkap pada Wireshark.

Pada hasil capture dapat diamati proses ARP Request dan ARP Reply yang digunakan perangkat untuk mencari MAC Address dari suatu alamat IP dalam jaringan lokal.

### Screenshot Capture Paket ARP

![Gambar 4. Hasil capture paket ARP pada Wireshark](<assets/gambar4.png>)
> *Gambar 4. Analisis Frame 395 - ARP Request*

**Detail Frame 395 yang dianalisis:**

- **Frame Number:** 395
- **Time:** 5.215009600 detik
- **Source:** EzvizSoftwar_4b:55:b8
- **Destination:** Broadcast
- **Protocol:** ARP
- **Length:** 60 bytes

**Ethernet Frame Details:**
- **Destination:** Broadcast (ff:ff:ff:ff:ff:ff)
  - LG bit: 1
  - IG bit: 1
  
- **Source:** EzvizSoftwar_4b:55:b8 (ac:1c:26:4b:55:b8)
  - LG bit: 0 (Globally unique address)
  - IG bit: 0 (Individual address - unicast)

- **Type:** ARP (0x0806)

**Address Resolution Protocol (request):**
- Opcode: request (1)
- Padding: 0000000000000000000000000000

---

# Hasil dan Analisis

## 1. Analisis Frame Ethernet

Berdasarkan hasil pengamatan pada Wireshark, frame Ethernet memiliki beberapa informasi penting:

### Frame 1107 - HTTP GET Request

**Destination MAC Address:** 6c:11:ba:a6:b2:03 (zte_a6:b2:03)
- Ini adalah MAC Address gateway/router (192.168.1.1)
- Karena tujuan (128.119.245.12) berada di luar jaringan lokal, maka frame dikirim ke gateway

**Source MAC Address:** c0:35:32:2f:b9:2f (LiteonTechno_2f:b9:2f)
- Ini adalah MAC Address komputer lokal (192.168.1.210)
- Adapter jaringan: Liteon Technology

**EtherType:** 0x0800 (IPv4)
- Menunjukkan bahwa frame ini membawa protokol IPv4

**Analisis:**
Frame Ethernet merupakan unit data utama pada layer Data Link yang digunakan untuk mengirimkan informasi antar perangkat dalam jaringan lokal. Pada kasus ini, meskipun tujuan akhir adalah server gaia.cs.umass.edu (128.119.245.12) yang berada di internet, frame Ethernet hanya sampai ke gateway lokal karena routing akan menangani pengiriman ke jaringan luar.

### Struktur Frame Ethernet yang Teramati:

1. **Preamble & SFD** (tidak terlihat di Wireshark - dihandle hardware)
2. **Destination Address:** 6 bytes (6c:11:ba:a6:b2:03)
3. **Source Address:** 6 bytes (c0:35:32:2f:b9:2f)
4. **Type/Length:** 2 bytes (0x0800 untuk IPv4)
5. **Payload:** 46-1500 bytes (berisi IP packet)
6. **Frame Check Sequence:** 4 bytes (tidak ditampilkan)

---

## 2. Analisis ARP Cache

Hasil perintah `arp -a` menunjukkan daftar pasangan alamat IP dan MAC Address yang tersimpan pada komputer.

### ARP Cache Interface 192.168.1.210:

**Entri Dynamic:**
- **192.168.1.1** → **6c-11-ba-a6-b2-03** (dynamic)
  - Ini adalah default gateway
  - Tipe "dynamic" berarti entri ini dipelajari secara otomatis melalui ARP
  - Akan expired setelah beberapa waktu jika tidak digunakan

**Entri Static (Multicast & Broadcast):**
- **192.168.1.255** → **ff-ff-ff-ff-ff-ff** (broadcast)
- **224.0.0.2** → **01-00-5e-00-00-02** (multicast)
- **224.0.0.22** → **01-00-5e-00-00-16** (IGMP multicast)
- **224.0.0.251** → **01-00-5e-00-00-fb** (mDNS multicast)
- **224.0.0.252** → **01-00-5e-00-00-fc** (LLMNR multicast)
- **239.255.255.250** → **01-00-5e-7f-ff-fa** (SSDP multicast)
- **255.255.255.255** → **ff-ff-ff-ff-ff-ff** (limited broadcast)

**Fungsi ARP Cache:**
ARP Cache berfungsi sebagai penyimpanan sementara hasil proses ARP sehingga komputer tidak perlu terus-menerus mengirim ARP Request untuk perangkat yang sama. Dengan adanya cache ini, proses komunikasi menjadi lebih cepat dan efisien.

**Korelasi dengan Frame 1107:**
MAC Address **6c-11-ba-a6-b2-03** yang terlihat di ARP Cache untuk IP 192.168.1.1 sama persis dengan Destination MAC Address pada Frame 1107. Ini membuktikan bahwa:
1. Komputer telah melakukan ARP request untuk mencari MAC address gateway
2. Hasilnya disimpan di ARP cache
3. Saat mengirim HTTP request ke internet, frame dikirim ke gateway menggunakan MAC address tersebut

---

## 3. Analisis Paket ARP

Dari hasil capture Wireshark terlihat bahwa ARP bekerja melalui dua jenis pesan utama:

### Frame 395 - ARP Request

**Karakteristik ARP Request:**

1. **Destination MAC:** ff:ff:ff:ff:ff:ff (Broadcast)
   - ARP request dikirim secara broadcast ke seluruh perangkat di jaringan lokal
   - Semua perangkat akan menerima paket ini

2. **Source MAC:** ac:1c:26:4b:55:b8 (EzvizSoftwar_4b:55:b8)
   - Perangkat yang melakukan query ARP
   - Kemungkinan perangkat IoT (Ezviz adalah brand kamera keamanan)

3. **EtherType:** 0x0806 (ARP)
   - Menunjukkan frame ini membawa protokol ARP

4. **ARP Opcode:** request (1)
   - Menunjukkan ini adalah ARP request
   - Bertanya "Who has this IP address?"

**Proses ARP Request:**
- Perangkat dengan MAC ac:1c:26:4b:55:b8 ingin mengetahui MAC address dari suatu IP
- Karena tidak ada di cache, dikirim broadcast ARP request
- Semua perangkat di jaringan lokal menerima request ini
- Hanya perangkat yang memiliki IP yang dicari yang akan merespon

### ARP Reply (tidak terlihat di screenshot, tapi terjadi setelah request):

**Karakteristik ARP Reply:**
- Dikirim secara unicast ke peminta
- Berisi informasi MAC address yang diminta
- Opcode: reply (2)
- Setelah menerima reply, peminta menyimpan di ARP cache

### Timeline Proses ARP:

```
1. Perangkat A ingin kirim data ke IP 192.168.1.X
2. Cek ARP Cache → tidak ada entri
3. Kirim ARP Request (broadcast)
   - "Who has 192.168.1.X? Tell 192.168.1.210"
4. Semua perangkat terima broadcast
5. Perangkat dengan IP 192.168.1.X kirim ARP Reply (unicast)
   - "192.168.1.X is at MAC xx:xx:xx:xx:xx:xx"
6. Perangkat A terima reply dan simpan di ARP cache
7. Sekarang bisa kirim data menggunakan MAC address tersebut
```

### Analisis Tambahan dari Wireshark:

Dari gambar terlihat beberapa ARP packets dari berbagai devices:
- **EzvizSoftwar_41:e7:** Perangkat Ezviz lain
- **EzvizSoftwar_4e:4c:** Perangkat Ezviz lain
- **Intel_ca:a1:ed:** Perangkat dengan adapter Intel

Ini menunjukkan jaringan lokal memiliki beberapa perangkat yang aktif melakukan ARP untuk maintain koneksi mereka.

---

# Kesimpulan

Berdasarkan praktikum yang telah dilakukan, dapat disimpulkan bahwa:

## 1. Ethernet Frame Analysis

**Ethernet** merupakan protokol pada layer Data Link (Layer 2 OSI) yang digunakan untuk mengirimkan data dalam bentuk frame antar perangkat pada jaringan lokal. Setiap frame Ethernet terdiri dari:
- Destination MAC Address (6 bytes)
- Source MAC Address (6 bytes)
- EtherType (2 bytes) - menunjukkan protokol layer network yang dibawa
- Payload (46-1500 bytes)
- Frame Check Sequence (4 bytes)

Pada Frame 1107, terlihat bahwa untuk komunikasi ke luar jaringan lokal, frame Ethernet dikirim ke gateway/router (MAC: 6c:11:ba:a6:b2:03) bukan langsung ke tujuan akhir.

## 2. ARP Protocol Analysis

**ARP (Address Resolution Protocol)** berfungsi untuk menerjemahkan alamat IP (Layer 3) menjadi MAC Address (Layer 2) sehingga perangkat dapat mengetahui alamat fisik tujuan sebelum mengirimkan data.

**Mekanisme ARP:**
- **ARP Request:** Dikirim secara broadcast (ff:ff:ff:ff:ff:ff) untuk mencari MAC address dari suatu IP
- **ARP Reply:** Dikirim secara unicast sebagai jawaban dari ARP request
- **ARP Cache:** Menyimpan hasil mapping IP-MAC untuk efisiensi

**Dari praktikum terlihat:**
- ARP Cache menunjukkan mapping 192.168.1.1 → 6c-11-ba-a6-b2-03
- MAC address ini sama dengan destination MAC pada HTTP request
- Ini membuktikan ARP digunakan sebelum pengiriman data

## 3. Wireshark Analysis

Dengan menggunakan **Wireshark**, proses pengiriman frame Ethernet dan pertukaran pesan ARP dapat diamati secara detail:
- Dapat melihat struktur lengkap Ethernet frame
- Dapat menganalisis MAC addresses (source dan destination)
- Dapat melihat proses ARP request/reply secara real-time
- Dapat memverifikasi isi ARP cache dengan traffic yang tertangkap

## 4. Hubungan Ethernet dan ARP

**Integrasi Ethernet dan ARP:**
1. Sebelum mengirim frame Ethernet, perangkat perlu tahu MAC address tujuan
2. Jika hanya tahu IP address, perangkat menggunakan ARP untuk mencari MAC address
3. Hasil ARP disimpan di cache untuk penggunaan selanjutnya
4. Frame Ethernet kemudian dikirim dengan MAC address yang telah diketahui

Praktikum ini membantu memahami bagaimana komunikasi pada layer Data Link berlangsung dan bagaimana ARP mendukung proses komunikasi dalam jaringan komputer dengan menjembatani antara alamat IP (logical) dan alamat MAC (physical).

---

# Referensi

1. Wireshark Lab: Ethernet and ARP, University of Massachusetts Amherst
2. RFC 826 - An Ethernet Address Resolution Protocol
3. IEEE 802.3 - Ethernet Standard

---
