from tf2_sku import to_sku, from_sku

# To SKU
# Mann Co. Supply Crate Key
item = {
    'defindex': 5021,
    'quality': 6,
    'craftable': True,
    'killstreak': 0,
    'australium': False,
    'festive': False,
    'effect': None,
    'paintkit': None,
    'wear': None,
    'quality2': None,
    'target': None,
    'craftnumber': None,
    'crateseries': None,
    'output': None,
    'outputQuality': None
}

print(to_sku(item))
# '5021;6'


# From SKU
# Mann Co. Supply Crate Key
sku = '5021;6'

print(from_sku(sku))
# {'defindex': 5021, 'quality': 6, 'craftable': True, 'killstreak': 0, 'australium': False, 'festive': False}
