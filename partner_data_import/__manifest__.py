# -*- coding: utf-8 -*-
{
    'name': "PARTNER DATA IMPORT",
    'summary': """
        Manage data import
        """,
    'description': """
        Manage data import
    """,
    'author': "KASIA",
    'website': "https://www.kasia.mg",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'portal', 'point_of_sale'],

    # always loaded
    'assets': {
        'point_of_sale.assets': [
            'partner_data_import/static/src/js/models.js',
        ],
        'web.assets_qweb': [
            'partner_data_import/static/src/xml/*',
        ],
    },
    'data': [
        # 'security/ir.model.access.csv',
        'views/portal_template.xml',
        'views/res_partner_views.xml',
        'views/sale_report_views.xml'
    ]
}
