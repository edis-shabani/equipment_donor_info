{
    'name': 'Equipment Donor Info',
    'version': '1.0',
    'summary': 'Adds a "Donor" dropdown field to the equipment view in the maintenance module',
    'description': 'This module enhances the Odoo maintenance module by adding a "Donor" dropdown field to the equipment view. This new field allows users to specify the organization that donated each piece of equipment.',
    'author': 'VAMED',
    'depends': ['base', 'maintenance'],
    'data': [
        'views/equipment_views.xml',
    ],
    'installable': True,
    'application': False,
    'images': ['static/description/icon.png'],
}
