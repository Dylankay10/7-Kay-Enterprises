
from odoo import models, api, fields


class ExcludeObjects(models.Model):
    _name = 'exclude.objects'


    model_id = fields.Many2one('ir.model', 'Model')
































