from odoo import models, fields, api


class ResPartner(models.Model):

    _inherit = ['res.partner']

    event_id= fields.Many2many('event_public.model_event',string="Listed Events")