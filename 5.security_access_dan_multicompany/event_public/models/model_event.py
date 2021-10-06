
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
    company_id = fields.Many2one('res.company', default=lambda self: self.env.user.company_id)
    # stage_id = fields.Selection([
    #     ('3', 'Rejected'),
    #     ('2', 'Accepted'),
    #     ('1', 'Pending'),
    #     ('0', 'Prepare'),
    # ],default='1')

    def write(self, vals):
        res = super(model_event, self).write(vals)

        if vals.get('stage_id') == 3 or vals.get('stage_id') == 4:
            if not self.user_has_groups('event_public.group_head_of_event'):
                raise models.ValidationError(
                    'Error! you are not allowed to change the status into rejected or accepted ! Director only.')

        return res

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

