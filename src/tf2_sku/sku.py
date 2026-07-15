from dataclasses import dataclass, fields

from .utils import get_defindex, get_properties, get_quality

MAPPING = {
    "effect": "u{}",
    "australium": "australium",
    "craftable": "uncraftable",
    "wear": "w{}",
    "skin": "pk{}",
    "strange": "strange",
    "killstreak_tier": "kt-{}",
    "sheen": "ks-{}",
    "killstreaker": "ke-{}",
    "target_defindex": "td-{}",
    "festivized": "festive",
    "craft_number": "n{}",
    "crate_number": "c{}",
    "output_defindex": "od-{}",
    "output_quality": "oq-{}",
    # "paint": "p",
}


@dataclass
class SKU:
    defindex: int
    quality: int
    effect: int = -1
    australium: bool = False
    craftable: bool = True
    wear: int = -1
    skin: int = -1
    strange: bool = False
    killstreak_tier: int = -1
    sheen: int = -1
    killstreaker: int = -1
    target_defindex: int = -1
    festivized: bool = False
    craft_number: int = -1
    crate_number: int = -1
    output_defindex: int = -1
    output_quality: int = -1
    # paint: int = -1

    def __str__(self) -> str:
        sku = f"{self.defindex};{self.quality}"

        for field in fields(self):
            if field.name in ["defindex", "quality"]:
                continue

            value = getattr(self, field.name)

            if value != field.default:
                sku += ";" + MAPPING[field.name].format(value)

        return sku


def has_string_value(sku_value: str) -> bool:
    return sku_value in ["uncraftable", "australium", "strange", "festive"]


def get_key_from_value(value: str) -> str:
    for key in MAPPING:
        if value == MAPPING[key]:
            return key

    return ""


def to_sku(item: dict) -> str:
    sku = SKU(**item)
    return str(sku)


def from_sku(sku: str) -> dict:
    parts = get_properties(sku)
    item = {"defindex": get_defindex(sku), "quality": get_quality(sku)}

    # loop through each part of the sku
    # -> u702, w3, pk292, strange, kt-3
    for sku_value in parts[2:]:
        # loop through every key
        # effect, australium, craftable
        for map_key in MAPPING:
            default = MAPPING[map_key].format("")

            # dont override
            if map_key in item:
                continue

            # no chance this is the right key -> skip
            if default not in sku_value:
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
