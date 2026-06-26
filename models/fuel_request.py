from odoo import models, fields, api


class FuelRequest(models.Model):
    _name = 'fuel.request'
    _description = 'Demande de carburant'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    reference = fields.Char(string="Référence", readonly=True, copy=False, default="Nouveau")
    customer_id = fields.Many2one('res.partner', string="Client", required=True)
    request_date = fields.Date(string="Date de la demande", default=fields.Date.context_today)
    fuel_type = fields.Selection([
        ('essence', 'Essence'),
        ('gasoil', 'Gasoil'),
    ], string="Type de carburant", required=True)
    quantity = fields.Float(string="Quantité", required=True)
    currency_id = fields.Many2one('res.currency', string="Devise",
                                   default=lambda self: self.env.company.currency_id)
    unit_price = fields.Monetary(string="Prix unitaire", currency_field='currency_id')
    total_amount = fields.Float(string="Montant total", compute='_compute_total_amount', store=True)
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('submitted', 'Soumis'),
        ('approved', 'Approuvé'),
        ('rejected', 'Rejeté'),
    ], string="État", default='draft', required=True, tracking=True)
    notes = fields.Text(string="Remarques")

    @api.depends('quantity', 'unit_price')
    def _compute_total_amount(self):
        for record in self:
            record.total_amount = record.quantity * record.unit_price

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('reference', 'Nouveau') == 'Nouveau':
                vals['reference'] = self.env['ir.sequence'].next_by_code('fuel.request') or 'Nouveau'
        return super().create(vals_list)

    def action_submit(self):
        for record in self:
            record.state = 'submitted'

    def action_approve(self):
        for record in self:
            record.state = 'approved'

    def action_reject(self):
        for record in self:
            record.state = 'rejected'

    def action_reset_to_draft(self):
        for record in self:
            record.state = 'draft'
