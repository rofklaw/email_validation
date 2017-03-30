from __future__ import unicode_literals

from django.db import models

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class EmailManager(models.Manager):
    def validmail(self, email):
        errors = []
        if len(email) < 1:
            errors.append("You must enter a valid email")
        if not EMAIL_REGEX.match(email):
            errors.append("Your email address is not correctly formatted")
        return {'errors': errors}

class Email(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add = True)
    objects = EmailManager()
