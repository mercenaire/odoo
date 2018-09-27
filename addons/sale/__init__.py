# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import models
from . import controllers
from . import report
from . import wizard
import threading

from functools import partial
import odoo
from odoo import api, SUPERUSER_ID


def uninstall_hook(cr, registry):
    def update_dashboard_graph_model(dbname):
        db_registry = odoo.modules.registry.Registry.new(dbname)
        with api.Environment.manage(), db_registry.cursor() as cr:
            env = api.Environment(cr, SUPERUSER_ID, {})
            if 'crm.team' in env:
                recs = env['crm.team'].search([])
                for rec in recs:
                    rec._onchange_team_type()

    cr.after("commit", partial(update_dashboard_graph_model, cr.dbname))

def post_load_sale():
    dbname = threading.currentThread().dbname
    db = odoo.sql_db.db_connect(dbname)
    odoo.registry(dbname).check_signaling()
    with odoo.api.Environment.manage(), db.cursor() as cr:
            env = odoo.api.Environment(cr, SUPERUSER_ID, {})
            # sales_order_result = env['sale.order'].create({'partner_id': 20})
            # print(sales_order_result)