# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import SUPERUSER_ID, api


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    coa_saveincloud_tmpl = env.ref(
        "l10n_br_coa_saveincloud.l10n_br_coa_saveincloud_chart_template"
    )
    if env["ir.module.module"].search_count(
        [
            ("name", "=", "l10n_br_account"),
            ("state", "=", "installed"),
        ]
    ):
        saveincloud_coa_charts = env["account.chart.template"].search(
            [("parent_id", "=", coa_saveincloud_tmpl.id)]
        )
        for saveincloud_coa_chart in saveincloud_coa_charts:
            saveincloud_coa_chart.load_fiscal_taxes(env, coa_saveincloud_tmpl)
