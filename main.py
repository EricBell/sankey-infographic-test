import json
import sys
import plotly.graph_objects as go

DATA_FILE = sys.argv[1] if len(sys.argv) > 1 else "data/PANW_Q2_FY26.json"

with open(DATA_FILE) as f:
    d = json.load(f)

title = d.pop("title", DATA_FILE)

nodes = [
    "Product revenue",
    "Subscription & support revenue",
    "Total revenue",
    "Cost of revenue",
    "Gross profit",
    "Sales & marketing",
    "R&D",
    "G&A",
    "Operating income",
    "Other income, net",
    "Provision for income taxes",
    "Net income"
]

idx = {name: i for i, name in enumerate(nodes)}

links = [
    ("Product revenue", "Total revenue", d["Product revenue"]),
    ("Subscription & support revenue", "Total revenue", d["Subscription & support revenue"]),
    ("Total revenue", "Cost of revenue", d["Cost of revenue"]),
    ("Total revenue", "Gross profit", d["Gross profit"]),
    ("Gross profit", "Sales & marketing", d["Sales & marketing"]),
    ("Gross profit", "R&D", d["R&D"]),
    ("Gross profit", "G&A", d["G&A"]),
    ("Gross profit", "Operating income", d["Operating income"]),
    ("Operating income", "Other income, net", d["Other income, net"]),
    ("Operating income", "Provision for income taxes", d["Provision for income taxes"]),
    ("Operating income", "Net income", d["Net income"]),
]

source = [idx[s] for s, t, v in links]
target = [idx[t] for s, t, v in links]
value  = [v for s, t, v in links]

node_colors = [
    "#2f2f2f", "#2f2f2f", "#000000",  # revenue components + total
    "#b22222",                         # cost
    "#2e7d32",                         # gross profit
    "#b22222", "#b22222", "#b22222",   # opex components
    "#2e7d32",                         # operating income
    "#2e7d32",                         # other
    "#b22222",                         # tax
    "#2e7d32"                          # net income
]

link_colors = []
for s, t, v in links:
    if t in ["Cost of revenue", "Sales & marketing", "R&D", "G&A", "Provision for income taxes"]:
        link_colors.append("rgba(178,34,34,0.45)")
    elif t in ["Gross profit", "Operating income", "Other income, net", "Net income"]:
        link_colors.append("rgba(46,125,50,0.45)")
    else:
        link_colors.append("rgba(60,60,60,0.45)")

fig = go.Figure(data=[go.Sankey(
    arrangement="snap",
    textfont=dict(color="black", shadow="none", size=18, family="Arial"),
    node=dict(
        pad=18,
        thickness=16,
        line=dict(color="rgba(0,0,0,0.25)", width=0.5),
        label=[f"{n}<br>${d[n]:,}M" for n in nodes],
        color=node_colors
    ),
    link=dict(
        source=source,
        target=target,
        value=value,
        color=link_colors
    )
)])

fig.update_layout(
    title=title,
    font=dict(size=12, family="Arial", color="black"),
    width=1200,
    height=650
)

if __name__ == "__main__":
    fig.show()
