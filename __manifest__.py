# -*- coding: utf-8 -*-
{
    'name': "mbf_report_mo",

    'summary': """
        Module tambahan report Manufacture Order catatan pengolahan no lot
        
        """,

    'description': """
        Module tambahan report Manufacture Order catatan pengolahan no lot
    """,

    'author': "Fikri Software",
    'website': "http://www.fikrisoftware.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mrp','base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}