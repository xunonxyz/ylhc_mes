# -*- coding: utf-8 -*-
# from odoo import http


# class YlhcMes(http.Controller):
#     @http.route('/ylhc_mes/ylhc_mes', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ylhc_mes/ylhc_mes/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ylhc_mes.listing', {
#             'root': '/ylhc_mes/ylhc_mes',
#             'objects': http.request.env['ylhc_mes.ylhc_mes'].search([]),
#         })

#     @http.route('/ylhc_mes/ylhc_mes/objects/<model("ylhc_mes.ylhc_mes"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ylhc_mes.object', {
#             'object': obj
#         })

