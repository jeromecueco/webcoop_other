# -*- coding: utf-8 -*-
import logging
from odoo import http
# from odoo.addons.website.controllers.main import Website
from odoo.addons.web.controllers.main import Home
from __builtin__ import True
from odoo.http import request

_logger = logging.getLogger(__name__)

class Eula(http.Controller):
    @http.route('/web/eula/', type='http', auth='user', website=True)
    def index(self, **kw):
        return {
            'name': 'EULA Modal',
            'type': 'ir.actions.act_window',
            'res_model': 'webcoop.eula',
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': http.request.env.ref('eula.view_modal').id,
            'target': 'new',
            'domain': [],
            'context': dict(),
            'res_id': 1,
        }
        # _logger.info('eula ........................................')
        # return http.request.render('eula.agreement', {'objects': {}})

    # @http.route('/eula/eula/objects/', auth='public')
    # def list(self, **kw):
    #     return http.request.render('eula.listing', {
    #         'root': '/eula/eula',
    #         'objects': http.request.env['eula.eula'].search([]),
    #     })

    # @http.route('/eula/eula/objects/<model("eula.eula"):obj>/', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('eula.object', {
    #         'object': obj
    #     })

class HomeEula(Home):
    @http.route('/web/login', type='http', auth="none")
    def web_login(self, redirect=None, **kw):
        _logger.info('eula ........................................^^^^')
        
        
#         current_login=http.request.env.context.get('uid') 
#         print(request.session.uid)
#         
#         accepted = http.request.env['webcoop.eula'].sudo().search([('user','=', current_login)]).eula_accepted
        
        
        accepted = True
         
        if accepted == False:
            response = super(HomeEula, self).web_login(redirect="/web#action=%s" % (http.request.env.ref('eula.action_modal').id), **kw)
            return response
        else:
            response = super(HomeEula, self).web_login(redirect="web#menu_id=79&action=88&active_id=channel_inbox")
            return response
# 
#         
#      
        #print(http.request.env['eula.eula'].name)
        #print(http.request.env['webcoop.eula'].eula_accepted)
#         useracc_id = http.request.env['eula.eula'].user
#         
        #accept = http.request.env['webcoop.eula'].sudo().search([('user','=', http.request.env.user.id)]).eula_accepted
        #print(http.request.env['webcoop.eula'].search([('user','=', 1)])
        #response = super(HomeEula, self).web_login(redirect="/web#action=%s" % (http.request.env.ref('eula.action_modal').id), **kw)
        
        #response = super(HomeEula, self).web_login(redirect="http://localhost:8069/web?debug#view_type=kanban&model=ir.module.module&menu_id=52&action=37", **kw)
        
        #return response
            
  
  
  
  
    @http.route('/web/eula_long', type="http")
    def eula_long(self):
        
        eula_content = """<!DOCTYPE html>
            <html>
              <head>
                <meta charset="utf-8" />
                    <meta name="viewport" content="width=device-width">
              </head>
              <body>
                <object data="/web_debranding/static/src/pdf/eula_long.pdf" type="application/pdf" style="min-height:100vh;width:100%"></object>
              </body>
            </html>"""
        
        return eula_content

# class HomeEula(Home):
#     @http.route('/web', type='http', auth="none")
#     def web_client(self, s_action=None, **kw):
#         return {
#             'name': 'EULA Modal',
#             'type': 'ir.actions.act_window',
#             'res_model': 'eula.eula',
#             'view_type': 'form',
#             'view_mode': 'form',
#             'view_id': self.env.ref('eula.view_modal'),
#             'target': 'new',
#             'domain': [],
#             'context': dict(),
#             'res_id': 1,
#         }
#         return super(HomeEula, self).web_client(s_action, **kw)