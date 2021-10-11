from odoo import models, fields, api


class Digest(models.Model):
    _inherit = 'digest.digest'

    kpi_event = fields.Boolean('Created Event')
    kpi_event_value = fields.Integer(compute='_compute_kpi_event_value')

    def _compute_kpi_event_value(self):
        for record in self:
            start, end, company = record._get_kpi_compute_parameters()
            record.kpi_event_value = self.env['event_public.model_event'].search_count([
                ('create_date', '>=', start),
                ('create_date', '<', end),
                ('company_id', '=', company.id)
            ])
