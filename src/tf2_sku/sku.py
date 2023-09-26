from .utils import SKU, MAPPING, has_string_value, get_key_from_value


def to_sku(item: dict) -> str:
    """Takes an item dictionary and formats it to a SKU.

    Args:
        Item dictionary containing specific keys and values.

    Returns:
        SKU string for given item.

    Example:
    to_sku({
        "defindex": 199,
        "quality": 5,
        "effect": 702,
        "australium": False,
        "craftable": True,
        "wear": 3,
        "skin": 292,
        "strange": True,
        "killstreak_tier": 3,
        "target_defindex": -1,
        "festivized": False,
        "craft_number": -1,
        "crate_number": -1,
        "output_defindex": -1,
        "output_quality": -1
    })
    """
    sku = SKU(**item)
    return str(sku)


def from_sku(sku: str) -> dict:
    """Takes a SKU and formats it to an item dictionary.

    Args:
        SKU string. E.g. `199;5;u702;w3;pk292;strange;kt-3`

    Returns:
        Item dictionary containing item properties.
    """
    sku_parts = sku.split(";")
    item = {"defindex": int(sku_parts[0]), "quality": int(sku_parts[1])}

    # loop through each part of the sku
    # -> u702, w3, pk292, strange, kt-3
    for sku_value in sku_parts[2:]:
        # loop through every key
        # effect, australium, craftable
        for map_key in MAPPING:
            default = MAPPING[map_key].format("")

            # dont override
            if map_key in item:
                continue

            # no chance this is the right key -> skip
            if not default in sku_value:
                continue

            value = None

            # check special keys like uncraftable, australium, strange and festive
            if has_string_value(sku_value):
                # get the correct key
                map_key = get_key_from_value(sku_value)
                # craftable is false, everything else true
                value = True if sku_value != "uncraftable" else False
            else:
                # replace the difference
                value = int(sku_value.replace(default, ""))

            item[map_key] = value
            break

    sku = SKU(**item)
    return sku.__dict__
