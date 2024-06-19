from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    bom_ids = fields.Many2many(
        comodel_name='mrp.bom',
        relation='sale_order_bom_rel',
        column1='sale_order_id',
        column2='bom_id',
        string='เพิ่ม BOMs (Bill Of Matts.) ครับ'
    )