from __future__ import unicode_literals
from django.db import models
from django import forms
# for regular expressions 
import re 
# for validating an Email 
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
# ---------------------------------------------

# MANAGER FOR VALIDATION
class DashboardUserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1 : 
            errors['first_name'] = "Enter a first name"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Enter a last name"
        if not (postData['first_name']).isalpha() or not (postData['last_name']).isalpha():
            errors['Name only include letters'] = "Name only include letters"
        
        if not (re.search(regex,postData['email'])):  
            errors['Invalid email'] = "Invalid email address"
        if len(postData['email']) < 1:
            errors['Add your email'] = "Add your email"
        if len(postData['password']) < 8:
            errors['Password must be at least 8 characters'] = "Password must be at least 8 characters"
        if postData['password'] != postData['confirm_password']:
            errors['Passwords don''t match'] = "Password don''t match"
        return errors

# ---------------------------------------------

# MANAGER FOR VALIDATION
class MessageManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['message_content']) < 1 : 
            errors['message_content'] = "you can''t post an empty message"
     
        return errors

# ---------------------------------------------

# MANAGER FOR VALIDATION
class CommentManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['comment_content']) < 1 : 
            errors['comment_content'] = "you can''t post an empty comment"
     
        return errors

# ---------------------------------------------

class DashboardUser(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length=255)
    password_hash = models.CharField(max_length=255)

    # normal = '0' | admin = '1' 
    user_level = models.CharField(max_length=2, default = '0')

    # optional user description
    desc = models.TextField(default = '')

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = DashboardUserManager()

    
    def __str__(self):
        return ('first_name = ' + self.first_name + ', last_name = ' + self.last_name + ', email = ' + self.email + ', password_hash = ' + self.password_hash)

# ---------------------------------------------

class Message(models.Model):
    # one-to-many relationship: one senderUser to many messages
    dashboardSender_id = models.ForeignKey(DashboardUser, related_name = "sent_messages")

    # one-to-many relationship: one receiver to many messages
    dashboardReceiver_id = models.ForeignKey(DashboardUser, related_name = "received_messages")

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = MessageManager()

    def __str__(self):
        return ('message = ' + self.message )
    
    # a=Message(dashboardSender_id=DashboardUser.objects.first(), dashboardReceiver_id = DashboardUser.objects.last(), message ="")

    # a.save()

# ---------------------------------------------

class Comment(models.Model):
    # one-to-many relationship: one user_id to many comments
    user_id = models.ForeignKey(DashboardUser, related_name = "sent_comments")

    # one-to-many relationship: one message_id to many comments
    message_id = models.ForeignKey(Message, related_name = "this_message")
  
    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = CommentManager()

    # def __str__(self):
    #     return ('comment = ' + self.comment )




