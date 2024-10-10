# -*- coding: utf-8 -*-
{
    'name': 'Edicion_facturav16',
    'version': '16.2',
    'license': 'AGPL-3',
    'author': 'Demsa Industrial',
    'website': '',
    'depends': [
        'account_accountant','account', 'account_payment', 'l10n_mx_edi',


    ],
    'data': [
        # security
        'security/ir.model.access.csv',
        # data
        # demo
        # reports
        # views
        'views/account_move.xml',
        'views/multi_payment_views.xml',
        'wizards/multi_payments.xml',

    ],
    'license': 'LGPL-3',
}
