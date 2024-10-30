# models/equipment.py
from odoo import models, fields

class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    donor = fields.Selection([
        ('mcc', 'MCC'),
        ('pepfar', 'PEPFAR'),
        ('icap', 'ICAP'),
        ('vamed', 'VAMED')
    ], string="Donor")
