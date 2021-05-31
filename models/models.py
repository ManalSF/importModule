# -*- coding: utf-8 -*-

import binascii
import tempfile

import certifi
import urllib3
import base64
import csv
import io
import xlrd


from odoo import models, fields, api, _
from odoo.exceptions import Warning, UserError

class import_records(models.Model):
    _name = 'import_records.import_records'
    _inherit = 'base'
    
    file = fields.Binary('File to import', required=True)
    file_type = fields.Selection([('csv', 'CSV'), ('xls', 'XLS')], string="File Type", default='csv')

    res_model = fields.Selection([('explo.explo','Explo'), ('invst.invest','Invest'),('achat.achat','Achat')],string='Model')

    def import_file(self):
        table = 'NULL'
        if self.res_model == 'explo.explo':
            table = 'explo_explo'
        if self.res_model == 'invest.invest':
            table = 'invest_invest'
        if self.file_type == 'csv':

            keys = ['code', 'rubriques','montant']

            try:
                file = base64.b64decode(self.file)
                data = io.StringIO(file.decode("utf-8"))
                data.seek(0)
                file_reader = []
                csv_reader = csv.reader(data, delimiter=',')
                file_reader.extend(csv_reader)

            except:
                raise Warning(_("File is not Valid!"))

            fields = list(map(str, file_reader[0]))
            print(fields)
            for fr in range(len(file_reader)):
                line = list(map(str, file_reader[fr]))
                vals = dict(zip(keys, line))
                if vals:
                    if fr == 0:
                        continue
                    else:
                        vals.update({
                            'code': line[0],
                            'rubriques': line[1],
                            'montant': line[2],
                        })
                        if line[2] == '' : 
                            line[2] = '0.0'
                        if "'" in line[1] :    
                            line[1] = line[1].replace("'","\'")
                        self.env.cr.execute("insert into "+table+" (code,rubriques,montant) values('"+line[0]+"','"+line[1]+"','"+line[2]+"')")
                        self.env.cr.commit()
                        
            
                        
        elif self.file_type == 'xls':
            try:
                fp = tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx")
                fp.write(binascii.a2b_base64(self.file))
                fp.seek(0)
                vals = {}
                workbook = xlrd.open_workbook(fp.name)
                sheet = workbook.sheet_by_index(0)

            except:
                raise Warning(_("File not Valid"))
            
            fields = map(lambda row: row.value.encode('utf-8'), sheet.row(0))
            print(fields)
            for row_no in range(sheet.nrows):
                val = {}
                if row_no <= 0:
                    continue
                else:

                    line = list(
                        map(lambda row: isinstance(row.value, bytes) and row.value.encode('utf-8') or str(row.value),
                            sheet.row(row_no)))

                    vals.update({
                        'code': line[0],
                        'rubriques': line[1],
                        'montant': line[2],
                    })
                    if line[2] == '' :
                        line[2] = '0.0'
                    if "'" in line[1] :
                        line[1] = line[1].replace("'","\'")
                    self.env.cr.execute("insert into "+table+" (code,rubriques,montant) values('"+line[0]+"','"+line[1]+"','"+line[2]+"')")
                    self.env.cr.commit()     
        else:
            raise UserError(_("Please select xls or csv format!"))

    
    def wiz_open(self):

        return self.env['ir.actions.act_window']._for_xml_id("import_records.wizard_action")
    #tim lif 