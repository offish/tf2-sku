tf2-sku
=======
|pypi| |license| |stars| |issues| |repo_size| |chat|

|donate_steam| |donate|

Format items as strings or objects using Python 3. 
Python port of `node-tf2-sku`_.

.. _node-tf2-sku: https://github.com/Nicklason/node-tf2-sku

.. contents:: Table of Contents
    :depth: 1

Installing
----------
Install and update using `pip`_:

.. code-block:: text

    pip install tf2-sku

.. _pip: https://pip.pypa.io/en/stable/quickstart/

Usage
-----

.. code-block:: python
   
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


License
-------
Copyright (c) 2020 `offish`_

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

.. _offish: https://offi.sh


.. |pypi| image:: https://img.shields.io/pypi/v/tf2-sku.svg
    :target: https://pypi.org/project/tf2-sku
    :alt: Latest version released on PyPi

.. |license| image:: https://img.shields.io/github/license/offish/tf2-sku.svg
    :target: https://github.com/offish/tf2-sku/blob/master/LICENSE
    :alt: License

.. |stars| image:: https://img.shields.io/github/stars/offish/tf2-sku.svg
    :target: https://github.com/offish/tf2-sku/stargazers
    :alt: Stars

.. |issues| image:: https://img.shields.io/github/issues/offish/tf2-sku.svg
    :target: https://github.com/offish/tf2-sku/issues
    :alt: Issues

.. |repo_size| image:: https://img.shields.io/github/repo-size/offish/tf2-sku.svg
    :target: https://github.com/offish/tf2-sku
    :alt: Repo Size

.. |chat| image:: https://img.shields.io/discord/467040686982692865.svg
    :target: https://discord.gg/t8nHSvA
    :alt: Discord

.. |donate_steam| image:: https://img.shields.io/badge/donate-steam-green.svg
    :target: https://steamcommunity.com/tradeoffer/new/?partner=293059984&token=0-l_idZR
    :alt: Donate via Steam

.. |donate| image:: https://img.shields.io/badge/donate-paypal-blue.svg
    :target: https://www.paypal.me/0ffish
    :alt: Donate via PayPal
