from dataclasses import dataclass, fields


MAPPING = {
    "effect": "u{}",
    "australium": "australium",
    "craftable": "uncraftable",
    "wear": "w{}",
    "skin": "pk{}",
    "strange": "strange",
    "killstreak_tier": "kt-{}",
    "target_defindex": "td-{}",
    "festivized": "festive",
    "craft_number": "n{}",
    "crate_number": "c{}",
    "output_defindex": "od-{}",
    "output_quality": "oq-{}",
    "paint": "p",
    # "sheen": "ks-{}",
    # "killstreaker": "ke-{}",
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
    target_defindex: int = -1
    festivized: bool = False
    craft_number: int = -1
    crate_number: int = -1
    output_defindex: int = -1
    output_quality: int = -1
    paint: int = -1
    # sheen: int = -1
    # killstreaker: int = -1

    def __str__(self) -> str:
        sku = f"{self.defindex};{self.quality}"

        for field in fields(self):
            if field.name in ["defindex", "quality"]:
                continue

            value = getattr(self, field.name)

            if value != field.default:
                sku += ";" + MAPPING[field.name].format(value)

        return sku
