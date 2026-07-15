from src.tf2_sku import from_sku, to_sku


def test_mann_co_supply_crate_key() -> None:
    sku = "5021;6"
    item = {
        "defindex": 5021,
        "quality": 6,
        "effect": -1,
        "australium": False,
        "craftable": True,
        "wear": -1,
        "skin": -1,
        "strange": False,
        "killstreak_tier": -1,
        "sheen": -1,
        "killstreaker": -1,
        "target_defindex": -1,
        "festivized": False,
        "craft_number": -1,
        "crate_number": -1,
        "output_defindex": -1,
        "output_quality": -1,
    }

    assert to_sku({"defindex": 5021, "quality": 6}) == sku
    assert to_sku(item) == sku
    assert from_sku(sku) == item


def test_uncraftable_team_captain() -> None:
    sku = "378;6;uncraftable"
    item = {
        "defindex": 378,
        "quality": 6,
        "effect": -1,
        "australium": False,
        "craftable": False,
        "wear": -1,
        "skin": -1,
        "strange": False,
        "killstreak_tier": -1,
        "sheen": -1,
        "killstreaker": -1,
        "target_defindex": -1,
        "festivized": False,
        "craft_number": -1,
        "crate_number": -1,
        "output_defindex": -1,
        "output_quality": -1,
    }

    assert to_sku({"defindex": 378, "quality": 6, "craftable": False}) == sku
    assert to_sku(item) == sku
    assert from_sku(sku) == item


def test_professional_rocket_launcher_kit() -> None:
    sku = "6526;6;uncraftable;kt-3;td-205"
    item = {
        "defindex": 6526,
        "quality": 6,
        "effect": -1,
        "australium": False,
        "craftable": False,
        "wear": -1,
        "skin": -1,
        "strange": False,
        "killstreak_tier": 3,
        "sheen": -1,
        "killstreaker": -1,
        "target_defindex": 205,
        "festivized": False,
        "craft_number": -1,
        "crate_number": -1,
        "output_defindex": -1,
        "output_quality": -1,
    }

    assert to_sku(item) == sku
    assert from_sku(sku) == item


def test_professional_festivized_australium_flame_thrower() -> None:
    sku = "208;11;australium;kt-3;festive"
    item = {
        "defindex": 208,
        "quality": 11,
        "effect": -1,
        "australium": True,
        "craftable": True,
        "wear": -1,
        "skin": -1,
        "strange": False,
        "killstreak_tier": 3,
        "sheen": -1,
        "killstreaker": -1,
        "target_defindex": -1,
        "festivized": True,
        "craft_number": -1,
        "crate_number": -1,
        "output_defindex": -1,
        "output_quality": -1,
    }

    assert to_sku(item) == sku
    assert from_sku(sku) == item


def test_professional_strange_isotope_potent_poison_shotgun_field_tested() -> None:
    sku = "199;5;u702;w3;pk292;strange;kt-3"
    item = {
        "defindex": 199,
        "quality": 5,
        "effect": 702,
        "australium": False,
        "craftable": True,
        "wear": 3,
        "skin": 292,
        "strange": True,
        "killstreak_tier": 3,
        "sheen": -1,
        "killstreaker": -1,
        "target_defindex": -1,
        "festivized": False,
        "craft_number": -1,
        "crate_number": -1,
        "output_defindex": -1,
        "output_quality": -1,
    }

    assert to_sku(item) == sku
    assert from_sku(sku) == item


def test_professional_energy_orb_festivized_masked_mender_medi_gun_minimal_wear_manndarin_singularity() -> (
    None
):
    sku = "15008;15;u704;w2;pk5;kt-3;ks-3;ke-2006;festive"
    item = {
        "defindex": 15008,
        "quality": 15,
        "effect": 704,
        "australium": False,
        "craftable": True,
        "wear": 2,
        "skin": 5,
        "strange": False,
        "killstreak_tier": 3,
        "sheen": 3,
        "killstreaker": 2006,
        "target_defindex": -1,
        "festivized": True,
        "craft_number": -1,
        "crate_number": -1,
        "output_defindex": -1,
        "output_quality": -1,
    }

    assert to_sku(item) == sku
    assert from_sku(sku) == item
