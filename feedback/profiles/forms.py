from django import forms 
# from .models import Fileuploads

# class FilesForms(forms.ModelForm):
#     class Meta:
#         model = Fileuploads
#         fields = "__all__"
#         labels = {
#                 "my_files":"File Name"
#             }
#         error_messages = {
#             "my_files":{
#                     "required":"This has to be uploaded"
#                 }
#             }

class ProfileForm(forms.Form):
    user_image = forms.ImageField()