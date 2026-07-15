# tf2-sku
[![Stars](https://img.shields.io/github/stars/offish/tf2-sku.svg)](https://github.com/offish/tf2-sku/stargazers)
[![Issues](https://img.shields.io/github/issues/offish/tf2-sku.svg)](https://github.com/offish/tf2-sku/issues)
[![Size](https://img.shields.io/github/repo-size/offish/tf2-sku.svg)](https://github.com/offish/tf2-sku)
[![Discord](https://img.shields.io/discord/467040686982692865?color=7289da&label=Discord&logo=discord)](https://discord.gg/t8nHSvA)
[![Downloads](https://img.shields.io/pypi/dm/tf2-sku)](https://pypi.org/project/tf2-sku/)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Parse TF2 items to SKU format with Python.

> [!TIP]
> Use [tf2-utils](https://github.com/offish/tf2-utils) to get SKUs directly from inventories or offers.

## Donate
- BTC: `bc1q9gmh5x2g9s0pw3282a5ypr6ms8qvuxh3fd7afh`
- [Steam Trade Offer](https://steamcommunity.com/tradeoffer/new/?partner=293059984&token=0-l_idZR)

## Usage
```python
>>> from tf2_sku import to_sku, from_sku

>>> to_sku({"defindex": 5021, "quality": 6})
"5021;6"
# https://marketplace.tf/items/tf2/5021;6

>>> from_sku("161;3;kt-3")
{
    "defindex": 161,
    "quality": 3,
    "effect": -1,
    "australium": False,
    "craftable": True,
    "wear": -1,
    "skin": -1,
    "strange": False,
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
# https://marketplace.tf/items/tf2/161;3;kt-3

>>> to_sku({
...    "defindex": 199,
...    "quality": 5,
...    "effect": 702,
...    "wear": 3,
...    "skin": 292,
...    "strange": True,
...    "killstreak_tier": 3
... })
"199;5;u702;w3;pk292;strange;kt-3"
# https://marketplace.tf/items/tf2/199;5;u702;w3;pk292;strange;kt-3
```

## Setup
### Install
```bash
pip install tf2-sku
# or 
python -m pip install tf2-sku
```

### Upgrade
```bash
pip install --upgrade tf2-sku
# or 
python -m pip install --upgrade tf2-sku
```

## Testing
```bash
# tf2-sku/
pytest
```
