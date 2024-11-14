
from odoo import models, fields

class Persiapan(models.Model):
    _name = 'mrp.persiapan'
    _description = 'A. Line Clearance dan Persiapan'

    shift = fields.Selection([
        ('1', 'Shift 1'),
        ('2', 'Shift 2'),
        ('3', 'Shift 3')],default ='1',string='Shift Produksi',
        help="pilihan shift kerja operator")
    suhu = fields.Integer(string="Suhu Celcius")
    kelembaban = fields.Integer(string="Kelembaban RH%")
    mrp_id = fields.Many2one('mrp.production', string="MRP Production")