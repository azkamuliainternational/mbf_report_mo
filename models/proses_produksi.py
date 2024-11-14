
from odoo import models, fields

class ProsesProduksi(models.Model):
    _name = 'mrp.proses_produksi'
    _description = 'A. Proses Produksi Black'

    shift = fields.Selection([
        ('1', 'Shift 1'),
        ('2', 'Shift 2'),
        ('3', 'Shift 3')],default ='1',string='Shift Produksi',
        help="pilihan shift kerja operator")
    speed = fields.Integer(string="Speed")    
    mrp_id = fields.Many2one('mrp.production', string="MRP Production")