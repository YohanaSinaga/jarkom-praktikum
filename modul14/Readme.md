# Laporan Praktikum Jaringan Komputer - Modul 14

## Analisis Jaringan WiFi Menggunakan Wireshark

### Identitas Praktikan

| Item      | Keterangan |
| --------- | ---------- |
| **Nama**  |      Yohana Sinaga      |
| **NIM**   |        103072400009   |
| **Kelas** |           IF 04-01 |

---

# Pendahuluan

WiFi atau IEEE 802.11 merupakan teknologi jaringan nirkabel yang memungkinkan perangkat saling berkomunikasi tanpa menggunakan media kabel. Dalam jaringan WiFi, komunikasi dilakukan menggunakan frame 802.11 yang berisi informasi mengenai manajemen jaringan, proses koneksi, serta pertukaran data antar perangkat.

Pada praktikum ini dilakukan analisis terhadap frame 802.11 menggunakan aplikasi Wireshark. Analisis difokuskan pada Beacon Frame dan proses komunikasi data yang terjadi pada jaringan WiFi.

---

# Tujuan Praktikum

1. Memahami konsep dasar jaringan WiFi (IEEE 802.11).
2. Menggunakan Wireshark untuk menganalisis frame WiFi.
3. Mengamati Beacon Frame yang dikirim oleh Access Point.
4. Menganalisis proses transfer data pada jaringan WiFi.
5. Memahami komunikasi yang terjadi antara client dan Access Point.

---

# Tools yang Digunakan

| Tools                  | Fungsi                                        |
| ---------------------- | --------------------------------------------- |
| Wireshark              | Melakukan capture dan analisis paket jaringan |
| File Capture WiFi      | Data hasil praktikum                          |
| Sistem Operasi Windows | Lingkungan praktikum                          |

---

# Langkah-Langkah Praktikum

## 14.2. Mengunduh File Capture

Unduh file:

```text
wireshark-traces.zip
```

Kemudian ekstrak file tersebut hingga diperoleh file:

```text
Wireshark_802_11.pcap
```

File ini digunakan sebagai bahan analisis pada praktikum.

---

## Membuka File Capture di Wireshark

1. Jalankan aplikasi Wireshark.
2. Klik **File → Open**.
3. Pilih file:

```text
Wireshark_802_11.pcap
```

4. Klik **Open**.

Setelah file terbuka akan terlihat daftar paket yang berhasil ditangkap dari jaringan WiFi.

### Screenshot Beacon Frame

![alt text](<assets/gambar1.png>)

> *Gambar 1. Hasil membuka file capture di wireshark*
---

## 14.3 Mengamati Beacon Frame
Beacon Frame digunakan oleh Access Point untuk mengumumkan keberadaan jaringan WiFi kepada perangkat di sekitarnya.

Langkah-langkah:

1. Cari paket bertipe **Beacon** pada daftar paket.
2. Klik salah satu paket Beacon.
3. Perhatikan bagian **IEEE 802.11** pada panel detail paket.
4. Amati informasi seperti:

   * SSID
   * Channel
   * Supported Rates
   * Capability Information

### Screenshot Beacon Frame

![alt text](<assets/gambar2.png>)

> *Gambar 2. Hasil analisis komunikasi data pada jaringan WiFi.*

---


## 14.4 Transfer Data pada Jaringan WiFi
Transfer data terjadi setelah perangkat berhasil terhubung ke Access Point.

Data Frame digunakan untuk membawa berbagai informasi seperti:

* Permintaan halaman web.
* Pengiriman file.
* Komunikasi aplikasi.
* Akses internet.

Melalui transfer data, perangkat dapat berkomunikasi dan bertukar informasi dengan perangkat lain maupun server di internet.


Pada file capture terdapat aktivitas akses website yang dilakukan oleh host yang telah terhubung ke Access Point.

Langkah-langkah:

1. Cari paket data yang berkaitan dengan komunikasi host.
2. Perhatikan alamat sumber dan tujuan paket.
3. Analisis proses pertukaran data yang terjadi melalui jaringan WiFi.
4. Identifikasi bagaimana data dikirim dari client menuju Access Point dan diteruskan ke tujuan.

Transfer data menunjukkan fungsi utama jaringan WiFi sebagai media pertukaran informasi.

Setelah perangkat berhasil terhubung ke Access Point, proses pertukaran data dapat dilakukan melalui Data Frame.

Data Frame digunakan untuk mengirimkan berbagai jenis informasi seperti permintaan web, pengiriman file, maupun komunikasi aplikasi lainnya. Pada jaringan WiFi, data yang dikirim oleh client akan diteruskan melalui Access Point menuju tujuan yang diinginkan.

Proses transfer data memungkinkan pengguna mengakses layanan jaringan seperti browsing internet, mengirim email, dan bertukar informasi dengan perangkat lain.

---

## 14.5 Association pada Jaringan WiFi

Association merupakan proses yang memungkinkan sebuah perangkat bergabung ke dalam jaringan WiFi.

Tahapan Association terdiri dari:

### Association Request

Association Request dikirim oleh client kepada Access Point sebagai permintaan untuk bergabung ke jaringan WiFi.

Frame ini berisi informasi kemampuan perangkat yang akan digunakan selama komunikasi.

### Association Response

Association Response merupakan balasan dari Access Point terhadap permintaan yang dikirim oleh client.

Jika permintaan diterima, Access Point akan mengizinkan perangkat bergabung ke jaringan sehingga komunikasi data dapat dilakukan.

Melalui proses Association, perangkat dan Access Point dapat saling mengenali serta membangun koneksi yang diperlukan untuk pertukaran data.


Association merupakan proses yang memungkinkan perangkat bergabung ke jaringan WiFi.

Langkah-langkah:

1. Cari frame **Association Request**.
2. Perhatikan informasi yang dikirim client kepada Access Point.
3. Cari frame **Association Response**.
4. Perhatikan balasan yang diberikan Access Point.
5. Analisis proses koneksi yang terjadi antara client dan Access Point.

Association harus berhasil dilakukan sebelum perangkat dapat bertukar data melalui jaringan WiFi.


---

# Kesimpulan


Berdasarkan praktikum yang telah dilakukan, dapat disimpulkan bahwa jaringan WiFi menggunakan standar IEEE 802.11 untuk melakukan komunikasi nirkabel antar perangkat.

Beacon Frame berfungsi untuk mengumumkan keberadaan Access Point dan memberikan informasi mengenai jaringan WiFi yang tersedia. Setelah perangkat menemukan jaringan yang diinginkan, proses Association dilakukan agar perangkat dapat bergabung ke jaringan tersebut.

Setelah proses Association berhasil, perangkat dapat melakukan transfer data melalui Data Frame untuk mengakses layanan jaringan dan bertukar informasi dengan perangkat lain.

Melalui penggunaan Wireshark, cara kerja jaringan WiFi dapat diamati secara lebih jelas sehingga membantu memahami proses komunikasi yang terjadi pada jaringan nirkabel.

---