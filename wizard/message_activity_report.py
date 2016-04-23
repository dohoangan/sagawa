import time
from datetime import datetime
from openerp import api, fields, models, _


class MessageActivity(models.TransientModel):

    _name = 'message.activity'
    _description = 'Activity Report'

    date1 = fields.Date(string='Start Date' , required=True, default=lambda *a: time.strftime('%Y-%m-%d'))
    date2 = fields.Date(string='End Date' , required=True, default=lambda *a: time.strftime('%Y-%m-%d'))

    def _build_contexts(self, data):
        result = {}
        result['date1'] = data['form']['date1'] or False
        result['date2'] = data['form']['date2'] or False
        return result

    @api.multi
    def check_report(self):
        self.ensure_one()
        data = {}
        data['ids'] = self.env.context.get('active_ids', [])
        data['model'] = self.env.context.get('active_model', 'ir.ui.menu')
        data['form'] = self.read(['date1', 'date2'])[0]
        used_context = self._build_contexts(data)
        data['form']['used_context'] = dict(used_context, lang=self.env.context.get('lang', 'en_US'))
        return self._print_report(data)


    def _print_report(self, data):
        res = {}
        data['form'].update(self.read(['date1'])[0])
        data['form'].update(self.read(['date1'])[0])
        data['form'].update(res)
        return self.env['report'].with_context(landscape=True).get_action(self, 'sagawatransport.report_crm_activity_mail',
                                                                          data=data)