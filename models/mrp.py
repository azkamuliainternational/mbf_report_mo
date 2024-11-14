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
    shift = fields.Selection([
        ('1', 'Shift 1'),
        ('2', 'Shift 2'),
        ('3', 'Shift 3')],default ='1',string='Shift Produksi',
        help="pilihan shift kerja operator")
    umur_produk = fields.Selection([
        ('1', '1 Tahun'),
        ('2', '2 Tahun'),
        ('3', '3 Tahun'),
        ('4', '4 Tahun'),
        ('5', '5 Tahun')        
        ],default ='3',string='Umur Produk',
        help="Umur Produk")
    rekap_ids = fields.One2many('mrp.rekap.produksi', 'mrp_id',
        string="Rekapitulasi Produksi")
    persiapan_ids = fields.One2many('mrp.persiapan', 'mrp_id',
        string="Persiapan Produksi")
    proses_produksi_ids = fields.One2many('mrp.proses_produksi', 'mrp_id',
        string="Persiapan Produksi")
    
    nie = fields.Char(
        related='product_tmpl_id.hs_code',
        string='NIE'
    )
    nama_mesin = fields.Char(
                string='Nama Mesin'
    )
    nama_operator = fields.Char(
                string='Nama Operator'
    )

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