# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    currency_id = fields.Many2one('res.currency', string='Currency')
    old_sales_values = fields.Monetary(string='Ancien solde')
    sales_values = fields.Monetary(compute="_compute_sales_values", store=True, string="CA TTC")
    old_sales_count = fields.Integer(string='Ancien nombre de ventes')
    sales_count = fields.Integer(string="Nombre de ventes", compute="_compute_sales_count", store=True,)
    badge = fields.Selection(
        [('water', 'Waterman/women'), ('king', 'Roi/reine du sport'), ('undefined', '')], string="Badge",
        compute="_compute_badge", store=True, default='undefined')
    sale_order_ids = fields.One2many('sale.order', 'partner_id')
    pos_order_ids = fields.One2many('pos.order', 'partner_id')

    def get_pos_order(self, partner_id):
        PosOrder = self.env['pos.order']
        return PosOrder.search([('partner_id', '=', partner_id), ('state', 'in', ['paid', 'done', 'invoiced'])])

    def get_sale_order(self, partner_id):
        SaleOrder = self.env['sale.order']
        return SaleOrder.search([('partner_id', '=', partner_id), ('state', 'in', ['sale', 'done'])])

    @api.depends("old_sales_values", "sale_order_ids", "pos_order_ids")
    def _compute_sales_values(self):
        for rec in self:
            rec.sales_values = rec.old_sales_values + sum(rec.pos_order_ids.mapped('amount_total')) + \
                               sum(rec.sale_order_ids.mapped('amount_total'))

    @api.depends("old_sales_count", "sale_order_ids", "pos_order_ids")
    def _compute_sales_count(self):
        for rec in self:
            rec.sales_count = rec.old_sales_count + len(rec.pos_order_ids) + len(rec.sale_order_ids)

    @api.depends("old_sales_values", "sale_order_ids", "pos_order_ids")
    def _compute_badge(self):
        for rec in self:
            rec.sales_values = rec.old_sales_values + sum(rec.sale_order_ids.mapped('amount_total')) + \
                               sum(rec.pos_order_ids.mapped('amount_total'))
            if rec.sales_values >= 10000:
                rec.badge = 'king'
            elif rec.sales_values > 3000:
                rec.badge = 'water'
            else:
                rec.badge = 'undefined'
