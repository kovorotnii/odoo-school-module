# -*- coding: utf-8 -*-

from odoo import models, fields

class StudentStudent(models.Model):
    # model name which will store like a table in db
	_name = 'student.student'

    # Properties
	name = fields.Char(string='Name', required=True)
	age = fields.Integer(string='Age')
	photo = fields.Binary(string='Image')
	gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender')
	student_dob = fields.Date(string="Date of Birth")
	student_blood_group = fields.Selection(
    	[('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
     	('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
    	string='Blood Group')
        
	nationality = fields.Many2one('res.country', string='Nationality')