# Creating a Custom Addon in Odoo to Add a Dropdown Field

This guide will help you create a custom addon in Odoo that adds an extra dropdown field in the equipment view of the maintenance module.

## Step-by-Step Guide

### 1. Set Up Your Development Environment
- Ensure you have Odoo installed and running.
- Activate developer mode in Odoo.

### 2. Create a New Module
- Navigate to your Odoo addons directory.
- Create a new directory for your custom module, e.g., `equipment_donor_info`.

### 3. Define the Module Structure
- Inside your module directory, create the following structure:
```
equipment_donor_info/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── equipment.py
├── views/
│   └── equipment_view.xml
└── static/
    └── description/
        └── icon.png
```

### 4. Edit `__manifest__.py`
- This file contains the module's metadata.
```python
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
```

### 5. Define the Model in `equipment.py`
- This file will define the new field in the equipment model.
```python
from odoo import models, fields

class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    donor = fields.Selection([
        ('mcc', 'MCC'),
        ('pepfar', 'PEPFAR'),
        ('icap', 'ICAP'),
        ('vamed', 'VAMED')
    ], string="Donor")
```
- Ensure your `__init__.py` file in the models directory imports the `equipment.py` file:
```python
from . import equipment
```

### 6. Create the View in `equipment_view.xml`
- This file will modify the equipment form view to include the new dropdown field.
```xml
<odoo>
    <record id="view_equipment_form_inherit" model="ir.ui.view">
        <field name="name">maintenance.equipment.form.inherit</field>
        <field name="model">maintenance.equipment</field>
        <field name="inherit_id" ref="maintenance.view_equipment_form"/>
        <field name="arch" type="xml">
            <xpath expr="//field[@name='name']" position="after">
                <field name="custom_dropdown"/>
            </xpath>
        </field>
    </record>
</odoo>
```

