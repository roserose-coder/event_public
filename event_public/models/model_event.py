from odoo import models, fields, api


class model_event(models.Model):
    _name = 'event_public.model_event'
    _description = 'event_public.model_event'

    _inherit = ['mail.thread', 'mail.activity.mixin']
    event_name = fields.Char('Event Name')
    description = fields.Html('Description')
    start_time = fields.Datetime(default=fields.Datetime.now)
    end_time = fields.Datetime(default=fields.Datetime.now)
    speaker = fields.Many2many('res.users', string="Speaker")

    def _default_program_stage(self):
        Stage = self.env['event_public.model_event_stage']
        return Stage.search([], limit=1)

    @api.model
    def _group_expand_stages(self, stages, domain, order):
        return stages.search([], order=order)

    stage_id = fields.Many2one(
        'event_public.model_event_stage',
        default=_default_program_stage,
        group_expand='_group_expand_stages'
    )


class model_event_stage(models.Model):
    _name = 'event_public.model_event_stage'
    _description = 'event_public.model_event_stage'
    name = fields.Char()
    sequence = fields.Integer()
    fold = fields.Boolean()
    status = fields.Selection(
        [('-1', 'Preparation'),
         ('0', 'Pending'),
         ('1', 'Accepted'), ('-2', 'Rejected')],
        'State', default='-1')
