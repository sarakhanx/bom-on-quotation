{
    'name': 'Custom BOM in Sale Order',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'เพิ่มข้อมูล BoM ใน Quotation.',
    'author': 'Sarawut Khantiyoo',
    'license': 'AGPL-3',
    'website': 'https://www.example.com',
    'depends': ['base', 'sale', 'mrp'],
    'data': [
        'views/quotation_bom.xml',
        'views/quotation_report_inherit.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
