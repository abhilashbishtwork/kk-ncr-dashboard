"""Static store roster for the KK NCR dashboard.

Each store is keyed by its exact ClickHouse `store_name` (online orders),
mapped to a display name and category. Confirmed against real ClickHouse
data on 2026-08-20 (39 stores, exact list given by the user) — every
online name and its `pos_name` (dine-in counterpart, where one exists)
was cross-checked directly against `orders`.

Category is a simplified 2-way split for v1, pending the real Curefoods-
owned vs. franchise ownership split (which Pune has as Cfi/Rebel/Offline
and NCR doesn't have yet):
  - "Offline": has a real POS/dine-in order stream in ClickHouse (13 stores)
  - "Online": online-only, no POS counterpart found (26 stores)
This is NOT an ownership split — it only reflects whether the store has a
dine-in channel. Replace with a real ownership categorization once
available, the same way Pune's Cfi/Rebel split came from the business.
"""

CATEGORIES = ("Online", "Offline")

STORE_ROSTER = [
    {"up_name": "GGN KK Ardee Mall Online", "pos_name": "GGN KK ARDEE MALL POS", "display_name": "Ardee Mall", "category": "Offline"},
    {"up_name": "GGN KK Ambience Mall Online", "pos_name": "GGN KK Ambience Mall POS", "display_name": "Ambience Mall", "category": "Offline"},
    {"up_name": "DEL KK Promenade Mall , Vasant Kunj Online", "pos_name": None, "display_name": "Promenade Mall, Vasant Kunj", "category": "Online"},
    {"up_name": "Noida KK DLF Mall of India Online", "pos_name": None, "display_name": "DLF Mall of India", "category": "Online"},
    {"up_name": "DEL KK Nexus Select CityWalk Mall Online", "pos_name": "DEL KK Nexus Select CityWalk Mall POS", "display_name": "Nexus Select CityWalk Mall", "category": "Offline"},
    {"up_name": "DEL KK Worldmark 1 (Aerocity) Online", "pos_name": "DEL KK Worldmark 1 (Aerocity) POS", "display_name": "Worldmark 1 (Aerocity)", "category": "Offline"},
    {"up_name": "GGN KK Worldmark Sec - 65 Online", "pos_name": "GGN KK Worldmark Sec - 65 POS", "display_name": "Worldmark Sec-65", "category": "Offline"},
    {"up_name": "DEL KK GK1 Online", "pos_name": None, "display_name": "GK1", "category": "Online"},
    {"up_name": "DEL KK Dwarka Online", "pos_name": None, "display_name": "Dwarka", "category": "Online"},
    {"up_name": "DEL KK Model Town Online", "pos_name": None, "display_name": "Model Town", "category": "Online"},
    {"up_name": "DEL KK Vasant Kunj Online", "pos_name": None, "display_name": "Vasant Kunj", "category": "Online"},
    {"up_name": "GGN KK Sohna Road Online", "pos_name": None, "display_name": "Sohna Road", "category": "Online"},
    {"up_name": "GGN KK Udyog Vihar Kitchen Online", "pos_name": None, "display_name": "Udyog Vihar Kitchen", "category": "Online"},
    {"up_name": "DEL KK Mayur Vihar Online", "pos_name": None, "display_name": "Mayur Vihar", "category": "Online"},
    {"up_name": "GZB KK Gaur City Online", "pos_name": "GZB KK Gaur City POS", "display_name": "Gaur City", "category": "Offline"},
    {"up_name": "Greater Noida KK Alpha 2 Online", "pos_name": None, "display_name": "Alpha 2", "category": "Online"},
    {"up_name": "DEL KK Dilshad Garden Online", "pos_name": None, "display_name": "Dilshad Garden", "category": "Online"},
    {"up_name": "FDB KK Sector 31 Online", "pos_name": None, "display_name": "Sector 31", "category": "Online"},
    {"up_name": "DEL KK Rohini Kitchen Online", "pos_name": None, "display_name": "Rohini Kitchen", "category": "Online"},
    {"up_name": "DEL KK Saket Online", "pos_name": None, "display_name": "Saket", "category": "Online"},
    {"up_name": "Noida KK Sector 10 Online", "pos_name": None, "display_name": "Sector 10", "category": "Online"},
    {"up_name": "DEL KK Hauz Khas Online", "pos_name": None, "display_name": "Hauz Khas", "category": "Online"},
    {"up_name": "Noida KK Sector 49 Online", "pos_name": None, "display_name": "Sector 49", "category": "Online"},
    {"up_name": "Noida KK Sector 63 Online", "pos_name": None, "display_name": "Sector 63", "category": "Online"},
    {"up_name": "GZB KK Vasundhra Online", "pos_name": None, "display_name": "Vasundhra", "category": "Online"},
    {"up_name": "DEL KK Janakpuri Online", "pos_name": None, "display_name": "Janakpuri", "category": "Online"},
    {"up_name": "GZB KK Shipra Mall Online", "pos_name": "GZB KK Shipra Mall POS", "display_name": "Shipra Mall", "category": "Offline"},
    {"up_name": "DEL KK Pacific Mall NSP Online", "pos_name": "DEL KK Pacific Mall NSP POS", "display_name": "Pacific Mall NSP", "category": "Offline"},
    {"up_name": "DEL KK Kamla Nagar Online", "pos_name": "DEL KK Kamla Nagar POS", "display_name": "Kamla Nagar", "category": "Offline"},
    {"up_name": "FDB KK Sector 15A Online", "pos_name": None, "display_name": "Sector 15A", "category": "Online"},
    {"up_name": "DEL KK Sikandarpur Online", "pos_name": None, "display_name": "Sikandarpur", "category": "Online"},
    {"up_name": "DEL KK Malviya Nagar Online", "pos_name": None, "display_name": "Malviya Nagar", "category": "Online"},
    {"up_name": "DEL KK PUNJABI BAGH Online", "pos_name": None, "display_name": "Punjabi Bagh", "category": "Online"},
    {"up_name": "NOI KK Noida Sec 51 Online", "pos_name": None, "display_name": "Noida Sec 51", "category": "Online"},
    {"up_name": "NOI KK Noida 141 Online", "pos_name": None, "display_name": "Noida 141", "category": "Online"},
    {"up_name": "GGN KK IRIS Broadway Mall Online", "pos_name": "GGN KK IRIS Broadway Mall POS", "display_name": "IRIS Broadway Mall", "category": "Offline"},
    {"up_name": "GGN KK KLJ Square", "pos_name": "GGN KK KLJ Square Pos", "display_name": "KLJ Square", "category": "Offline"},
    {"up_name": "GGN KK Elan Miracle", "pos_name": "GGN KK Elan Miracle Pos", "display_name": "Elan Miracle", "category": "Offline"},
    {"up_name": "DEL KK Omaxe Chandni Chowk", "pos_name": "DEL KK Omaxe Chandni Chowk Pos", "display_name": "Omaxe Chandni Chowk", "category": "Offline"},
]


def up_names():
    return [s["up_name"] for s in STORE_ROSTER]


def pos_names():
    return [s["pos_name"] for s in STORE_ROSTER if s["pos_name"]]


def up_name_for_pos_name(pos_name):
    for s in STORE_ROSTER:
        if s["pos_name"] == pos_name:
            return s["up_name"]
    return None


def display_name_for(up_name):
    for s in STORE_ROSTER:
        if s["up_name"] == up_name:
            return s["display_name"]
    return None


def category_for(up_name):
    for s in STORE_ROSTER:
        if s["up_name"] == up_name:
            return s["category"]
    return None
