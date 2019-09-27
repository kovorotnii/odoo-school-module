# -*- coding: utf-8 -*-

from odoo import models, fields

class Parent(models.Model):
    # model name
    _name = 'parent.parent'

    # Names for fields set in xml
    name = fields.Char(required=True)
    test = fields.Char()
    # link parent with student
    student = fields.Many2one('student.student') 
    # link parent with teacher
    teacher = fields.Many2one('teacher.teacher')
