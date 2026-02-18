# sankey-infographic-test
Saw a Sankey infographic and wanted to replicate it.

Here's the LLM prompt to fetch the data:


---

## Updated prompt (v3) — URL-based, one-step-at-a-time
Copy/paste and reuse:

1) Ask me for the **ticker only**. Stop.  
2) Ask me for the **as-of date** (or confirm “today”). Stop.  
3) Ask me what **period I want** (e.g., “most recent quarter”, “Q2 FY26”, “FY26 YTD”, “full FY”). Stop.  
4) Based on (1)-(3), **tell me what to look up** (the exact doc type + naming pattern), for example:
   - “`<TICKER> Q2 FY26 earnings press release` / ‘reports fiscal second quarter 2026 financial results’”
   - “`<TICKER> Form 10-Q` (quarterly report)”
   - “earnings slide deck / supplemental tables”  
   Then ask me for **the single best official URL** (prefer Investor Relations). Stop.
5) When I paste the URL, **confirm the URL** back to me and ask:  
   **Output preference:**  
   - (A) “JSON payload only” (for your Sankey script), or  
   - (B) “JSON + short narrative validation notes.” Stop.
6) Then do research in this order:
   - Use web_search to collect **context** (what quarter, headline results, any known special items). Cite every non-obvious fact.  
   - Use web_search on the **provided URL** to extract/verify the income statement line items (and segment splits if present). Cite every non-obvious fact.  
   - If a field isn’t explicitly available in the source document, set it to `null` and list it as “missing”.
7) Finally output **ONLY** one JSON object with these exact keys (values in **$M**):
   - `title` (string, e.g., `"WDC Q2 FY26 (ended YYYY-MM-DD)"`)
   - `Product revenue`
   - `Subscription & support revenue`
   - `Total revenue`
   - `Cost of revenue`
   - `Gross profit`
   - `Sales & marketing`
   - `R&D`
   - `G&A`
   - `Operating income`
   - `Other income, net`
   - `Provision for income taxes`
   - `Net income`

---

## What I’ll tell you to look up (example using your WDC scenario)
If ticker = **WDC** and as-of date = **2/18/26**, the likely best source is the **earnings press release** titled like: “Western Digital Reports Fiscal Second Quarter 2026 Financial Results” (often Business Wire / IR page). [1]  
You then paste the official IR URL (like the one you gave).

---

This is an incomplete workflow as of yet. The idea is to enter parameters that drive the process to the end.
1. What ticker and timeframe.
2. Fetch the data, all of it. Some may have to be gathered from an investor website.
3. Create the data document that's added to the app's data folder.
4. Run the app, create the infographic.