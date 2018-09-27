# -*- coding: utf-8 -*-
from odoo import http

# class RumaKafka(http.Controller):
#     @http.route('/ruma_kafka/ruma_kafka/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ruma_kafka/ruma_kafka/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ruma_kafka.listing', {
#             'root': '/ruma_kafka/ruma_kafka',
#             'objects': http.request.env['ruma_kafka.ruma_kafka'].search([]),
#         })

#     @http.route('/ruma_kafka/ruma_kafka/objects/<model("ruma_kafka.ruma_kafka"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ruma_kafka.object', {
#             'object': obj
#         })