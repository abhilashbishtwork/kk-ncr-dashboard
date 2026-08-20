from build.stores import (
    STORE_ROSTER,
    CATEGORIES,
    up_names,
    pos_names,
    up_name_for_pos_name,
    display_name_for,
    category_for,
)


def test_thirty_nine_stores():
    assert len(STORE_ROSTER) == 39


def test_up_names_unique():
    names = up_names()
    assert len(names) == len(set(names))


def test_all_categories_valid():
    assert all(s["category"] in CATEGORIES for s in STORE_ROSTER)


def test_display_name_for_known_store():
    assert display_name_for("DEL KK GK1 Online") == "GK1"


def test_category_for_gk1_is_online():
    assert category_for("DEL KK GK1 Online") == "Online"


def test_unknown_store_returns_none():
    assert display_name_for("Not A Store") is None
    assert category_for("Not A Store") is None


def test_category_counts_match_spec():
    counts = {}
    for s in STORE_ROSTER:
        counts[s["category"]] = counts.get(s["category"], 0) + 1
    assert counts == {"Offline": 13, "Online": 26}


def test_pos_names_only_for_offline_category_stores():
    offline_up_names = {s["up_name"] for s in STORE_ROSTER if s["category"] == "Offline"}
    pos_having_up_names = {s["up_name"] for s in STORE_ROSTER if s["pos_name"]}
    assert pos_having_up_names == offline_up_names
    assert len(pos_names()) == 13


def test_up_name_for_pos_name_round_trips():
    assert up_name_for_pos_name("GGN KK ARDEE MALL POS") == "GGN KK Ardee Mall Online"
    assert up_name_for_pos_name("DEL KK Omaxe Chandni Chowk Pos") == "DEL KK Omaxe Chandni Chowk"


def test_up_name_for_pos_name_unknown_returns_none():
    assert up_name_for_pos_name("Not A Pos Name") is None
