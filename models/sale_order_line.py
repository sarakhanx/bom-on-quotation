from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    related_bom_ids = fields.Many2many(
        'mrp.bom',
        compute='_compute_related_bom_ids',
        string='Related BOMs'
    )

    @api.depends('order_id.bom_ids')
    def _compute_related_bom_ids(self):
        for line in self:
            line.related_bom_ids = line.order_id.bom_ids