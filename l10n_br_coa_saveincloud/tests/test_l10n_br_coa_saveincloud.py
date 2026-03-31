# Copyright 2026 - TODAY, Cristiano Mafra Junior <cristiano.mafra@escodoo.com.br>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class L10nBrCoaSaveincloud(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.l10n_br_coa_generic = cls.env.ref(
            "l10n_br_coa_saveincloud.l10n_br_coa_saveincloud_chart_template"
        )
        cls.l10n_br_company = cls.env["res.company"].create(
            {"name": "Saveincloud - Chart of Accounts"}
        )

    def test_l10n_br_coa_saveincloud(self):
        """Test to install the chart of accounts template in a new company"""
        self.env.user.company_ids += self.l10n_br_company
        self.env.user.company_id = self.l10n_br_company
        self.l10n_br_coa_generic.try_loading()

        self.assertEqual(
            self.l10n_br_coa_generic, self.l10n_br_company.chart_template_id
        )
