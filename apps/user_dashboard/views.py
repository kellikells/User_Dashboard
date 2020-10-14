
from django import http
from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.views import generic
from .models import *
import bcrypt
from django.contrib import messages # flash messages
from .models import *

# ====================================================
def index(request):
    return render(request, 'user_dashboard/index.html')

# ------------------------------------------------------------------------
def logout(request):
    request.session.clear()
    return redirect('/user_dashboard/')

# ------------------------------------------------------------------------
def register(request):
    return render(request, 'user_dashboard/register.html')

# ------------------------------------------------------------------------
def register_process(request):
    if request.method == "POST":

        # getting errors from DashboardUser Manager
        errors = DashboardUser.objects.basic_validator(request.POST)

        # if there are errors: go back to signin.html and display errors
        if len(errors):
            context = {
                "messages": errors
            }
            return render(request, 'user_dashboard/register.html', context)

        # if email is already in the database
        if len(DashboardUser.objects.filter(email = request.POST['email'])) > 0:
            context = {
                "email_messages" : request.POST['email'] + ' : email already exists'
            }
            return render(request, 'user_dashboard/register.html', context)

        # -----------------------------------------------------------------
        # NO ERRORS: ADD USER TO DATABASE
        else:

            # use bcrypt to hash password
            password_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

            # create DashboardUser
            new_user = DashboardUser(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password_hash=password_hash)
            new_user.save()


            if 'user_level' not in request.session:
                return redirect('/user_dashboard/register_success/')

            if request.session['user_level'] == "1":
                context = {
                    "good_messages": "you successfully created a new user! good job admin!"
                }
                return render(request, 'user_dashboard/users_new.html', context)
           
            else:
                return redirect('/user_dashboard')

# ------------------------------------------------------------------------
def register_success(request):
    context = {
                "good_messages": "you successfully registered, now you may sign in"
            }

    return render(request, 'user_dashboard/signin.html', context)

# ========================================================================
# ------------------------------------------------------------------------
def signin(request):
    return render(request, 'user_dashboard/signin.html')

# ------------------------------------------------------------------------
def signin_process(request):

    if request.method == "POST":
        errors = {}

        if len(request.POST['email']) < 1:
            errors['Enter your email'] = "Enter your email"
        if len(request.POST['password']) < 1:
            errors['Enter your password'] = "Enter your password"
        
        # if email is not in the database:
        if len(DashboardUser.objects.filter(email = request.POST['email'])) < 1 :
            errors['Email does not exist, please register'] = "Email does not exist, please register"
        
        if len(errors):
            context = {
                "messages": errors
            }
            return render(request, 'user_dashboard/signin.html', context)

        else: 
            # saving user object
            this_user = DashboardUser.objects.get(email = request.POST['email'])

            # if password matches database password ************************
            if bcrypt.checkpw(request.POST['password'].encode(), this_user.password_hash.encode()):
          
                # if user_level is admin : renders dashboard_admin.html
                if this_user.user_level == "1":
                    if 'user_level' not in request.session:
                        request.session['user_level'] = "1"
                    if 'user_id' not in request.session:
                        request.session['user_id'] = this_user.id
                    if 'user_name' not in request.session:
                        request.session['user_name'] = this_user.first_name
                    return redirect('/user_dashboard/dashboard_admin/')   

                # if user_level is normal : renders dashboard.html
                else:
                    if 'user_level' not in request.session:
                        request.session['user_level'] = "0"
                    if 'user_id' not in request.session:
                        request.session['user_id'] = this_user.id
                    if 'user_name' not in request.session:
                        request.session['user_name'] = this_user.first_name
                    return redirect('/user_dashboard/dashboard/')
            # .............................................................
                
            # if password doens't match database password
            else: 
                errors['password doesn''t match'] = "password doesn''t match"
                context = {
                    "messages": errors
                }
                return render(request, 'user_dashboard/signin.html', context)

# ------------------------------------------------------------------------
def dashboard_admin(request):
    context ={
        "users" : DashboardUser.objects.all()
    }
    return render(request,'user_dashboard/dashboard_admin.html', context)

# ------------------------------------------------------------------------
def dashboard(request):
    context = {

        "users": DashboardUser.objects.all()
    }
    return render(request, 'user_dashboard/dashboard.html', context)

# ------------------------------------------------------------------------
def users_new(request):
    return render(request, 'user_dashboard/users_new.html')

# ------------------------------------------------------------------------
def remove(request):
    if request.method == "POST":

        DashboardUser.objects.get(id= request.POST.get('removeID')).delete()

        return redirect('/user_dashboard/dashboard_admin/')

# ------------------------------------------------------------------------
def users_edit(request, id):
    context = {
        "user" : DashboardUser.objects.get(id=id)
    }
    return render(request, 'user_dashboard/users_edit_id.html', context)

# ------------------------------------------------------------------------
def normal_users_edit(request):
    context = {
        "user" : DashboardUser.objects.get(id=request.session['user_id'])
    }
    return render(request, 'user_dashboard/users_edit_id.html', context)

# ------------------------------------------------------------------------
def update(request, id):
    if request.method == "POST":
        temp_user = DashboardUser.objects.get(id=id)

        if request.POST['email']:
            temp_user.email = request.POST['email']
        
        if request.POST['first_name']:
            temp_user.first_name = request.POST['first_name']
        
        if request.POST['last_name']:
            temp_user.last_name = request.POST['last_name']
        
        temp_user.user_level = request.POST['user_level']

        temp_user.save()
      
    return redirect('/user_dashboard/dashboard_admin/')

# ------------------------------------------------------------------------
def update_password(request, id):
    if request.method == "POST":

        # figure out how to have a popup with errors, because can't use context in this redirect
        if request.POST['password'] != request.POST['confirm_password']:
            return redirect('/user_dashboard/users/edit/'+ id + '/')
        if len(request.POST['password']) < 8:
            return redirect('/user_dashboard/users/edit/'+ id + '/')

        # use bcrypt to hash password & update password
        else:
            temp_user = DashboardUser.objects.get(id=id)
            temp_user.password_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

            temp_user.save()
            return redirect('/user_dashboard/users/edit/'+ id + '/')

# ------------------------------------------------------------------------
def update_description(request, id):

    if request.method == "POST":
        temp_user = DashboardUser.objects.get(id = id)
        temp_user.desc = request.POST['desc']
        temp_user.save()

        return redirect('/user_dashboard/users/edit/' +id + '/')

# ------------------------------------------------------------------------
def users_show(request, id):
 
    context = {
        "user" : DashboardUser.objects.get(id=id),
        "messages" : Message.objects.filter(dashboardReceiver_id = id).order_by("-updated_at"),
        "comments" : Comment.objects.all().order_by("-updated_at")
    }

    return render(request, 'user_dashboard/users_show_id.html', context)

# ------------------------------------------------------------------------
def create_message(request, id, receiverID):
    if request.method == "POST":
         # getting errors from DashboardUser Manager
        errors = Message.objects.basic_validator(request.POST)

        # if there are errors: go back to signin.html and display errors
        if len(errors):
            context = {
                "errors": errors
            }
            return render(request, 'user_dashboard/users_show_id.html', context)

        # -----------------------------------------------
        # NO ERRORS: ADD MESSAGE TO DATABASE
        else:
            print("-"*30)
            print(request.POST['message_content'])
            # # save sender 
            sender = DashboardUser.objects.get(id = id)

            # # save receiver 
            receiver = DashboardUser.objects.get(id = receiverID)

            message_query = Message(dashboardSender_id = sender, dashboardReceiver_id = receiver, message = request.POST['message_content'])
            message_query.save()

            response="it works"
            return redirect('/user_dashboard/users/show/'+receiverID +'/')

# ------------------------------------------------------------------------
def create_comment(request, userID, messageID, receiverID):
    if request.method == "POST":

        # getting errors from Comment Manager
        errors = Comment.objects.basic_validator(request.POST)

        # if there are errors: go back to signin.html and display errors
        if len(errors):
            context = {
                "errors": errors
            }
            return render(request, 'user_dashboard/users_show_id.html', context)

        # ----------------------------------------------------------------
        # NO ERRORS: ADD COMMENT TO DATABASE
        else:

            # save sender
            # ------------------------------------------------------------
            commenter = DashboardUser.objects.get(id = userID)

            # save receiver 
            # ------------------------------------------------------------
            this_message = Message.objects.get(id = messageID)

            # create and save comment
            comment_query = Comment(user_id= commenter, message_id = this_message, comment = request.POST['comment_content'])
            comment_query.save()
    
            return redirect('/user_dashboard/users/show/'+receiverID +'/')

