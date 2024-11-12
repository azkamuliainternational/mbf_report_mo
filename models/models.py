# -*- coding: utf-8 -*-

from odoo import models, fields, api
class MrpProduction(models.Model):
    """ Manufacturing Orders """
    _inherit = 'mrp.production'
    no_lot_mo = fields.Many2one(
        comodel_name='stock.production.lot',
        string='No Lot',
        related='finished_move_line_ids.lot_id',
        store=True,  # Optional: Set to True if you want the field value to be stored in the database
        readonly=False  # Optional: Set to False if you want users to be able to edit this field manually
    )
    shift = fields.Char(
        'Shift',
        help="Reference of the document that generated this production order request.")

# class ./(models.Model):
#     _name = './../'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100