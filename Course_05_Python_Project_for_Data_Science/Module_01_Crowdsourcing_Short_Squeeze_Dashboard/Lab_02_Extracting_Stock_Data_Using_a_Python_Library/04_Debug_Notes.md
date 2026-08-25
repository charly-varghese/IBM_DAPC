# Debug Notes — Lab 02

## Lab

\*_Extracting Stock Data Using a Python Library_

## Error 1 — `NameError: stock_history is not defined`

### Problem

While building the multi-stock analysis in `02_My_Practice.py`, the program raised:

````text
NameError: name 'stock_history' is not defined
The error occurred because stock_history was referenced before it was created.

Incorrect Order
stock_results.append(
    {
        "Trading Days": len(stock_history),
        "Average Close": round(average_close, 2),
        "Total Volume": total_volume,
    }
)

stock_history = stock.history(period="1y")

The variables were being used before they had been assigned values.

Solution

The execution order was corrected:

stock_history = stock.history(period="1y")

average_close = stock_history["Close"].mean()
total_volume = stock_history["Volume"].sum()

stock_results.append(
    {
        "Trading Days": len(stock_history),
        "Average Close": round(average_close, 2),
        "Total Volume": total_volume,
    }
)
Key Lesson

Python variables must be created before they are used.

The correct processing sequence is:

Create Stock Object
        ↓
Extract Stock Information
        ↓
Extract Historical Data
        ↓
Calculate Metrics
        ↓
Store Results
Error 2 — Incorrect Indentation / Code Order
Problem

During the development of the multi-stock section, some code was accidentally placed outside the for loop.

This caused the DataFrame to be created before the stock results had been collected.

Solution

The complete stock-analysis logic was kept inside the loop:

for ticker in tickers:
    ...
    stock_history = stock.history(period="1y")
    ...
    stock_results.append(...)

The final DataFrame was created only after the loop completed:

multi_stock_summary = pd.DataFrame(stock_results)
Key Lesson

Python indentation controls program structure.

Code that belongs to a for loop must be indented inside the loop.

Validation

After fixing the errors:

01_IBM_Lab.py runs successfully.
02_My_Practice.py runs successfully.
03_Challenge.py runs successfully.
No traceback remains.
Multi-stock analysis works for AAPL, MSFT, NVDA, and AMD.
Final Status

Lab 02 Debugging — RESOLVED ✅


