
from odoo import models, fields, api


class model_event(models.Model):
    _name = 'event_public.model_event'
    _description = 'event_public.model_event'

    event_image = fields.Image('Event Image')
    event_name = fields.Char('Event Name')
    description = fields.Html('Description')
    start_time = fields.Date(default=fields.Date.today)
    end_time = fields.Date(default=fields.Date.today)

    speaker = fields.Many2many('res.users', string="Speaker")

    attendance = fields.Many2many('res.partner', string="Attendance")
