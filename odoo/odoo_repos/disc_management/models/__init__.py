from odoo import models, fields

class DiscManagement(models.Model):
    _name = 'disc.management'
    _description = 'Disc Management'
    
    name = fields.Char()
    author = fields.Char()
    year = fields.Date()
    image = fields.Image()
    format = fields.Selection([('cd', 'CD'),
                               ('dvd', 'DVD'),
                               ('vinyl', 'Vinyl')])
    remastered = fields.Boolean()
    genere = fields.Selection([('rock', 'Rock'),
                               ('pop', 'Pop'),
                               ('jazz', 'Jazz'),
                               ('blues', 'Blues'),
                               ('classical', 'Classical'),
                               ('country', 'Country')])