# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class StockPicking(models.Model):
    _name = 'stock.picking'
    _inherit = ['stock.picking', 'sync.document.status']

    customer_reference = fields.Char('Customer Reference')
    customer_expected_date = fields.Date('Customer Expected Date')

    shipping_collect_account = fields.Char('Shipping Collect Account', related='sale_id.shipping_collect_account')
    shipping_carrier = fields.Many2one(related='sale_id.shipping_carrier')
    shipping_billing_code = fields.Char(related='sale_id.shipping_billing_code')
    ship_priority = fields.Selection(string="Shipping Priority", related='sale_id.ship_priority', readonly=False)
    warehouse_instructions = fields.Text(related='sale_id.warehouse_instructions', readonly=False)
    warehouse_instructions_edi = fields.Text('Borderworx Notes', compute="_compute_warehouse_instructions", readonly=False, store=True)

    @api.depends('shipping_collect_account','ship_priority','warehouse_instructions')
    def _compute_warehouse_instructions(self):
        priorities = dict(self.sale_id._fields['ship_priority'].selection)
        for picking in self:
            picking.warehouse_instructions_edi = ''
            if picking.ship_priority:
                picking.warehouse_instructions_edi = picking.warehouse_instructions_edi + f"Priority: {priorities[picking.ship_priority]}\n"
            if picking.shipping_collect_account:
                picking.warehouse_instructions_edi = picking.warehouse_instructions_edi + f"Shipping Collect Account: {picking.shipping_collect_account}\n"
            if picking.warehouse_instructions:
                picking.warehouse_instructions_edi = picking.warehouse_instructions_edi + f"Warehouse Instructions: {picking.warehouse_instructions}"


    # -- Manual EDI Import/Export --------------------------------------

    def export_pickings_to_edi(self):
        self.export_delivery_orders_to_edi()
        self.export_receipts_to_edi()
        return True
    
    @api.model
    def import_pickings_from_edi(self):
        active_ids = self._context.get('active_ids', [])
        if active_ids:
            picking_types = self.env['stock.picking'].browse(active_ids).mapped('picking_type_code')
        else:
            picking_types = ['outgoing','incoming']
        if 'outgoing' in picking_types:
            self.import_delivery_orders_from_edi()
        if 'incoming' in picking_types:
            self.import_receipts_from_edi()

    # -- EDI Sync Actions ----------------------------------

    def export_delivery_orders_to_edi(self):
        records = self.filtered(lambda p: p.picking_type_code == 'outgoing' \
                                            and p.state == 'assigned')
        if not self._context.get('force_export', False):
            records = records.filtered(lambda p: p.edi_status == 'pending')
        return self._execute_edi_sync('export_delivery_order', records) if records else True
 
    @api.model
    def import_delivery_orders_from_edi(self):
        return self._execute_edi_sync('import_confirm_delivery_order')

    def export_receipts_to_edi(self):
        records = self.filtered(lambda p: p.picking_type_code == 'incoming' \
                                            and p.state == 'assigned')
        if not self._context.get('force_export', False):
            records = records.filtered(lambda p: p.edi_status == 'pending')
        return self._execute_edi_sync('export_receipt', records) if records else True

    @api.model
    def import_receipts_from_edi(self):
        return self._execute_edi_sync('import_confirm_receipt')

    # -- Automatic Export --------------------------------

    @api.depends('move_type', 'immediate_transfer', 'move_lines.state', 'move_lines.picking_id')
    def _compute_state(self):
        ''' When orders becomes ready, export 940/943 EDI document. '''
        res = super()._compute_state()
        self.with_context(ignore_edi_errors=True).export_delivery_orders_to_edi()
        self.with_context(ignore_edi_errors=True).export_receipts_to_edi()
        return res
