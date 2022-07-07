# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import os
import tempfile
from datetime import datetime
from dateutil import parser, tz

from lxml import etree as ET
from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class SyncDocumentType(models.Model):
    _inherit = "sync.document.type"

    doc_code = fields.Selection(
        selection_add=[
            ("export_delivery_order", "940 - Warehouse Shipping Order"),
            ("export_receipt", "943 - Warehouse Stock Transfer Shipment Advice"),
            ("import_confirm_receipt", "944 - Warehouse Stock Transfer Receipt Advice"),
            ("import_confirm_delivery_order", "945 - Warehouse Shipping Advice"),
            ("import_request_inventory", "846 - Inventory Inquiry/Advice")
        ],
        ondelete={
            "export_delivery_order": "cascade",
            "export_receipt": "cascade",
            "import_confirm_receipt": "cascade",
            "import_confirm_delivery_order": "cascade",
            "import_request_inventory": "cascade"
        },
    )


    # ===============================
    # Shared XML Export for 940/943 |
    # ===============================

    def _export_edi(self, conn, sync_action_id, values, model_name, search_domain, get_xml_func):
        conn._connect()
        conn.cd(sync_action_id.dir_path)
        records = values.get('records', self.env[model_name].search(search_domain or []))
        for record in records:
            xml = get_xml_func(record)
            export_file_path, filename, tmp_dir = self.write_xml_file(xml, f"{record.name.replace('/','_')}.xml")

            #conn._conn.put(export_file_path, os.path.join(sync_action_id.dir_path, filename)) #throws an error when user uses FTP (put() does not exist)
            contents = open(export_file_path, mode="rb")
            conn.mkf(os.path.join(sync_action_id.dir_path, filename), contents) #FTPConnection.mkf() instead of calling storbinary ourselves
            ## *****************************************

            _logger.info('Writing xml file %s' % filename)
            os.remove(export_file_path)
            os.rmdir(tmp_dir)
            record.write({
                "edi_status": 'sent',
                "edi_sync_time": datetime.now()
            })
            if hasattr(record, 'message_post'):
                record.message_post(body="EDI file exported: %s" % filename)
        conn._disconnect()
        return True

    def write_xml_file(self, xml, filename):
        parser = ET.XMLParser(remove_blank_text=True)
        tree = ET.fromstring(xml, parser=parser)
        formatted_xml = ET.tostring(tree, pretty_print=True)
        tmp_dir = tempfile.mkdtemp()
        filename = filename.strip()
        export_file_path = tmp_dir.rstrip("/") + "/" + filename
        with open(export_file_path, "wb") as file:
            file.write(formatted_xml)
        return export_file_path, filename, tmp_dir

    # ===================================
    # Shared XML Import for 944/945/846 |
    # ===================================

    def _import_xml(self, conn, sync_action_id, values, _root_processor): #downloading XMLs from the server and processing them

        conn._connect() #connect to server
        conn.cd(sync_action_id.dir_path) #go to the sync action's set directory path on the server
        files = conn.ls() #get list of files
        if not files:
            _logger.warning('Directory on host is empty')
        for file in files:
            if not (file.endswith('.xml') or file.endswith('.txt')): #ignore anything that's not xml or txt
                continue

            #temp_file = 'temp.xml'
            #conn._conn.get(file, temp_file) ## ************************* what does this line do????
            # -> downloads `file` from server and puts it in local `temp_file`

            #rewrote the below commented out code to use ftp_connection's download_file instead of get (same problem as put)

            file_content = conn.download_file(file)

            _logger.info('Importing EDI document %s' % file)
            root = ET.fromstring(file_content) #returns root element of the xml
            nsmap = root.nsmap #gets the namespace
            records = _root_processor(root, nsmap) #_root_processor is a processing function passed in and processes the individual records
            if records and "edi_status" in records._fields:
                records.write({
                    "edi_status": 'processed',
                    "edi_sync_time": datetime.now()
                })
                for record in records:
                    _logger.info(f'Updated record from EDI, {record}')
                    if hasattr(record, 'message_post'):
                        record.message_post(
                            author_id = self.env.ref('base.partner_root').id,
                            body=_("EDI file imported: %s", file)
                        )

            """

            with open(temp_file, 'rb') as file_data:
                _logger.info('Importing EDI document %s' % file)
                file_content = file_data.read()
                root = ET.fromstring(file_content)
                nsmap = root.nsmap
                records = _root_processor(root, nsmap)
                if records and "edi_status" in records._fields:
                    records.write({
                        "edi_status": 'processed',
                        "edi_sync_time": datetime.now()
                    })
                    for record in records:
                        _logger.info(f'Updated record from EDI, {record}')
                        if hasattr(record, 'message_post'):
                            record.message_post(
                                author_id = self.env.ref('base.partner_root').id,
                                body=_("EDI file imported: %s", file)
                            )
            """

            try:
                conn.rename(file, os.path.join(sync_action_id.dir_mv_path, file))
            except IOError as e:
                conn.mkd(sync_action_id.dir_mv_path)
                conn.rename(file, os.path.join(sync_action_id.dir_mv_path, file))
        conn._disconnect()
        return True

    # ================================
    # 940 - Warehouse Shipping Order |
    # ================================

    def _do_export_delivery_order(self, conn, sync_action_id, values):
        search_domain = [('edi_status', '=', 'pending'), 
                         ('picking_type_code', '=', 'outgoing'), 
                         ('state','=','assigned')]
        return self._export_edi(conn, sync_action_id, values, 'stock.picking', search_domain, self.get_delivery_xml)

    def get_delivery_xml(self, picking):
        return self.env.ref("edi_3pl_central.export_delivery_order_xml")._render({"picking": picking})

    # ================================================
    # 943 - Warehouse Stock Transfer Shipment Advice |
    # ================================================

    def _do_export_receipt(self, conn, sync_action_id, values):
        search_domain = [('edi_status', '=', 'pending'), 
                         ('picking_type_code', '=', 'incoming'), 
                         ('state','=','assigned')]
        return self._export_edi(conn, sync_action_id, values, 'stock.picking', search_domain, self.get_receipt_xml)

    def get_receipt_xml(self, picking):
        return self.env.ref("edi_3pl_central.export_receipt_xml")._render({"picking": picking})

    # ===============================================
    # 944 - Warehouse Stock Transfer Receipt Advice |
    # ===============================================

    def _do_import_confirm_receipt(self, conn, sync_action_id, values):
        return self._import_xml( conn, sync_action_id, values, self._process_transaction_list)

    # =================================
    # 945 - Warehouse Shipping Advice |
    # =================================

    def _do_import_confirm_delivery_order(self, conn, sync_action_id, values):
        return self._import_xml( conn, sync_action_id, values, self._process_transaction_list)

    # ================================
    # 846 - Inventory Inquiry/Advice |
    # ================================

    def _do_import_request_inventory(self, conn, sync_action_id, values):
        return self._import_xml( conn, sync_action_id, values, self.with_context(sync_action_id=sync_action_id)._process_total_inventory)

    # = Processors ==============================================
    # Called when importing XMLs

    def _process_total_inventory(self, root, nsmap = None):
        ''' stock.inventory '''
        nsmap = root.nsmap or nsmap
        document_id = root.find('DocumentId', namespaces=nsmap).text
        document_date = root.find('DocumentDate', namespaces=nsmap).text
        date = parser.parse(document_date).astimezone(tz.tzutc()).replace(tzinfo=None)
        inventory_values = []
        unknown_products = []
        for product in root.findall('StockStatusEntry', namespaces=nsmap):
            values = self._get_stock_inventory_values(product, nsmap)
            if values:
                inventory_values.append(values)
            else:
                unknown_sku = self._get_unknown_product(product, nsmap)
                if unknown_sku:
                    unknown_products.append(unknown_sku)
        InvAdjustment = self.env['stock.inventory']
        adjustment = InvAdjustment.create({
            'date': date,
            'name': document_id,
            'state': 'confirm',
            'line_ids': [(0,0,val) for val in (inventory_values or [])],
        })
        if unknown_products:
            sync_action_id = self._context.get('sync_action_id')
            if sync_action_id.config_id.activity_user_id:
                adjustment.message_post(
                    author_id = self.env.ref('base.partner_root').id,
                    partner_ids = [sync_action_id.config_id.activity_user_id.partner_id.id],
                    body = _('The following SKUs could not be found: %s',', '.join(unknown_products)),
                    subject = _('Tried to adjust stock for unknown SKUs'),
                )
        adjustment._action_done()
        return adjustment

    def _process_transaction_list(self, root, nsmap = None):
        ''' stock.picking '''
        nsmap = root.nsmap or nsmap
        pickings = self.env['stock.picking']
        for transaction in root:
            pickings += self._process_picking_transaction(transaction, nsmap)
        pickings._action_done()
        return pickings
     
    def _process_picking_transaction(self, transaction, nsmap = None):
        ''' stock.picking '''
        nsmap = transaction.nsmap or nsmap
        picking_name = transaction.find('.//TransInfo/ReferenceNum', namespaces=nsmap).text
        picking = self.env['stock.picking']
        if picking_name:
            picking = picking.search([('name', '=', picking_name)],limit=1)
        if picking:
            picking_type_code = picking.picking_type_code
            # Read stock.picking
            shipping_values = {}
            if picking_type_code == 'outgoing':
                shipping_values = self._get_shipping_values(transaction)
                shipping_cost = self._get_shipping_cost(transaction)
                # Set cost on the sale order
                delivery_order_lines = picking.sale_id.order_line.filtered(lambda l: l.is_delivery)
                if delivery_order_lines:
                    delivery_order_lines[-1].price_unit = shipping_cost
            items_list = transaction.find('orderItems', namespaces=nsmap) if picking_type_code == 'outgoing' else transaction.find('ReceiveItems', namespaces=nsmap)
            move_line_vals = [
                self._get_move_line_values(order_line, picking, nsmap)
                for order_line in items_list
            ]

            picking.write({
                **shipping_values,
                'move_line_ids': [(0,0,vals) for vals in move_line_vals if vals]
            })
        return picking

    # = Finders ==============================================

    def _find_product(self, node, nsmap = None):
        product_sku = self._get_stock_status_entry_values(node, nsmap)
        return self.env['product.product'].search([('default_code','ilike',product_sku)],limit=1) if product_sku else self.env['product.product']

    def _find_location(self, node, nsmap = None):
        nsmap = node.nsmap or nsmap
        location = self.env['stock.location']
        location_id_node = node.find('LocationID', namespaces=nsmap)
        external_location_id = int(location_id_node.text) if location_id_node is not None else 0
        if external_location_id:
            location = self.env['stock.location'].search([('external_id','=',external_location_id)], limit=1)
        if not location:
            location_name_node = node.find('Location', namespaces=nsmap)
            external_location_name = location_name_node.text if location_name_node is not None else 0
            if external_location_name:
                location = self.env['stock.location'].search([('external_name','ilike',external_location_name)], limit=1)
        if not location:
            location_id_node = node.find('FacilityID', namespaces=nsmap)
            external_location_id = int(location_id_node.text) if location_id_node is not None else 0
            if external_location_id:
                location = self.env['stock.location'].search([('external_id','=',external_location_id)], limit=1)            
        return location

    def _find_move_line(self, node, nsmap=None):
        nsmap = node.nsmap or nsmap
        line = node.find('.//SavedElements/CodeDescrPair[Code="OdooStockMoveID"]/Description', namespaces=nsmap)
        move_id =  int(line.text) if line is not None else False
        return self.env['stock.move'].browse(move_id) if move_id else self.env['stock.move']

    # = Value Getters ==============================================

    def _get_shipping_values(self, transaction, nsmap = None):
        nsmap = transaction.nsmap or nsmap
        # Set tracking number
        carrier_tracking_ref = transaction.find('TrackingInfo/TrackingNumber', namespaces=nsmap).text if transaction.find('TrackingInfo/TrackingNumber', namespaces=nsmap) is not None else ''
        # Determine carrier
        carrier_name = transaction.find('ShippingInstructions/Carrier', namespaces=nsmap).text if transaction.find('ShippingInstructions/Carrier', namespaces=nsmap) is not None else ''
        carrier_id = False
        if carrier_name:
            carrier_id = self.env['delivery.carrier'].search([('name','ilike',carrier_name),('delivery_type','=','fixed')], limit=1)
        return {
            'carrier_tracking_ref': carrier_tracking_ref or '',
            'carrier_id': carrier_id,
        }

    def _get_shipping_cost(self, transaction, nsmap=None):
        nsmap = transaction.nsmap or nsmap
        # Compute total shipping cost
        costInfo = transaction.find('CostInfo', namespaces=nsmap)
        if costInfo is not None:
            return sum(float(line.text) for line in costInfo.getchildren() if line.text is not None)
        return 0

    def _get_move_line_values(self, order_line, picking = None, nsmap=None):
        nsmap = order_line.nsmap or nsmap
        # Determine stock.move
        move_line = self._find_move_line(order_line, nsmap)
        # Determine product.product
        product = move_line.product_id
        if not product:
            product = self._find_product(order_line, nsmap)
        # Determine stock.picking
        picking = picking or move_line.picking_id
        # Get qty_done
        qty_done_node = order_line.find('PrimaryInvQty', namespaces=nsmap) if picking.picking_type_code == 'outgoing' else order_line.find('OrigQtyPrimary', namespaces=nsmap)
        qty_done = float(qty_done_node.text) if qty_done_node is not None else 0
        # get location_id
        location = self._find_location(order_line, nsmap)
        # Create stock.move.line
        vals = {}
        if picking and product:
            vals = {
                'product_id': product.id,
                'product_uom_id': product.uom_id.id,
                'picking_id': picking.id,
                'qty_done': qty_done,
                'move_id': move_line.id,
                'location_id': picking.location_id.id,
                'location_dest_id': picking.location_dest_id.id
            }
            if location:
                vals['location_dest_id'] = location.id
        return vals

    def _get_stock_status_entry_values(self, node, nsmap = None):
        nsmap = node.nsmap or nsmap
        sku_tags = ['Sku', 'SKU']
        product_sku_node = None
        for tag in sku_tags:
            product_sku_node = node.find(tag, namespaces=nsmap)
            if product_sku_node is not None:
                break
        return product_sku_node.text if product_sku_node is not None else False

    def _get_stock_inventory_values(self, node, nsmap = None):
        ''' stock.inventory.line '''
        nsmap = node.nsmap or nsmap
        # Get location
        location = self._find_location(node, nsmap)
        # Get product
        product = self._find_product(node, nsmap)
        # Get quantities
        line = node.find('SumOfOnHand', namespaces=nsmap)
        qty = float(line.text) if line is not None else 0
        # 3PL splits StockStatusEntry into two if there is a negative qty available. 
        # We can ignore the entry that handles the overage since we should only have a
        # single stock adjustment line per product and we only care about qty on hand.
        line = node.find('OverOrdered', namespaces=nsmap)
        over_ordered = float(line.text) if line is not None else 0
        # Create stock.inventory.line 
        if location and product and over_ordered == 0:
            return {
                'location_id': location.id,
                'product_id': product.id,
                'product_qty': qty
            }
        return None

    def _get_unknown_product(self, node, nsmap = None):
        product = self._find_product(node, nsmap)
        return self._get_stock_status_entry_values(node, nsmap) if not product else ''
