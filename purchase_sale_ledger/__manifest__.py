{
    'name' : 'Sale & Purchase Ledger',
    'version': '1.0',
    'category': 'Account',
    'complexity': 'easy',
    'description': "It has to differ VAT taxes from all other taxes.",
    'depends': ['account','td_generico_gt'],
    'data': [
        'views/document_type_view.xml',
        'security/ir.model.access.csv',
        'wizard/sale_purchase_report_wiz.xml',
        'report/sale_po_ledger_report.xml',
        'report/report_sale_purchase_ledger.xml',

    ],
    'installable': True,
}
