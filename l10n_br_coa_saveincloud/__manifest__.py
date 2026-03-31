# Copyright 2026 - TODAY, Cristiano Mafra Junior <cristiano.mafra@escodoo.com.br>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Plano de Contas Saveincloud",
    "summary": "Plano de Contas da Saveincloud",
    "category": "Accounting",
    "license": "AGPL-3",
    "author": "Escodoo",
    "website": "https://github.com/Escodoo/savein-addons",
    "version": "16.0.1.0.0",
    "depends": ["l10n_br_coa"],
    "data": [
        "data/l10n_br_coa_saveincloud_template.xml",
        "data/account_group.xml",
        "data/account.account.template.csv",
        "data/l10n_br_coa_saveincloud_template_post.xml",
    ],
    "post_init_hook": "post_init_hook",
}
