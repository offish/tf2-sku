from .utils import SKU, MAPPING


def to_sku(item: dict) -> str:
    """Takes an item dictionary and formats it to a SKU.
    Example:

    """
    sku = SKU(**item)
    return str(sku)


def from_sku(sku: str) -> dict:
    """Takes a SKU and formats it to an item dictionary.
    Example:

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

            elif key == "quality2":
                value = 11

            else:
                if not value:
                    value = True

                else:
                    value = int(value)

            item[key] = value
            break

    sku = SKU(**item)
    return sku.__dict__
