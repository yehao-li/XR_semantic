import numpy as np
import matplotlib.pyplot as plt

MIU = 40
K = 20


def bit_communication(sinr):
    v = np.log10(1 + 10**(sinr/10))
    r = v / MIU
    return r


def semantic_communication(sinr):
    # logistic function
    k0, x0 = -0.15, -2
    v = 1 / (1 + np.exp(k0 * (sinr - x0)))
    r = v / K
    return r


# plot the semantic and bit communication rate
sinr = np.arange(-10, 25, 0.1)
bit_rate = bit_communication(sinr)
semantic_rate = semantic_communication(sinr)
plt.plot(sinr, bit_rate, label="bit communication")
plt.plot(sinr, semantic_rate, label="semantic communication")
plt.xlabel("SNR (dB)")
plt.ylabel("Sum SemCom (suts/s/Hz)")
plt.legend()
plt.show()
