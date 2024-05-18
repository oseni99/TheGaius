from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic import CreateView
from django.views.generic import ListView
# Create your views here.


class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"

class ProfilesView(ListView):
    template_name = "profiles/user_profile.html"
    model = UserProfile
    context_object_name = "profile"

    
    # def get(self, request):
    #     form = ProfileForm()
    #     return render(request, "profiles/create_profile.html",
    #                   {
    #                   "form":form
    #                       })

    # def post(self, request):
    #     submitted_data = ProfileForm(request.POST, request.FILES)

    #     if submitted_data.is_valid():
    #         profile = UserProfile(image = request.FILES["user_image"])
    #         profile.save()
    #         print(profile) 
    #         return HttpResponseRedirect("/profiles")
    #     return render(request, "profiles/create_profile.html",
    #                   {
    #                   "form":submitted_data
    #                       })