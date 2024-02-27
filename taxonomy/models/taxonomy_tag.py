# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging


_logger = logging.getLogger(__name__)


class TaxonomyTag(models.Model):
    _name = 'taxonomy.tag'
    _description = 'Taxonomy Tag'

    name = fields.Char(string='Name', required=True,
                       index=True, translate=True)
    active = fields.Boolean(string='Archiviert', default=True)
    parent_id = fields.Many2one('taxonomy.tag', string='Parent')
    systemtag = fields.Boolean(
        string='System Tag', default=False, help='System Tags können nicht gelöscht werden.')

    all_parent_ids = fields.Many2many('taxonomy.tag', string='All Parent Tags', compute='_compute_all_parent_ids',
                                      relation='all_parent_child_tag_rel', column1='child_id', column2='parent_id',
                                      store=True, readonly=True, recursive=True)
    all_child_ids = fields.Many2many('taxonomy.tag', string='All Child Tags', readonly=True,
                                     relation='all_parent_child_tag_rel', column1='parent_id', column2='child_id')

    def unlink(self):
        systemtags = self.filtered(lambda r: r.systemtag)
        if systemtags:
            tag_names = '\n'.join([f'- {tag.name}' for tag in systemtags])
            raise ValidationError(
                f'Folgende Tags sind System Tags und können deshalb nicht gelöscht werden:\n{tag_names}')
        return super().unlink()

    def name_get(self):
        res = []
        for record in self:
            _logger.info("name get taxonomy %s" % record.name)

            name = record.name
            parent = record.parent_id
            while parent:
                name = f'{parent.name} > {name}'
                parent = parent.parent_id
            res.append((record.id, name))
        return res

    @api.depends('parent_id', 'parent_id.all_parent_ids')
    def _compute_all_parent_ids(self):
        for record in self:
            record.all_parent_ids = record.parent_id + record.parent_id.all_parent_ids
