from odoo import api, models, fields


class createwizardparent(models.TransientModel):
    _name = "createee.wizard.parent"
    

    file = fields.Binary('File to import', required=True)
    file_type = fields.Selection([('csv', 'CSV'), ('xls', 'XLS')], string='Choose the file Type', default='csv')

    res_model = fields.Selection([('explo.explo','Explo'), ('invst.invest','Invest'),('achat.achat','Achat')],string='Model', required=True)
    def create_records(self):
        print("Yeah successfully click on update_student_fees method........")