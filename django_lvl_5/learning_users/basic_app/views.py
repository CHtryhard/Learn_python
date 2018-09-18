from django.shortcuts import render

from basic_app.forms import UserForm, UserProfileInfoForm


# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit = False)
            # the reason for not commit is we dont want to overwrite it
            # the following code is build the one to one relationship
            profile.user = user
            # same type of method dealing with other files
            #  live .csv .pdf resume something like that
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/registration.html',
                    {'user_form':user_form,
                    'profile_form':profile_form,
                    'registered':registered})
