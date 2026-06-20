r"""Generate an HTML indicator-card grid for the Qhawarina project page from the live data exports.
Prints the HTML block to stdout; paste into content/projects/qhawarina/index.md.
"""
import json, os
D = r"D:\qhawarina\public\assets\data"


def g(f):
    try:
        return json.load(open(os.path.join(D, f), encoding="utf-8"))
    except Exception:
        return {}


price = g("daily_price_index.json").get("latest", {})
infl = g("inflation_nowcast.json").get("nowcast", {})
gdp = g("gdp_nowcast.json").get("nowcast", {})
pol = g("political_index_daily.json")
polcur = pol.get("current", {}) if isinstance(pol, dict) else {}
povn = g("poverty_nowcast.json")
povm = (povn.get("monthly_series") or [{}])[-1] if isinstance(povn, dict) else {}

# political "current": 7-day score vs the 2025 baseline of 100
pol_score = polcur.get("score")
LVL = {"MINIMO": "minimal", "BAJO": "low", "MEDIO": "moderate", "ALTO": "high", "EXTREMO": "extreme"}
pol_level = LVL.get((polcur.get("level") or "").upper(), (polcur.get("level") or "").lower())
DOT = " &middot; "

cards = [
    ("Daily price index", f"{price.get('index_all', 0):.1f}", f"{price.get('cum_pct', 0):+.1f}% cumulative{DOT}{int(price.get('n_products_today', 0)):,} products/day"),
    ("Monthly inflation nowcast", f"{infl.get('value', 0):.1f}%", f"target {infl.get('target_period', '')}"),
    ("GDP nowcast", f"{gdp.get('value', 0):+.1f}%", f"year-on-year{DOT}{gdp.get('target_period', '')}"),
    ("Political-risk index", (f"{pol_score:.0f}" if isinstance(pol_score, (int, float)) else "live"), f"{pol_level} level{DOT}vs 2025 baseline of 100"),
    ("Poverty nowcast", f"{povm.get('national_rolling3m', 0):.1f}%", f"national{DOT}{povm.get('month', '')}"),
]

out = ['<div class="qh-cards">']
for label, val, sub in cards:
    out.append(
        f'  <div class="qh-card"><div class="qh-val">{val}</div>'
        f'<div class="qh-label">{label}</div><div class="qh-sub">{sub}</div></div>'
    )
out.append('</div>')
out.append('<p class="qh-note">Latest readings from the Qhawarina exports (June 2026). '
           '<a href="https://github.com/cesarchavezp29/qhawarina">Code &amp; daily data on GitHub</a>.</p>')
print("\n".join(out))
