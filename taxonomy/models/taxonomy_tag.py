# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging


_logger = logging.getLogger(__name__)


class TaxonomyTag(models.Model):
    _name = 'taxonomy.tag'
    _description = 'Taxonomy Tag'

    name = fields.Char(string='Name', required=True, index=True)
    active = fields.Boolean(string='Archiviert', default=True)
    parent_id = fields.Many2one('taxonomy.tag', string='Parent')

    all_parent_ids = fields.Many2many('taxonomy.tag', string='All Parent Tags', compute='_compute_all_parent_ids',
                                      relation='all_parent_child_tag_rel', column1='child_id', column2='parent_id',
                                      store=True, readonly=True, recursive=True)
    all_child_ids = fields.Many2many('taxonomy.tag', string='All Child Tags', readonly=True,
                                     relation='all_parent_child_tag_rel', column1='parent_id', column2='child_id')

    @api.depends('parent_id', 'parent_id.all_parent_ids')
    def _compute_all_parent_ids(self):
        _logger.info(f'compute all parent ids for tags {self}')
        for record in self:
            record.all_parent_ids = record.parent_id + record.parent_id.all_parent_ids
