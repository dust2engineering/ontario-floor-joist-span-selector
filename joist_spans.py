#!/usr/bin/env python3
"""Part 9 floor joist span selector (OBC 2024, Table 9.23.4.2.-A).
Usage:
  python3 joist_spans.py --species SPF --size 38x184 --spacing 400 --restraint B
  python3 joist_spans.py --species SPF --spacing 400 --restraint B --need-span 3.6
--restraint: S strapping, B bridging, SB strapping + bridging
"""
import argparse, json, os
D = json.load(open(os.path.join(os.path.dirname(__file__), "joist-span-table.json")))
KEY = {"SPF": "Spruce - Pine - Fir, No. 1 and No. 2", "DFL": "Douglas Fir - Larch, No. 1 and No. 2"}
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--species", choices=["SPF", "DFL"], required=True)
    ap.add_argument("--size", default=None)
    ap.add_argument("--spacing", type=int, choices=[300, 400, 600], default=400)
    ap.add_argument("--restraint", choices=["S", "B", "SB"], default="B")
    ap.add_argument("--need-span", type=float, default=None)
    a = ap.parse_args()
    table = D["spans_m"][KEY[a.species]]
    idx = [300, 400, 600].index(a.spacing)
    if a.need_span:
        ok = [(s, table[s][a.restraint][idx]) for s in table if table[s][a.restraint][idx] >= a.need_span]
        if ok:
            print(f"Smallest {a.species} joist spanning {a.need_span} m at {a.spacing} mm o.c. ({a.restraint}): {ok[0][0]} - max span {ok[0][1]} m")
        else:
            print(f"No {a.species} joist in the table spans {a.need_span} m at {a.spacing} mm o.c. ({a.restraint}). Reduce spacing, add a beam, or leave Part 9 prescriptive tables.")
        return
    print(f"{KEY[a.species]}, {a.size}, {a.spacing} mm o.c., restraint {a.restraint}: maximum span {table[a.size][a.restraint][idx]} m (Table 9.23.4.2.-A)")
if __name__ == "__main__":
    main()
