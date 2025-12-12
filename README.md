# BB84 Kuantum Anahtar Dağıtım Protokolü Simülasyonu

Bu depo, BB84 kuantum anahtar dağıtım (QKD) protokolünün Python
kullanılarak simüle edilmiş hâlini içerir.\
Çalışma, Ahmet (gönderici), Mehmet (alıcı) ve Arda (saldırgan)
karakterleri üzerinden temel kuantum kriptografi prensiplerini
modellemektedir.

Simülasyon, kuantum ölçümünün bozucu doğasını, baz eşleşmesi
mekanizmasını ve saldırı durumunda hata oranının (QBER) nasıl arttığını
göstermeyi amaçlar.

------------------------------------------------------------------------

## 📌 Projenin Amacı

Bu simülasyonun amacı, BB84 protokolünün pratik olarak nasıl
çalıştığını;\
- **Rastgele bit ve baz seçimi**,\
- **Qubit hazırlama**,\
- **Ölçüm süreci**,\
- **Arda'nın müdahale ettiği saldırı senaryosu**,\
- **QBER hesaplaması**,\
gibi adımlar üzerinden görünür hâle getirmektir.

Bu çalışma özellikle kuantum kriptografi, kuantum bilişim ve siber
güvenlik alanlarına başlangıç yapmak isteyen araştırmacılar ve
öğrenciler için örnek bir temel oluşturur.

------------------------------------------------------------------------

## 📁 Proje Yapısı

    BB84-Protocol-Simulation/
    │
    ├── sim.py                # Simülasyon kodu (en güncel)
    ├── README.md             # Bu belge
    └── (isteğe bağlı ek dosyalar)

------------------------------------------------------------------------

## 🧪 Simülasyonun İçeriği

Simülasyon iki temel senaryo içerir:

### 1) **Saldırı Yok**

-   Ahmet ve Mehmet rastgele bazlarla çalışır.
-   Baz eşleşmesi olduğunda sifted key oluşur.
-   QBER ≈ 0 çıkar.

### 2) **Arda Saldırıyor**

-   Arda qubitleri rastgele bazda ölçüp yeniden yollar.
-   Heisenberg Belirsizlik İlkesi ve No-Cloning Teoremi gereği qubitler
    bozulur.
-   QBER ≈ %30--%40 civarında artar.
-   Bu, saldırının başarılı şekilde tespit edildiğini gösterir.

------------------------------------------------------------------------
# 🔧 1. GEREKSİNİMLER

- Python **3.10 – 3.11** *(Qiskit ile en uyumlu sürüm aralığı)*
- pip paket yöneticisi
- Git (opsiyonel, repo klonlamak için)

---

# 🐧 2. Kurulum — **Linux (Fedora, Ubuntu, Arch, Debian vb.)**

### 1) Python sürümünü kontrol et
```bash
python3 --version
python3 -m venv bb84
source bb84/bin/activate
pip install --upgrade pip
pip install requipments.txt


## ▶️ Simülasyonu Çalıştırma

Depoyu indirdikten sonra:

``` bash
python3 sim.py
```

Simülasyon çıktısı şu bölümlerden oluşur:

-   **Ahmet'in sifted key'i**
-   **Mehmet'in sifted key'i**
-   **Sifted key uzunluğu**
-   **QBER değeri**
-   **Arda'nın saldırılı ve saldırısız durum sonuçları**

------------------------------------------------------------------------

## ⚙️ Kullanılan Yöntemler ve Fonksiyonlar

### `random_bits(n)`

Rastgele bit dizisi oluşturur.

### `random_bases(n)`

Gönderici ve alıcı için rastgele bazlar üretir.\
- 0 → Z bazı\
- 1 → X bazı

### `measure_qubit(bit, basis, measurement_basis)`

Mehmet'in qubitleri nasıl ölçtüğünü simüle eder.

### `eavesdrop_qubit(bit, basis)`

Arda'nın qubitleri bozarak yeniden üretmesini simüle eder.

### `bb84_protocol(n, attack=True/False)`

Tam BB84 akışını simüle eder.

------------------------------------------------------------------------

## 📊 Beklenen Sonuçlar

  -----------------------------------------------------------------------
  Senaryo                 QBER              Açıklama
  ----------------------- ----------------- -----------------------------
  **Saldırı Yok**         ≈ 0.0             Sistem güvenli, bozunum yok

  **Arda Saldırıyor**     ≈ 0.30--0.40      Saldırgan ölçümü bozuyor,
                                            saldırı tespit ediliyor
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 🧭 Teorik Temeller

Simülasyon şu kuantum prensiplerine dayanır:

-   **Heisenberg Belirsizlik İlkesi:** Yanlış bazda ölçülen qubit
    bozulur.\
-   **No-Cloning Teoremi:** Qubit birebir kopyalanamaz.\
-   **Kuantum Ölçümünün Bozuculuğu:** Her ölçüm qubitin durumunu
    değiştirir.

Bu nedenle Arda'nın saldırısı doğrudan sifted key istatistiklerine
yansır.

------------------------------------------------------------------------

## 📘 Kaynakça

-   Nielsen, M., & Chuang, I. *Quantum Computation and Quantum
    Information*.\
-   Bernhardt, C. *Herkes İçin Kuantum Bilgisayım*. TÜBİTAK Popüler
    Bilim Yayınları.\
-   IBM Qiskit Documentation: https://qiskit.org/

------------------------------------------------------------------------

## ✨ Katkı Sunmak

Her türlü katkı, öneri veya geliştirme isteği için pull request
gönderebilirsiniz.
