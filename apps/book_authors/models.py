from __future__ import unicode_literals
from django.db import models

class Book( models.Model ):
    name = models.CharField( max_length = 255 )
    desc = models.TextField( max_length = 1000, blank = True )
    created_at = models.DateTimeField( auto_now_add = True )
    updated_at = models.DateTimeField( auto_now = True )
    def _unicode__( self ):
        return "id: " + str( self.id ) + ", name: " + self.name

class Author( models.Model ):
    books = models.ManyToManyField( Book, related_name = "authors" )
    first_name = models.CharField( max_length = 255 )
    last_name = models.CharField( max_length = 255 )
    email = models.CharField( max_length = 255 )
    notes = models.TextField( blank = True )
    created_at = models.DateTimeField( auto_now_add = True )
    updated_at = models.DateTimeField( auto_now = True )
