# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleReport(models.Model):
    _inherit = 'sale.report'

    badge = fields.Selection(
        [('water', 'Waterman/women'), ('king', 'Roi/reine du sport'), ('undefined', '')], string="Badge", readonly=True)

    def _select_sale(self, fields):
        return super(SaleReport, self)._select_sale(fields) + ", partner.badge as badge"

    def _group_by_sale(self, groupby):
        return super(SaleReport, self)._group_by_sale(groupby) + ", partner.badge"

    def _select_pos(self, fields):
        return super(SaleReport, self)._select_pos(fields) + ", partner.badge as badge"

    def _group_by_pos(self):
        return super(SaleReport, self)._group_by_pos() + ", partner.badge"

    # def _query(self, with_clause='', fields=None, groupby='', from_clause=''):
    #     if fields is None:
    #         fields = {}
    #     fields['badge'] = ", partner.badge"
    #     groupby += ', partner.badge'
    #     return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)
