# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA - Damien Crier, Alexandre Fayolle
# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# Copyright 2017 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Purchase order lines with sequence number',
    'summary': 'Adds sequence to PO lines and propagates it to'
               'Invoice lines and Stock Moves',
    'version': '10.0.1.0.1',
    'category': 'Purchase Management',
    'author': "Camptocamp, "
              "Eficent, "
              "Serpent CS, "
              "Odoo Community Association (OCA)",
    'website': 'http://www.camptocamp.com',
    'depends': [
        'purchase', 'stock_picking_line_sequence',
    ],
    'data': ['views/purchase_view.xml',
             'views/report_purchaseorder.xml',
             'views/report_purchasequotation.xml'],
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'auto_install': False,
    'license': "AGPL-3",
}
