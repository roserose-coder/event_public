# -*- coding: utf-8 -*-
# from odoo import http


# class EventPublicRoomster(http.Controller):
#     @http.route('/event_public_roomster/event_public_roomster/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/event_public_roomster/event_public_roomster/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('event_public_roomster.listing', {
#             'root': '/event_public_roomster/event_public_roomster',
#             'objects': http.request.env['event_public_roomster.event_public_roomster'].search([]),
#         })

#     @http.route('/event_public_roomster/event_public_roomster/objects/<model("event_public_roomster.event_public_roomster"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('event_public_roomster.object', {
#             'object': obj
#         })
