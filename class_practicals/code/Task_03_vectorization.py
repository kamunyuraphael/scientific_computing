"""Task 3 - Mathematical Functions and Vectorization
PART 1 original | PART 2 changed N | PART 3 related case (ADC voltage -> RMS)"""
import numpy as np
import timeit

def compare(latency_ms):
    def loop_version():
        squared = []
        for value in latency_ms:
            seconds = value / 1000.0
            squared.append(seconds ** 2)
        return squared
    def vectorized_version():
        seconds = latency_ms / 1000.0
        return seconds ** 2
    loop_time = timeit.timeit(loop_version, number=1)
    vector_time = timeit.timeit(vectorized_version, number=3) / 3
    return loop_time, vector_time, vectorized_version()

print("=== PART 1: Original - 1,000,000 latency readings ===")
rng = np.random.default_rng(42)
latency_ms = rng.uniform(5, 250, 1_000_000)
loop_time, vector_time, result = compare(latency_ms)
print("First five squared latency values:", result[:5])
print(f"Loop time: {loop_time:.4f} s")
print(f"Vectorized time: {vector_time:.6f} s")
print(f"Approximate speed-up: {loop_time/vector_time:.1f}x")

print("\n=== PART 2: Changed input - N = 1,000 instead of 1,000,000 ===")
small = rng.uniform(5, 250, 1_000)
lt, vt, _ = compare(small)
print(f"Loop time: {lt:.6f} s | Vectorized: {vt:.8f} s | speed-up: {lt/vt:.1f}x")

print("\n=== PART 3: Related case - ADC samples to RMS voltage (2,000,000 samples) ===")
# 12-bit ADC (0-4095 counts) mapped to 0-3.3 V; remove DC offset then RMS
counts = rng.integers(0, 4096, 2_000_000)
def rms_loop():
    total = 0.0
    for c in counts:
        total += (c * 3.3 / 4095) ** 2
    return (total / len(counts)) ** 0.5
def rms_vec():
    volts = counts * 3.3 / 4095
    return np.sqrt(np.mean(volts ** 2))
t_loop = timeit.timeit(rms_loop, number=1)
t_vec = timeit.timeit(rms_vec, number=3) / 3
print(f"RMS (loop) = {rms_loop():.6f} V | RMS (vectorized) = {rms_vec():.6f} V")
print(f"Loop {t_loop:.3f} s | Vectorized {t_vec:.5f} s | speed-up {t_loop/t_vec:.0f}x")
x = np.linspace(0, 2*np.pi, 1_000_000)
print("Identity check max |sin^2+cos^2-1| =", np.max(np.abs(np.sin(x)**2 + np.cos(x)**2 - 1)))
