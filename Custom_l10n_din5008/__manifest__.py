# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Custom DIN 5008',
    'version': '18.0',
    'description' : "Custom Module defines the DIN5008 standard.",
    'depends': ['account', 'l10n_din5008','sale_management'],
    'data': [
        'report/minimal_layout.xml',
        'report/din5008_report.xml',
        "views/sale_view.xml",
        "views/report_saleorder.xml",
        "views/account_move_view.xml",
        "views/report_invoice.xml"
    ],
    'license': 'LGPL-3',
}
