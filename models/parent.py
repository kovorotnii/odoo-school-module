# -*- coding: utf-8 -*-

from odoo import models, fields, api
import random

class Parent(models.Model):
    # model name
    _name = 'parent.parent'

    # Names for fields set in xml
    name = fields.Char(required=True)
    
    # use for testing funcs
    age = fields.Integer()

    test = fields.Char(compute='_compute_test')
    # link parent with student
    student = fields.Many2one('student.student') 
    # link parent with teacher
    teacher = fields.Many2one('teacher.teacher')

    onchange_field = fields.Char(compute='_on_change_computing')

    # while changing na,e then click next input
    # it will generate test field value
    @api.depends('name')
    def _compute_test(self):
        for record in self:
            record.test = str(random.randint(1, 1e6))

    # while we change age then
    # the value will be generated for onchange_filed variable
    @api.onchange('age')
    def _on_change_computing(self):
        self.onchange_field = str(random.randint(1, 1000) * random.randint(100, 100) * self.age) 