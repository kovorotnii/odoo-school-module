# -*- coding: utf-8 -*-

from odoo import models, fields

class Parent(models.Model):
    # model name
    _name = 'parent.parent'

    name = fields.Char(string='Name', required=True)
    # link parent with student
    student = fields.Many2one('student.student', required=True) 
    # link parent with teacher
    teacher = fields.Many2one('teacher.teacher', required=True)
