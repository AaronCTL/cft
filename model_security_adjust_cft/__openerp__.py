# -*- coding: utf-8 -*-
# Copyright 2016 Ecosoft Co. Ltd.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Model Security Adjust CFT",
    "version": "8.0.1.1.0",
    "author": "Ecosoft Co. Ltd.",
    "license": "AGPL-3",
    "description": """
    """,
    "category": "Uncategorized",
    "depends": [
        'crm','purchase','product_price_visible',
    ],
    "data": [
        'security/sale_security.xml',
        'security/product_security.xml',
        'security/base_security.xml',
        'views/account_invoice_view.xml',
        'views/partner_view.xml',
        'data/ir.model.access.csv',
    ],
    "js": [
    ],
    "css": [
    ],
    "auto_install": False,
    "installable": True,
    "external_dependencies": {
        'python': [],
    },
}