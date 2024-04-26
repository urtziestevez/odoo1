{
    'name': 'Disc Management',
    'category': 'Ocio',
    'summary': 'Disc Management',
    'version': '16.0.1.0.0',
    'author': 'Soluciones Tecnológicas Freedoo',
    'website': 'https://www.freedoo.es',
    'description': """
        Este módulo se encarga de la gestión de discos 
        """,
    'depends': [
        'base',
    ], 
    'data': [
        'security/ir.model.access.csv',
        'views/disc_management_view.xml',
    ],
    
    'installable': True,
    'application': True,
    'auto_install': False,
}