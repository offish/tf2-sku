import re


def get_properties(sku: str) -> list[str]:
    return sku.split(";")


def get_property(sku: str, index: int) -> str:
    return get_properties(sku)[index]


def get_defindex(sku: str) -> int:
    return int(get_property(sku, 0))


def get_quality(sku: str) -> int:
    return int(get_property(sku, 1))


def has_uncraftable_in_sku(sku: str) -> bool:
    return ";uncraftable" in sku


def has_strange_in_sku(sku: str) -> bool:
    return ";strange" in sku


def has_australium_in_sku(sku: str) -> bool:
    return ";australium" in sku


def has_festive_in_sku(sku: str) -> bool:
    return ";festive" in sku


def is_sku(sku: str) -> bool:
    properties = get_properties(sku)

    if len(properties) < 2:
        return False

    is_sku = True

    try:
        get_defindex(sku)
        get_quality(sku)
    except ValueError:
        is_sku = False
    finally:
        return is_sku


def is_key(sku: str) -> bool:
    return sku == "5021;6"


def is_metal(sku: str) -> bool:
    return sku in ["5000;6", "5001;6", "5002;6"]


def is_pure(sku: str) -> bool:
    return is_metal(sku) or is_key(sku)


def is_craftable(sku: str) -> bool:
    return not has_uncraftable_in_sku(sku)


def is_uncraftable(sku: str) -> bool:
    return has_uncraftable_in_sku(sku)


def get_property_by_key(sku: str, key: str) -> str | None:
    for part in get_properties(sku):
        match = re.search(key + r"(\d+)", part)

        if match:
            return match.group(1)


def get_key_value_property(sku: str, key: str) -> int:
    value = get_property_by_key(sku, key)

    if value is None:
        return -1

    return int(value.replace(key, ""))


def get_effect(sku: str) -> int:
    return get_key_value_property(sku, "u")


def get_wear(sku: str) -> int:
    return get_key_value_property(sku, "w")


def get_skin(sku: str) -> int:
    return get_key_value_property(sku, "pk")


def get_killstreak(sku: str) -> int:
    return get_key_value_property(sku, "kt-")


def get_sheen(sku: str) -> int:
    return get_key_value_property(sku, "ks-")


def get_killstreaker(sku: str) -> int:
    return get_key_value_property(sku, "ke-")


def get_target_defindex(sku: str) -> int:
    return get_key_value_property(sku, "td-")


def get_craft_number(sku: str) -> int:
    return get_key_value_property(sku, "n")


def get_crate_number(sku: str) -> int:
    return get_key_value_property(sku, "c")


def get_output_defindex(sku: str) -> int:
    return get_key_value_property(sku, "od-")


def get_output_quality(sku: str) -> int:
    return get_key_value_property(sku, "oq-")
