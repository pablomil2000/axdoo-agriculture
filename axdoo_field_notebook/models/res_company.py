# Copyright 2020 Manuel Calero <manuelcalero@xtendoo.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class Company(models.Model):
    _inherit = 'res.company'

    def _create_performance_sequence(self):
        vals = []
        for company in self:
            vals.append({
                'name': 'Sequence of performance',
                'code': 'field.notebook.performance',
                'company_id': company.id,
                'prefix': 'ACT/%(year)s/',
                'padding': 5,
                'number_next': 1,
                'number_increment': 1
            })
        if vals:
            self.env['ir.sequence'].create(vals)

    @api.model
    def create_missing_performance_sequences(self):
        company_ids = self.env['res.company'].search([])
        company_has_performance_seq = self.env['ir.sequence'].search(
            [('code', '=', 'field.notebook.performance')]).mapped('company_id')
        company_todo_sequence = company_ids - company_has_performance_seq
        company_todo_sequence._create_performance_sequence()

    def _create_phytosanitary_sequence(self):
        vals = []
        for company in self:
            vals.append({
                'name': 'Sequence of phytosanitary',
                'code': 'field.notebook.phytosanitary',
                'company_id': company.id,
                'prefix': 'FITO/%(year)s/',
                'padding': 5,
                'number_next': 1,
                'number_increment': 1
            })
        if vals:
            self.env['ir.sequence'].create(vals)

    @api.model
    def create_missing_phytosanitary_sequences(self):
        company_ids = self.env['res.company'].search([])
        company_has_phytosanitary_seq = self.env['ir.sequence'].search(
            [('code', '=', 'field.notebook.phytosanitary')]).mapped('company_id')
        company_todo_sequence = company_ids - company_has_phytosanitary_seq
        company_todo_sequence._create_phytosanitary_sequence()

    def _create_labor_sequence(self):
        vals = []
        for company in self:
            vals.append({
                'name': 'Sequence of labor',
                'code': 'field.notebook.labor',
                'company_id': company.id,
                'prefix': 'LABOR/%(year)s/',
                'padding': 5,
                'number_next': 1,
                'number_increment': 1
            })
        if vals:
            self.env['ir.sequence'].create(vals)

    @api.model
    def create_missing_labor_sequences(self):
        company_ids = self.env['res.company'].search([])
        company_has_labor_seq = self.env['ir.sequence'].search(
            [('code', '=', 'field.notebook.labor')]).mapped('company_id')
        company_todo_sequence = company_ids - company_has_labor_seq
        company_todo_sequence._create_labor_sequence()

    def _create_harvest_sequence(self):
        vals = []
        for company in self:
            vals.append({
                'name': 'Sequence of harvest',
                'code': 'field.notebook.harvest',
                'company_id': company.id,
                'prefix': 'COSECHA/%(year)s/',
                'padding': 5,
                'number_next': 1,
                'number_increment': 1
            })
        if vals:
            self.env['ir.sequence'].create(vals)

    @api.model
    def create_missing_harvest_sequences(self):
        company_ids = self.env['res.company'].search([])
        company_has_harvest_seq = self.env['ir.sequence'].search(
            [('code', '=', 'field.notebook.harvest')]).mapped('company_id')
        company_todo_sequence = company_ids - company_has_harvest_seq
        company_todo_sequence._create_harvest_sequence()

    def _create_irrigation_sequence(self):
        vals = []
        for company in self:
            vals.append({
                'name': 'Sequence of irrigation',
                'code': 'field.notebook.irrigation',
                'company_id': company.id,
                'prefix': 'RIEGO/%(year)s/',
                'padding': 5,
                'number_next': 1,
                'number_increment': 1
            })
        if vals:
            self.env['ir.sequence'].create(vals)

    @api.model
    def create_missing_irrigation_sequences(self):
        company_ids = self.env['res.company'].search([])
        company_has_irrigation_seq = self.env['ir.sequence'].search(
            [('code', '=', 'field.notebook.irrigation')]).mapped('company_id')
        company_todo_sequence = company_ids - company_has_irrigation_seq
        company_todo_sequence._create_irrigation_sequence()

    def _create_per_company_sequences(self):
        super(Company, self)._create_per_company_sequences()
        self._create_performance_sequence()
        self._create_phytosanitary_sequence()
        self._create_labor_sequence()
        self._create_harvest_sequence()
        self._create_irrigation_sequence()



