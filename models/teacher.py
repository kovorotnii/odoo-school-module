# -*- coding: utf-8 -*-

from odoo import models, fields

class TeacherTeacher(models.Model):
    # model name
    _name = 'teacher.teacher'

    name = fields.Char(string='Name', required=True, default='Petr Ivanovich')
    age = fields.Integer(string='Age', required=True)
    teacher_dob = fields.Date(string='Date of birth')

    student = fields.Many2one('student.student', string='Student')