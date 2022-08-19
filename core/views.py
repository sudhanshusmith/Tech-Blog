from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render
from core.models import Post
from core.forms import NewPost





from core.forms import SignupForm
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import  authenticate, login, logout, update_session_auth_hash

#Home
def home(request):
  posts = Post.objects.all()
  return render(request, 'core/home.html', {'posts': posts})






def newpost(request):
  if request.user.is_authenticated:
    if request.method == 'POST':
      added_post = NewPost(request.POST)
      if added_post.is_valid():
        added_post.save()
        messages.success(request, 'Post Added Successfully !!')
        return HttpResponseRedirect('/dashboard/')
    else:
      form = NewPost()
    return render(request, 'core/newpost.html', {'form': form})
  else:
    return HttpResponseRedirect('/user_login/')





def editpost(request , id):
  if request.user.is_authenticated:
    if request.method == 'POST':
      data = Post.objects.get(pk=id)
      form = NewPost(instance=data)
      return render(request, 'core/editpost.html', {'form': form, 'id': id} )
    else:
      return HttpResponseRedirect('/user_login/')  
  else:
    return HttpResponseRedirect('/user_login/')



def updatepost(request, id):
  if request.user.is_authenticated:
    if request.method == 'POST':
      data = Post.objects.get(pk=id)
      form = NewPost(request.POST, instance=data)
      if form.is_valid:
        form.save()
        messages.success(request, 'Post Updated Successfully !!')
        return HttpResponseRedirect('/dashboard/')
    else:
      return HttpResponseRedirect('/user_login/')
  else:
    return HttpResponseRedirect('/user_login/')



def confirm_del(request , id):
  if request.user.is_authenticated:
    if request.method == 'POST':
      return render(request, 'core/confirm_del.html', {'id': id})
    else:
      return HttpResponseRedirect('/user_login/')
  else:
    return HttpResponseRedirect('/user_login/')



def deletepost(request, id):
  if request.user.is_authenticated:
    if request.method == 'POST':
      to_be_deleted = Post.objects.get(pk = id)
      to_be_deleted.delete()
      messages.success(request, 'Deletion Successfull !!')
      return HttpResponseRedirect('/dashboard/')

    else:
      return HttpResponseRedirect('/user_login/')
  else:
    return HttpResponseRedirect('/user_login/')




# view for User Sign-Up
def user_signup(request):
  if not request.user.is_authenticated:
    if request.method == "POST":
      fm = SignupForm(request.POST)
      if fm.is_valid():

        # Adding into Author Groups 
        user = fm.save()
        Author = Group.objects.get(name='Author')
        user.groups.add(Author)

        messages.success(request, 'Account Created Succesfully, Now You can Log in !!')
    else:
      fm = SignupForm()
    return render(request, 'core/user_signup.html', {'form': fm})
  else:
    return HttpResponseRedirect('/dashboard')



# View for user Log In
def user_login(request):
  if not request.user.is_authenticated:
    if request.method == 'POST':
      fm = AuthenticationForm(request=request, data=request.POST)
      if fm.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
          login(request, user)
          messages.success(request, 'Logged in Succesfully !!')
          return HttpResponseRedirect('/dashboard/')
    else:
      fm = AuthenticationForm()
    return render(request, 'core/user_login.html', {'form': fm})
  else:
    return HttpResponseRedirect('/dashboard/')




# Views of dashboard is Here
def dashboard(request):
  if request.user.is_authenticated:
    all_post = Post.objects.all()
    return render(request, 'core/dashboard.html', {'all_post': all_post, 'name':request.user})
  else:
    return HttpResponseRedirect('/user_login/')



# Views of Logout is Here
def user_logout(request):
  if request.user.is_authenticated:
    logout(request)
    messages.success(request, 'Logged Out Successfully !!')
    return HttpResponseRedirect('/user_login/')
  else:
    messages.warning(request, 'Please Login First !!')
    return HttpResponseRedirect('/user_login/')


# Views of Password Change is Here
def user_changepass(request):
  if request.user.is_authenticated:
    if request.method == 'POST':
      fm = PasswordChangeForm(user=request.user, data=request.POST)
      if fm.is_valid():
        fm.save()
        messages.success(request,'Password Changed Successfully!!')
        update_session_auth_hash(request, fm.user)
        return HttpResponseRedirect('/dashboard/')
    else:
      fm = PasswordChangeForm(user=request.user)
    return render(request, 'core/user_changepass.html', {'form': fm})
  else:
    messages.warning(request, 'Please Login First !!')
    return HttpResponseRedirect('/user_login/')
