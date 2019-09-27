# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo.exceptions import ValidationError

class TeacherTeacher(models.Model):
    # model name
    _name = 'teacher.teacher'

    name = fields.Char(string='Name', required=True, default='Petr Ivanovich')
    age = fields.Integer(string='Age')#, compute='_check_age')
    
    #teacher_dob = fields.Date(string='Date of birth')

    student = fields.Many2one('student.student', string='Student')

    # create age constrain
   # @api.constrains('age')
   # def _check_age(self):
    #    for r in self:
     #       if r.age > 70:
       #         raise ValidationError("Your age is too high")
   
