# -*- coding: utf-8 -*-
# from odoo import http


# class EventPublic(http.Controller):
#     @http.route('/event_public/event_public/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/event_public/event_public/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('event_public.listing', {
#             'root': '/event_public/event_public',
#             'objects': http.request.env['event_public.event_public'].search([]),
#         })

#     @http.route('/event_public/event_public/objects/<model("event_public.event_public"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('event_public.object', {
#             'object': obj
#         })
