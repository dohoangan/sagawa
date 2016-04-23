import time
import re
from openerp import models, fields, api, tools, _
class sale_order(models.Model):
    _inherit = 'sale.order'
    is_templete = fields.Boolean('Is Templete')
    total_confirm_sale = fields.Float(string='Total Sale Value')
    order_details = fields.Html('Quotation Details')
    templete_id = fields.Many2one('sale.order', 'Chose Templete', domain="[('is_templete', '=', True)]")    
    @api.onchange('templete_id')
    def _onchange_is_templete(self):
        if self.templete_id:
            templete = self.env['sale.order'].browse(self.templete_id.id)
            self.order_details = templete.order_details
class crm_lead(models.Model):
    _inherit = 'crm.lead'
    sale_revenue = fields.Float('Revenue')
    reason_to_fail = fields.Text('Reason to fail')