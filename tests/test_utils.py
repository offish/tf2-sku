from src.tf2_sku import (
    get_craft_number,
    get_crate_number,
    get_defindex,
    get_effect,
    get_killstreak,
    get_killstreaker,
    get_output_defindex,
    get_output_quality,
    get_properties,
    get_property,
    get_quality,
    get_sheen,
    get_skin,
    get_target_defindex,
    get_wear,
    has_australium_in_sku,
    has_festive_in_sku,
    has_strange_in_sku,
    has_uncraftable_in_sku,
    is_craftable,
    is_key,
    is_metal,
    is_pure,
    is_sku,
    is_uncraftable,
)


def test_is_sku() -> None:
    assert is_sku("734;6;uncraftable")
    assert not is_sku("734")
    assert not is_sku("something;text")


def test_properties() -> None:
    sku = "734;6;uncraftable"

    assert get_properties(sku) == ["734", "6", "uncraftable"]
    assert get_property(sku, 0) == "734"
    assert get_property(sku, 1) == "6"
    assert get_property(sku, 2) == "uncraftable"


def test_specialized_festivized_australium_flame_thrower() -> None:
    sku = "208;11;australium;kt-2;festive"

    assert get_defindex(sku) == 208
    assert get_quality(sku) == 11
    assert has_australium_in_sku(sku)
    assert get_killstreak(sku) == 2
    assert has_festive_in_sku(sku)
    assert is_craftable(sku)
    assert get_effect(sku) == -1
    assert not has_strange_in_sku(sku)


def test_quarantined_collection_case() -> None:
    sku = "5822;6;c96"

    assert get_crate_number(sku) == 96
    assert get_craft_number(sku) == -1
    assert get_effect(sku) == -1
    assert get_wear(sku) == -1
    assert get_skin(sku) - 1
    assert not is_uncraftable(sku)


def test_strange_isotope_secretly_serviced_war_paint_factory_new() -> None:
    sku = "17412;11;u702;w1;pk412"

    assert get_quality(sku) == 11
    assert get_effect(sku) == 702
    assert get_wear(sku) == 1
    assert get_skin(sku) == 412
    assert get_target_defindex(sku) == -1
    assert get_output_defindex(sku) == -1
    assert get_output_quality(sku) == -1
    assert not has_strange_in_sku(sku)
    assert not has_festive_in_sku(sku)
    assert not has_uncraftable_in_sku(sku)


def test_professional_iron_bomber_kit() -> None:
    sku = "6526;6;uncraftable;kt-3;td-1151"

    assert is_uncraftable(sku)
    assert get_killstreak(sku) == 3
    assert get_target_defindex(sku) == 1151
    assert get_output_defindex(sku) == -1
    assert get_output_quality(sku) == -1
    assert get_killstreaker(sku) == -1
    assert get_sheen(sku) == -1


def test_brawling_buccaneer() -> None:
    sku = "30131;6;n1"

    assert get_craft_number(sku) == 1
    assert get_crate_number(sku) == -1
    assert is_craftable(sku)


def test_sydney_sleeper_chemistry_set() -> None:
    sku = "20006;6;od-230;oq-14"

    assert get_defindex(sku) == 20006
    assert get_quality(sku) == 6
    assert get_output_defindex(sku) == 230
    assert get_output_quality(sku) == 14


def test_professional_energy_orb_festivized_masked_mender_medi_gun_minimal_wear_manndarin_singularity() -> (
    None
):
    sku = "15008;15;u704;w2;pk5;kt-3;ks-3;ke-2006;festive"

    assert get_quality(sku) == 15
    assert get_effect(sku) == 704
    assert get_wear(sku) == 2
    assert get_skin(sku) == 5
    assert get_killstreak(sku) == 3
    assert get_sheen(sku) == 3
    assert get_killstreaker(sku) == 2006
    assert has_festive_in_sku(sku)


def test_is_metal() -> None:
    assert is_metal("5000;6")
    assert is_metal("5001;6")
    assert is_metal("5002;6")
    assert not is_metal("5021;6")


def test_is_key() -> None:
    assert is_key("5021;6")
    assert not is_key("5021;5")
    assert not is_key("5000;6")
    assert not is_key("5001;6")
    assert not is_key("5002;6")


def test_is_pure() -> None:
    assert is_pure("5000;6")
    assert is_pure("5001;6")
    assert is_pure("5002;6")
    assert is_pure("5021;6")
    assert not is_pure("5021;7")
