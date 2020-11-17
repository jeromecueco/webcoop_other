
# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, date
from __builtin__ import True
from pickle import TRUE

class eula(models.Model):
    _name = 'webcoop.eula'
    
  
    user = fields.Integer()
    eula_accepted = fields.Boolean()
    date_accepted = fields.Datetime()

        
    @api.one
    def accept_eula(self):
        self.ensure_one()    
        user_id = self.env.user
        print(user_id.id)
        self.user = user_id.id
        self.eula_accepted = True
        self.date_accepted = datetime.now()

            

        
        
                

    