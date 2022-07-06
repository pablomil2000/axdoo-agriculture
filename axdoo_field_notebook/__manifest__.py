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
        'views/axdoo_field_notebook_view.xml',
    ],
    'application': True,
}
