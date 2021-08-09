from .prettify import prettify


TEMPLATE = {
    'defindex': 0,
    'quality': 0,
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


def to_sku(item):
    """Convert SKU to item object
    """
    item = prettify(item, TEMPLATE)

    sku = f'{item["defindex"]};{item["quality"]}'
    
    if 'craftable' in item and not item['craftable']:
        sku += ';uncraftable'

    if 'effect' in item and item['effect']:
        sku += f';u{item["effect"]}'
    
    if 'australium' in item and item['australium']:
        sku += ';australium'
    
    if 'wear' in item and item['wear']:
        sku += f';w{item["wear"]}'

    if 'paintkit' in item and item['paintkit']:
        sku += f';pk{item["paintkit"]}'
    
    if 'quality2' in item and item['quality2'] == 11:
        sku += ';strange'
    
    if isinstance(item['killstreak'], int) and not item['killstreak'] == 0:
        sku += f'kt-{item["killstreak"]}'
    
    if 'target' in item and item['target']:
        sku += f'td-{item["target"]}'

    if 'festive' in item and item['festive']:
        sku += ';festive'
    
    if 'craftnumber' in item and item['craftnumber']:
        sku += f'n${item["craftnumber"]}'
    
    if 'crateseries' in item and item['crateseries']:
        sku += f'c{item["crateseries"]}'
    
    if 'output' in item and item['output']:
        sku += f'od-{item["output"]}'
    
    if 'outputQuality' in item and item['outputQuality']:
        sku += f'oq-{item["outputQuality"]}'

    return sku


def from_sku(sku):
    """Convert item object to SKU
    """
    attributes = {}
    parts = sku.split(';')

    if len(parts) > 0:
        if parts[0].isnumeric():
            attributes['defindex'] = int(parts[0])
        parts.pop(0)

    if len(parts) > 0:
        if parts[0].isnumeric():
            attributes['quality'] = int(parts[0])
        parts.pop(0)

    for part in parts:
        attribute = part.replace('-', '')

        if attribute == 'uncraftable':
            attributes['craftable'] = False

        elif attribute == 'australium':
            attributes['australium'] = True

        elif attribute == 'festive':
            attributes['festive'] = True

        elif attribute == 'strange':
            attributes['quality2'] = 11

        elif attribute.startswith('kt') and attribute[2:].isnumeric():
            attributes['killstreak'] = int(attribute[2:])

        elif attribute.startswith('u') and attribute[1:].isnumeric():
            attributes['effect'] = int(attribute[1:])

        elif attribute.startswith('pk') and attribute[2:].isnumeric():
            attributes['paintkit'] = int(attribute[2:])

        elif attribute.startswith('w') and attribute[1:].isnumeric():
            attributes['wear'] = int(attribute[1:])

        elif attribute.startswith('td') and attribute[2:].isnumeric():
            attributes['target'] = int(attribute[2:])

        elif attribute.startswith('n') and attribute[1:].isnumeric():
            attributes['craftnumber'] = int(attribute[1:])

        elif attribute.startswith('c') and attribute[1:].isnumeric():
            attributes['crateseries'] = int(attribute[1:])

        elif attribute.startswith('od') and attribute[2:].isnumeric():
            attributes['output'] = int(attribute[2:])

        elif attribute.startswith('oq') and attribute[2:].isnumeric():
            attributes['outputQuality'] = int(attribute[2:])

    item = prettify(attributes, TEMPLATE)

    return item
