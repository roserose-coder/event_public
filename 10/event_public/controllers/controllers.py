from odoo import http
from odoo.http import request
import werkzeug


class Main(http.Controller):
    @http.route('/event_survey', type='http', auth="public", website=True)
    def books_issues(self, **post):
        if post.get('event_id'):
            event_id = int(post.get('event_id'))
            rate = int(post.get('star'))
            name = post.get('name')
            address = post.get('address')
            desc = post.get('description')
            request.env['event_public.model_event.rating'].sudo().create({
                'event_id': event_id,
                'rate': rate,
                'name': name,
                'address': address,
                'description': desc,

            })

            test = '/event_survey?submitted=' + str(post.get('star'))
            return request.redirect(test)

        return request.render('event_public.event_form_templates', {
            'events': request.env['event_public.model_event'].search([]),
            'submitted': post.get('submitted', False)
        })

    @http.route('/event', type='http', auth="public", website=True)
    def books_issuess(self, **post):
        return request.render('event_public.event_list', {
            'events': request.env['event_public.model_event'].search(request.website.website_domain()),
        })
