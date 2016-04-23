# -*- coding: utf-8 -*-

import time
from openerp import api, models, _


class ReportCrmActivityMail (models.AbstractModel):

    _name = 'report.sagawatransport.report_crm_activity_mail'

    def _get_lines(self, form):
        cr = self.env.cr
        cr.execute('SELECT create_date as date, body as body, res_id as id FROM mail_message WHERE model = %s and create_date >= %s and create_date <= %s and subtype_id in %s and create_uid = %s', ('crm.lead', form['date1'], form['date2'],(3,4,5),self.env.uid))
        return cr.fetchall()

    @api.multi
    def render_html(self, data):
        model = self.env.context.get('active_model')
        docs = self.env[model].browse(self.env.context.get('active_id'))
        get_lines = self._get_lines(data['form'])
        docargs = {
            'doc_ids': self.ids,
            'doc_model': model,
            'data': data['form'],
            'docs': docs,
            'get_lines': get_lines,
            'time': time,

        }
        return self.env['report'].render('sagawatransport.report_crm_activity_mail', docargs)