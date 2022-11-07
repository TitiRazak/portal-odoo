# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    currency_id = fields.Many2one('res.currency', string='Currency')
    old_sales_values = fields.Monetary(string='Ancien solde')
    sales_values = fields.Monetary(compute="_compute_sales_values_badge", store=True, string="CA TTC")
    old_sales_count = fields.Integer(string='Ancien nombre de ventes')
    sales_count = fields.Integer(string="Nombre de ventes", compute="_compute_sales_values_badge", store=True, )
    badge = fields.Selection(
        [('water', 'Waterman/women'), ('king', 'Roi/reine du spot'), ('undefined', '')], string="Badge",
        compute="_compute_sales_values_badge", store=True, default='undefined')
    sale_order_ids = fields.One2many('sale.order', 'partner_id')
    pos_order_ids = fields.One2many('pos.order', 'partner_id')

    @api.depends("old_sales_values", "old_sales_count", "sale_order_ids", "pos_order_ids")
    def _compute_sales_values_badge(self):
        for rec in self:
            pos_order_ids = rec.pos_order_ids.filtered(lambda x: x.state in ['paid', 'done', 'invoiced'])
            sale_order_ids = rec.sale_order_ids.filtered(lambda x: x.state in ['sale', 'done'])
            sales_values = rec.old_sales_values + sum(pos_order_ids.mapped('amount_total')) + \
                           sum(sale_order_ids.mapped('amount_total'))
            sales_count = rec.old_sales_count + len(pos_order_ids) + len(sale_order_ids)
            badge = 'undefined'
            if sales_values >= 10000:
                badge = 'king'
            elif sales_values > 3000:
                badge = 'water'
            rec.write({
                'sales_values': sales_values,
                'badge': badge,
                'sales_count': sales_count
            })
