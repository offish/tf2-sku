

def prettify(target, template):
    """Sort properties in an object using a template
    """
    if target == None or template == None:
        raise KeyError('Missing arguments: target, template, or both')

    elif not (isinstance(target, dict) or isinstance(target, list)):
        raise TypeError('Invalid argument: first argument (target) must be an object')

    elif not (isinstance(template, dict) or isinstance(template, list)):
        raise TypeError('Invalid argument: second argument (template) must be either an object or array')

    prettified = {}

    for key in template:

        if key not in template:
            continue
        
        elif isinstance(template, list):
            key = template[key]
        
        
        if not isinstance(key, str):
            raise TypeError('Invalid argument: template list must only contain strings')
        
        try:
            value = target[key]

            if value is not None:
                prettified[key] = value

        except KeyError:
            prettified[key] = template[key]

    return prettified
