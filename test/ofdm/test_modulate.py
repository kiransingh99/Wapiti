from src.ofdm.modulate import modulate_sequence


def test_modulate_sequence():
    K = 2
    N = 8
    Q1 = 1
    Q2 = 3
    Q = Q2 - Q1 # 4

    P = N + K # size of each ofdm block
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = modulate_sequence(x, N, K, Q1, Q2)
    assert len(y) == P * len(x) // Q