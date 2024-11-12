# models/mrp_rekap_produksi.py

from odoo import models, fields

class MrpRekapProduksi(models.Model):
    _name = 'mrp.rekap.produksi'
    _description = 'MRP Rekap Produksi'

    jam_mulai = fields.Datetime(string="Jam Mulai")
    jam_selesai = fields.Datetime(string="Jam Selesai")
    awal = fields.Integer(string="Awal")
    akhir = fields.Integer(string="Akhir")
    produk_jadi = fields.Integer(string="Jumlah Produk Jadi")
    reject = fields.Integer(string="Jumlah Reject")
    reject_kemas = fields.Integer(string="Reject Kemas Bahan Kemas(pcs)")
    sample = fields.Integer(string="Jumlah Sampel QC")
    mrp_id = fields.Many2one('mrp.production', string="MRP Production")
