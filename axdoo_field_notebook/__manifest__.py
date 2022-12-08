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
        'mrp',
        'maintenance',
        'hr',
        'account',
        'web_domain_field',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/field_notebook_campaign_view.xml',
        'views/field_notebook_crop_view.xml',
        'views/field_notebook_labor_view.xml',
        'views/field_notebook_harvest_view.xml',
        'views/field_notebook_phytosanitary_view.xml',
        'views/field_notebook_phytosanitary_application_type_view.xml',
        'views/field_notebook_autonomy_view.xml',
        'views/field_notebook_town_view.xml',
        'views/field_notebook_province_view.xml',
        'views/field_notebook_variety_view.xml',
        'views/field_notebook_plot_use_view.xml',
        'views/field_notebook_zone_view.xml',
        'views/field_notebook_system_view.xml',
        'views/field_notebook_irrigation_view.xml',
        'views/field_notebook_irrigation_system_view.xml',
        'views/field_notebook_ucth_view.xml',
        'views/field_notebook_parcel_view.xml',
        'views/field_notebook_exploitation_view.xml',
        'views/field_notebook_enclosure_view.xml',
        'views/field_notebook_agent.xml',
        'views/res_partner_view.xml',
        'views/maintenance_view.xml',
        'views/res_config_settings_views.xml',
        'views/axdoo_field_notebook_view.xml',
        'views/product_template_view.xml',
        'data/field_notebook_data.xml',
        'data/field_notebook_agent_data.xml',
        'data/field_notebook_demo_data.xml',
        'data/field_notebook_crop_data.xml',
        'data/field_notebook_product_data.xml',
    ],
    'application': True,
}
