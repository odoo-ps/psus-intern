from odoo import fields, models, api

class SaleOrderInherit(models.Model):

    _inherit = "sale.order"
    job_number = fields.Char(string="Job Number", required=False, readonly = True, compute ="_compute_job_number")
    plant_number = fields.Char(string="Plant Code", required=False, readonly = True)
    job_number_sequence = fields.Char(string="Job Number Sequence", default="00001")
    plant_number_sequence = fields.Char(string="Plant Number Sequence")


    @api.model
    def create(self, vals):
        job_number_sequence_id = self.env['ir.sequence'].search([('code', '=', 'sequence.order')])[0]
        vals["job_number_sequence"] = job_number_sequence_id.number_next_actual
        self.env['ir.sequence'].next_by_code('sequence.order')
        return super(SaleOrderInherit,self).create(vals)

    @api.model
    def action_confirm(self):
        if self._get_forbidden_state_confirm() & set(self.mapped('state')):
            raise UserError(_(
                'It is not allowed to confirm an order in the following states: %s'
            ) % (', '.join(self._get_forbidden_state_confirm())))
        # Added following two lines.
        plant_number = self.getPlantNumberPrefix() + self.getNextPlantNumberSequence()
        self.write({"name" : plant_number})
        #
        for order in self.filtered(lambda order: order.partner_id not in order.message_partner_ids):
            order.message_subscribe([order.partner_id.id])
        self.write(self._prepare_confirmation_values())

        # Context key 'default_name' is sometimes propagated up to here.
        # We don't need it and it creates issues in the creation of linked records.
        context = self._context.copy()
        context.pop('default_name', None)

        self.with_context(context)._action_confirm()
        if self.env.user.has_group('sale.group_auto_done_setting'):
            self.action_done()
        return True

    @api.onchange('x_studio_prefix','x_studio_suffix','job_number_sequence')
    def _on_change_compute_job_number(self):
        if self._origin.id:
            job_number = f'{self.x_studio_prefix if self.x_studio_prefix else ""}{self.job_number_sequence}{self.x_studio_suffix if self.x_studio_suffix else ""}'
            self.write({'job_number': job_number})
        else:
            job_number_sequence_id = self.env['ir.sequence'].search([('code', '=', 'sequence.order')])[0]
            self.write({"job_number_sequence": job_number_sequence_id.number_next_actual})


    @api.depends('x_studio_prefix','x_studio_suffix')
    def _compute_job_number(self):
        job_number = f'{self.x_studio_prefix if self.x_studio_prefix else ""}{self.job_number_sequence}{self.x_studio_suffix if self.x_studio_suffix else ""}'
        self.write({'job_number': job_number})

    def getPlantNumberPrefix(self):

        company_name = ""
        plant_number_prefix = ""

        if self.partner_id.is_company:
            company_name = self.partner_id.name
        else:
            if self.partner_id.parent_name:
                company_name = self.partner_id.parent_name
            else:
                company_name = self.partner_id.name

        for char in company_name:
            if char.isalpha():
                plant_number_prefix += char
            if len(plant_number_prefix) == 3:
                break

        return plant_number_prefix.upper()

    def getNextPlantNumberSequence(self):
        sequence_plant_iteration = self.env['ir.sequence'].search([('code', '=', 'sequence.plant_iteration')])[0]
        sequence_plant = self.env['ir.sequence'].search([('code', '=', 'sequence.plant')])[0]
        if sequence_plant.number_next_actual == 100:
            sequence_plant.write({'number_next_actual': 1})
            self.env['ir.sequence'].next_by_code('sequence.plant_iteration')
        sequence_plant_iteration_char = sequence_plant_iteration.get_next_char(sequence_plant_iteration.number_next_actual)
        sequence_plant_char = sequence_plant.get_next_char(sequence_plant.number_next_actual)
        self.env['ir.sequence'].next_by_code('sequence.plant')
        plant_number = sequence_plant_iteration_char + "-" + sequence_plant_char
        return plant_number






