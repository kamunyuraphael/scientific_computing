"""Task 2 - NumPy Arrays and Numerical Computation
PART 1 original | PART 2 changed input | PART 3 related case (greenhouse IoT)"""
import numpy as np

print("=== PART 1: Original - weather station ===")
temperatures_c = np.array([
    18.5, 18.0, 17.8, 17.5, 17.9, 19.0,
    21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
    29.4, 29.1, 28.5, 27.6, 26.2, 24.8,
    23.4, 22.1, 21.0, 20.2, 19.6, 19.0
])
mean_temp, min_temp, max_temp = np.mean(temperatures_c), np.min(temperatures_c), np.max(temperatures_c)
temperatures_f = 1.8 * temperatures_c + 32
print(f"Daily mean temperature: {mean_temp:.2f} C")
print(f"Minimum temperature: {min_temp:.2f} C")
print(f"Maximum temperature: {max_temp:.2f} C")
print("First six Fahrenheit readings:", temperatures_f[:6])

print("\n=== PART 2: Changed input - midday (12:00) reading is a sensor spike (29.4 -> 45.0) ===")
spiked = temperatures_c.copy()
spiked[12] = 45.0
print(f"Mean: {spiked.mean():.2f} C (was {mean_temp:.2f})")
print(f"Max : {spiked.max():.2f} C (was {max_temp:.2f})")
print(f"Median: {np.median(spiked):.2f} C (was {np.median(temperatures_c):.2f})")

print("\n=== PART 3: Related case - greenhouse IoT, 24 hourly readings ===")
rng = np.random.default_rng(7)
hours = np.arange(24)
greenhouse_c = 24 + 6*np.sin((hours - 9) * np.pi / 12) + rng.normal(0, 0.4, 24)
alert_limit = 28.0
alerts = greenhouse_c > alert_limit
kelvin = greenhouse_c + 273.15
print(f"Mean {greenhouse_c.mean():.2f} C | min {greenhouse_c.min():.2f} C | max {greenhouse_c.max():.2f} C")
print(f"Hours above {alert_limit} C: {alerts.sum()} -> hours {hours[alerts]}")
print(f"Std deviation: {greenhouse_c.std(ddof=1):.2f} C")
print(f"Max in Kelvin: {kelvin.max():.2f} K")
