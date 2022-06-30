# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class MRPProductionInherit(models.Model):

    _inherit = "mrp.production"

    def action_generate_serial(self):

        lot_number_prefix = (
            self.env["product.template"]
            .search([("id", "=", self.product_tmpl_id.id)])
            .lot_number_prefix
        )

        if lot_number_prefix:

            self.ensure_one()
            self.lot_producing_id = self.env["stock.production.lot"].create(
                {
                    "product_id": self.product_id.id,
                    "company_id": self.company_id.id,
                    "name": self.env["product.template"]
                    .search([("id", "=", self.product_tmpl_id.id)])
                    .lot_number_prefix
                    + self.env["ir.sequence"].next_by_code("stock.lot.serial"),
                }
            )

            if self.move_finished_ids.filtered(
                lambda m: m.product_id == self.product_id
            ).move_line_ids:
                self.move_finished_ids.filtered(
                    lambda m: m.product_id == self.product_id
                ).move_line_ids.lot_id = self.lot_producing_id
            if self.product_id.tracking == "serial":
                self._set_qty_producing()

        else:

            super(MRPProductionInherit, self).action_generate_serial()
