from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np

def bb84_qiskit(n=1000, attack=False):
    backend = AerSimulator()

    # 1) Ahmet rastgele bit ve baz seçimi
    ahmet_bits = np.random.randint(0, 2, n)
    ahmet_bases = np.random.randint(0, 2, n)
    mehmet_bases = np.random.randint(0, 2, n)

    if attack:
        arda_bases = np.random.randint(0, 2, n)
    else:
        arda_bases = None

    # ---- AHMED QUBIT HAZIRLAMA DEVRESİ ----
    qc = QuantumCircuit(n, n)

    for i in range(n):
        if ahmet_bits[i] == 1:
            qc.x(i)
        if ahmet_bases[i] == 1:  # X bazı
            qc.h(i)

    # ---- ARDA SALDIRI MODU ----
    if attack:
        for i in range(n):
            if arda_bases[i] == 1:
                qc.h(i)

            qc.measure(i, i)
            qc.reset(i)

            if arda_bases[i] == 1:
                qc.h(i)
            if ahmet_bits[i] == 1:
                qc.x(i)

    # ---- MEHMET ÖLÇÜM MODU ----
    for i in range(n):
        if mehmet_bases[i] == 1:
            qc.h(i)
        qc.measure(i, i)

    # ---- DEVRE ÇALIŞTIRMA ----
    job = backend.run(qc, shots=1)
    result = job.result().get_counts()

    measured = list(result.keys())[0]     # Qiskit sonucu string döndürür
    measured = measured[::-1]             # Bit sırası ters gelir → düzelt
    mehmet_bits = np.array([int(b) for b in measured])

    # ---- SİFTED KEY ----
    sift_mask = (ahmet_bases == mehmet_bases)

    sift_a = ahmet_bits[sift_mask]
    sift_m = mehmet_bits[sift_mask]

    if len(sift_a) > 0:
        qber = np.mean(sift_a != sift_m)
    else:
        qber = None

    return sift_a, sift_m, qber


if __name__ == "__main__":
    print("---- SALDIRI YOK ----")
    a, m, q = bb84_qiskit(n=1000, attack=False)
    print("Sifted Key Length:", len(a))
    print("QBER:", q)

    print("\n---- ARDA SALDIRIYOR ----")
    a2, m2, q2 = bb84_qiskit(n=1000, attack=True)
    print("Sifted Key Length:", len(a2))
    print("QBER:", q2)

