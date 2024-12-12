## 5 Calculations for Year-over-Year Sales Difference

| Calculation | Formula |
|---|---|
| Current Year | {MAX(YEAR([Order Date]))} |
| Prior Year | [Current Year] - 1 |
| CY Sales | IF [Current Year] = YEAR([Order Date]) THEN [Sales] END |
| PY Sales | IF [Prior Year] = YEAR([Order Date]) THEN [Sales] END |
| CY vs PY | (SUM([CY Sales]) - SUM([PY Sales])) / SUM([PY Sales]) |
