# -*- coding: utf-8 -*-
{
    'name': 'Axdoo Agriculture',
    'version': '16.0.1.0.0',
    'category': 'Tools',
    'summary': 'Axdoo Agriculture Application',
    'license': 'AGPL-3',
    'author': 'Xtendoo',
    'depends': [
        'base',
        'sale',
        'sale_management',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/agriculture_format_view.xml',
        'views/agriculture_brand_view.xml',
        'views/alfinf_control_panel_view.xml',
        'views/res_partner_view.xml',
        'views/agriculture_view.xml',
        'views/sale_order_view.xml',
    ],
    'application': True,
}
