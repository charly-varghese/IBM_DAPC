"""
=========================================================
CV_05 – My Practice

Business Statistics using NumPy
=========================================================
"""

import numpy as np

monthly_profit = np.array(
    [42000, 45000, 47000, 52000, 51000, 56000, 60000, 62000, 65000, 67000, 70000, 75000]
)

print("=" * 60)
print("MONTHLY PROFIT ANALYSIS")
print("=" * 60)

print("\nProfit Data")
print(monthly_profit)

print("\nTotal Profit")
print(np.sum(monthly_profit))

print("\nAverage Profit")
print(np.mean(monthly_profit))

print("\nMedian Profit")
print(np.median(monthly_profit))

print("\nHighest Profit")
print(np.max(monthly_profit))

print("\nLowest Profit")
print(np.min(monthly_profit))

print("\nStandard Deviation")
print(np.std(monthly_profit))

print("\nVariance")
print(np.var(monthly_profit))

print("\n90th Percentile")
print(np.percentile(monthly_profit, 90))
