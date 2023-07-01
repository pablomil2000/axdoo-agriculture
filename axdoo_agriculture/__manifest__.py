# -*- coding: utf-8 -*-
{
    'name': 'Axdoo Agriculture',
    'version': '15.0.1.0.0',
    'category': 'Tools',
    'summary': 'Axdoo Agriculture Application',
    'license': 'AGPL-3',
    'author': 'Xtendoo',
    'depends': [
        'base',
        'sale',
        'axdoo_field_notebook',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/agriculture_format_view.xml',
        'views/alfinf_control_panel_view.xml',
        'views/res_partner_view.xml',
        'views/agriculture_view.xml',
    ],
    'application': True,
}
