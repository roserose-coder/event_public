from odoo import models, fields, api


class model_event(models.Model):
    _name = 'event_public.model_event'
    _description = 'event_public.model_event'

    _inherit = ['base.archive', 'mail.thread', 'mail.activity.mixin', 'image.mixin', 'website.multi.mixin']
    image_1920 = fields.Image('Event Image')
    event_name = fields.Char('Event Name')
    description = fields.Html('Description')
    start_time = fields.Date(default=fields.Date.today)
    end_time = fields.Date(default=fields.Date.today)
    speaker = fields.Many2many('res.users', string="Speaker")

    attendance = fields.Many2many('res.partner', string="Attendance")

    attendance_count = fields.Integer("Attendance Count")

    company_id = fields.Many2one('res.company', default=lambda self: self.env.user.company_id)
    rates = fields.One2many('event_public.model_event.rating', 'event_id')

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

    @api.model
    def get_partner_from_group(self, group_id):
        users_ids = []
        partners_ids = []
        sql_query = """select uid from res_groups_users_rel where gid = %s"""
        params = (group_id,)
        self.env.cr.execute(sql_query, params)
        results = self.env.cr.fetchall()
        for users_id in results:
            partners_ids.append(self.env['res.users'].browse(users_id[0]).partner_id.id)

            # users_ids.append(users_id[0])
        # return users_ids
        return partners_ids

    @api.model
    def get_user_from_group(self, group_id):
        users_ids = []
        sql_query = """select uid from res_groups_users_rel where gid = %s"""
        params = (group_id,)
        self.env.cr.execute(sql_query, params)
        results = self.env.cr.fetchall()
        for users_id in results:
            users_ids.append(users_id[0])
        return users_ids

    @api.model
    def create(self, vals):
        res = super(model_event, self).create(vals)

        if vals.get('stage_id') == 3 or vals.get('stage_id') == 4:
            if not self.user_has_groups('event_public.group_head_of_event'):
                raise models.ValidationError(
                    'Error! you are not allowed to change the status into rejected or accepted ! Director only.')

        domain = [('model', '=', 'res.groups'), ('name', '=', 'group_head_of_event')]
        model_data = self.env['ir.model.data'].search(domain, limit=1)
        staff = self.get_partner_from_group(model_data.res_id)
        staff_userid = self.get_user_from_group(model_data.res_id)
        res.message_subscribe(partner_ids=staff)
        if res.start_time:
            for user_id in staff_userid:
                res.activity_schedule('mail.mail_activity_data_meeting', user_id=user_id, date_deadline=res.start_time,
                                      summary='there is an event need to be checked')

        res.message_post_with_view('event_public.director_event_notif_qweb')
        return res

    def write(self, vals):
        res = super(model_event, self).write(vals)

        if vals.get('stage_id') == 3 or vals.get('stage_id') == 4:
            if not self.user_has_groups('event_public.group_head_of_event'):
                raise models.ValidationError(
                    'Error! you are not allowed to change the status into rejected or accepted ! Director only.')

        return res

    def _check_overdue(self):

        recs = self.env['event_public.model_event'].search([('start_time', '=', fields.Date.today())])
        for rec in recs:
            rec.write({'stage_id': 3})


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


class model_event_rating(models.Model):
    _name = 'event_public.model_event.rating'
    event_id = fields.Many2one('event_public.model_event', string="Event Name")
    rate = fields.Integer('Rate')
    description = fields.Text('Description')
    name = fields.Char('Name')
    address = fields.Text('Address')
