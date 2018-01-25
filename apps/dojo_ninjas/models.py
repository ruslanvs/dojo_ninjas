from __future__ import unicode_literals
from django.db import models

class Dojo( models.Model ):
    name = models.CharField( max_length = 255 )
    city = models.CharField( max_length = 255 )
    state = models.CharField( max_length = 2 )
    desc = models.TextField()
    created_at = models.DateTimeField( auto_now_add = True )
    updated_at = models.DateTimeField( auto_now = True )
    def __unicode__(self):
        return "id: " + str(self.id) + ", name: " + self.name

class Ninja( models.Model ):
    dojo = models.ForeignKey( Dojo, related_name = "ninjas" )
    first_name = models.CharField( max_length = 255 )
    last_name = models.CharField( max_length = 255 )
    created_at = models.DateTimeField( auto_now_add = True )
    updated_at = models.DateTimeField( auto_now = True )
    def __unicode__(self):
        return "id: " + str(self.id) + ", name: " + self.first_name, self.last_name
