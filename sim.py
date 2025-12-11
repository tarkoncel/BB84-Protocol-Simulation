import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def generate_random_bits(n):
    return np.random.randint(2, size=n)

def generate_random_bases(n):
    return np.random.randint(2, size=n)  # 0 = Z, 1 = X

def prepare_qubit(bit, basis):
    qc = QuantumCircuit(1, 1)
    if bit == 1:
        qc.x(0)
    if basis == 1:
        qc.h(0)
    return qc

def measure_qubit(qc, basis):
    if basis == 1:
        qc.h(0)
    qc.measure(0, 0)
    simulator = AerSimulator()
    result = simulator.run(qc).result()
    counts = result.get_counts()
    measured_bit = int(max(counts, key=counts.get))
    return measured_bit

def bb84_protocol(n=20, attack=False):
    ahmet_bits = generate_random_bits(n)
    ahmet_bases = generate_random_bases(n)
    mehmet_bases = generate_random_bases(n)

    raw_key_ahmet = []
    raw_key_mehmet = []

    for i in range(n):
        bit = ahmet_bits[i]
        basis = ahmet_bases[i]

        qc = prepare_qubit(bit, basis)

        if attack:
            arda_basis = np.random.randint(2)
            measure_qubit(qc, arda_basis)

        mbit = measure_qubit(qc, mehmet_bases[i])

        raw_key_ahmet.append(bit)
        raw_key_mehmet.append(mbit)

    sift_ahmet = []
    sift_mehmet = []

    for a, b, bit_a, bit_m in zip(ahmet_bases, mehmet_bases, raw_key_ahmet, raw_key_mehmet):
        if a == b:
            sift_ahmet.append(bit_a)
            sift_mehmet.append(bit_m)

    sift_ahmet = np.array(sift_ahmet)
    sift_mehmet = np.array(sift_mehmet)

    qber = np.mean(sift_ahmet != sift_mehmet) if len(sift_ahmet)>0 else 0

    return sift_ahmet, sift_mehmet, qber


print("---- Arda saldırmıyor ----")
key_a, key_m, qber_clean = bb84_protocol(n=50, attack=False)
print("Ahmet:", key_a)
print("Mehmet:", key_m)
print("QBER:", qber_clean)

print("\n---- Arda saldırıyor ----")
key_a2, key_m2, qber_attack = bb84_protocol(n=50, attack=True)
print("Ahmet:", key_a2)
print("Mehmet:", key_m2)
print("QBER:", qber_attack)

