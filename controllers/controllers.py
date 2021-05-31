# -*- coding: utf-8 -*-
from odoo import http

# class ImportRecords(http.Controller):
#     @http.route('/import_records/import_records/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/import_records/import_records/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('import_records.listing', {
#             'root': '/import_records/import_records',
#             'objects': http.request.env['import_records.import_records'].search([]),
#         })

#     @http.route('/import_records/import_records/objects/<model("import_records.import_records"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('import_records.object', {
#             'object': obj
#         })