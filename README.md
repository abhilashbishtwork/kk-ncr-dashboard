# KK NCR Dashboard

No-login, NCR-only dashboard for Krispy Kreme's 39 live NCR stores
(Delhi, Gurgaon, Noida, Ghaziabad, Faridabad): revenue (online + dine-in),
ratings, and Swiggy/Zomato/Google storefront ops metrics. Refreshed daily.

This is a sibling of the KK Pune dashboard
(`/Users/SushmaS/kk-pune-dashboard/`) — same architecture, same code
structure, different store roster. **Any feature change made to one
should be ported to the other** — that's a standing expectation, not a
one-off.

Key difference from Pune: categories here are a simple `Online` /
`Offline` split (does this store have a real dine-in/POS order stream?),
not an ownership split — all 39 stores are Curefoods-owned, there's no
franchise distinction in NCR.

Live at: https://abhilashbishtwork.github.io/kk-ncr-dashboard/

See `docs/superpowers/specs/` and `docs/superpowers/plans/` for the
original Pune design/plan this was cloned from.
