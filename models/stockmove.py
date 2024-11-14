
from odoo import models, fields, api
class Stockmovereport(models.Model):
    """ Manufacturing Orders """
    _inherit = 'stock.move'
    no_lot=fields.Many2one(
        related='active_move_line_ids.lot_id',
        string='No Lot'
    )