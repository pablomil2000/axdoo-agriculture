# -*- coding: utf-8 -*-
{
    'name': 'Axdoo Field Notebook',
    'version': '15.0.1.0.0',
    'category': 'Tools',
    'summary': 'Centralize agriculture field notebooks',
    'description': '''
    This module offers the possibility of centralize agriculture field notebooks
''',
    'license': 'AGPL-3',
    'author': 'Xtendoo',
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/field_notebook_crop_view.xml',
        'views/field_notebook_variety_view.xml',
        'views/field_notebook_plot_use_view.xml',
        'views/field_notebook_vulnerable_zone_view.xml',
        'views/field_notebook_parcel_view.xml',
        'views/field_notebook_exploitation_view.xml',
        'views/field_notebook_technical_view.xml',
        'views/field_notebook_enclosure_view.xml',
        'views/axdoo_field_notebook_view.xml',
    ],
    'application': True,
}
