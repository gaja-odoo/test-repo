from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    group_new_implied_group = fields.Boolean(
        "Use pickings for rental orders",
        implied_group='test_module_ppch.group_new_implied_group'
    )
