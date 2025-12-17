# BB84 Kuantum Anahtar Dağıtım Protokolü (BB84) Simülasyonu

Bu depo, BB84 kuantum anahtar dağıtım (QKD) protokolünün **Python 3.11** kullanılarak simüle edilmiş hâlini içerir.
Çalışma; Ahmet (gönderici), Mehmet (alıcı) ve Arda (saldırgan) karakterleri üzerinden temel kuantum kriptografi prensiplerini modellemektedir.

Simülasyonun amacı, kuantum ölçümünün bozucu doğasını, baz eşleşmesi mekanizmasını ve araya giren bir saldırgan durumunda kuantum bit hata oranının (QBER) nasıl yükseldiğini açık biçimde göstermektir.

---

## 📌 Projenin Amacı

Bu simülasyonun temel amacı, BB84 protokolünün pratik işleyişini aşağıdaki adımlar üzerinden görünür hâle getirmektir:

- Rastgele bit ve baz seçimi  
- Qubitlerin Z ve X bazlarında hazırlanması  
- Kuantum kanalında iletim ve ölçüm süreci  
- Araya giren saldırgan (Intercept–Resend) senaryosu  
- QBER (Quantum Bit Error Rate) hesaplaması

Bu çalışma, kuantum kriptografi ve kuantum bilişim alanına giriş yapmak isteyen öğrenciler ve araştırmacılar için eğitsel bir örnek sunmayı hedeflemektedir.

---

## 📁 Proje Yapısı

```text
BB84-Protocol-Simulation/
│
├── sim.py              # BB84 protokolü simülasyon kodu
├── requirements.txt    # Gerekli Python paketleri
└── README.md           # Bu belge
```

---

## ⚙️ Gereksinimler

Bu projeyi çalıştırabilmek için sisteminizde aşağıdaki yazılımların kurulu olması gerekmektedir:

- **Python 3.11**  
- **pip** (Python paket yöneticisi)

> Not: Proje ve kullanılan kütüphaneler Python 3.11 üzerinde test edilmiştir.

---

## 🛠️ Kurulum

Kurulum işlemleri `pip` ve `requirements.txt` dosyası üzerinden gerçekleştirilmektedir.

### 1) Depoyu Klonlayın

```bash
git clone https://github.com/tarkoncel/BB84-Protocol-Simulation.git
cd BB84-Protocol-Simulation
```

---

### 2) Sanal Ortam Oluşturun (Önerilir)

#### Linux / macOS / BSD

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows (PowerShell)

```powershell
python3 -m venv venv
venv\Scripts\activate
```

---

### 3) Gerekli Paketleri Kurun

```bash
pip install -r requirements.txt
```

---

## ▶️ Simülasyonu Çalıştırma

Simülasyonu başlatmak için aşağıdaki komutu kullanın:

```bash
python3.11 sim.py
```

Simülasyon sonunda terminalde şu çıktılar üretilir:

- Ahmet ve Mehmet için sifted key dizileri  
- Sifted key uzunluğu  
- QBER değeri  
- Saldırının tespit edilip edilmediği bilgisi

---

## 🧪 Simüle Edilen Senaryolar

### 1) Saldırı Yok

- Gönderici ve alıcı rastgele bazlar kullanır.
- Baz eşleşmesi olan bitler sifted key’i oluşturur.
- QBER ≈ 0 olarak gözlemlenir.

### 2) Araya Giren Saldırgan (Intercept–Resend)

- Arda qubitleri rastgele bazlarda ölçüp yeniden gönderir.
- Ölçüm, kuantum durumları bozduğu için hata oranı artar.
- QBER ≈ %30–%40 aralığına yükselir.
- Bu durum saldırının sistem tarafından tespit edildiğini gösterir.

---

## 📊 QBER Hesabı

```text
QBER = Hatalı Bit Sayısı / Toplam Sifted Bit Sayısı
```

- Saldırgan yokken → QBER ≈ 0  
- Saldırgan varken → QBER ≥ %20

---

## 🧭 Teorik Temeller

Simülasyon aşağıdaki kuantum fiziği prensiplerine dayanmaktadır:

- **Heisenberg Belirsizlik İlkesi:** Yanlış bazda yapılan ölçüm qubitin durumunu bozar.  
- **No-Cloning Teoremi:** Bir qubit birebir kopyalanamaz.  
- **Kuantum Ölçümünün Bozuculuğu:** Ölçüm işlemi kuantum durumunu geri döndürülemez biçimde değiştirir.

Bu nedenle saldırganın her müdahalesi ölçüm istatistiklerine yansır.

---
## License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

Copyright (C) 2025 Tarık Öncel

You may redistribute and/or modify this project under the terms of the GPL-3.0.
See the `LICENSE` file for details.


## 📘 Kaynakça

- Bennett, C. H., & Brassard, G. (1984). *Quantum cryptography: Public key distribution and coin tossing.*  
- Nielsen, M. A., & Chuang, I. L. (2010). *Quantum Computation and Quantum Information.*  
- IBM Qiskit Documentation: https://qiskit.org/
