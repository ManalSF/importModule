from odoo import api, models, fields


class createwizard(models.TransientModel):
    _name = "createee.wizard"
    

    file = fields.Binary('File to import', required=True)
    file_type = fields.Selection([('csv', 'CSV'), ('xls', 'XLS')], string='Choose the file Type', default='csv')
    
    def create_records(self):
        print("Yeah successfully click on update_student_fees method........")

    

