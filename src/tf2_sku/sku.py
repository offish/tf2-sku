from .utils import SKU, MAPPING


def to_sku(item: dict) -> str:
    """Takes an item dictionary and formats it to a SKU.

    :param item: Item dictionary containing specific keys and values
    :type item: dict

    :return: SKU string
    :rtype: str

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
        "output_quality": -1,
        "paint": -1,
    })
    """
    sku = SKU(**item)
    return str(sku)


def from_sku(sku: str) -> dict:
    """Takes a SKU and formats it to an item dictionary.

    :param sku: SKU string
    :type sku: str

    :return: Item dictionary containing specific keys and values
    :rtype: dict

    Example:
    from_sku("199;5;u702;w3;pk292;strange;kt-3")
    """
    parts = sku.split(";")
    item = {"defindex": int(parts[0]), "quality": int(parts[1])}

    for part in parts[2:]:
        for key in MAPPING:
            default = MAPPING[key].format("")

            if not default in part:
                continue

            value = part.replace(default, "")

            if key == "craftable":
                value = False

            else:
                if not value:
                    value = True

                else:
                    value = int(value)

            item[key] = value
            break

    sku = SKU(**item)
    return sku.__dict__
