from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView 
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView


from .forms import ReviewForm
from .models import Review

# Create your views here.

class ReviewView(FormView):
    form_class = ReviewForm
    template_name = "reviews/reviews.html"
    success_url = "/thank-you"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    # def post(self,request):
    #     form = ReviewForm(request.POST)
        
    #     if form.is_valid():
    #         form.save()
    #         print(form.cleaned_data)
    #         return HttpResponseRedirect("/thank-you")
        
    #     return render(request, "reviews/reviews.html",{
    #             "form":form
    #         })

class ThanksView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "It works!"
        return context 

class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "review_lst"

    # def get_queryset(self):
    #     base = super().get_queryset()
    #     dataset = base.filter(rating__gt=3)
    #     return dataset
    

    
class SingleReviewView(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        loaded_review = self.object.id  #The loaded detail 
        favorite_id = self.request.session.get("favorite_review") # This is the favorite review that gets activated when that button is clicked that sends a POST request with that ID of what it loaded 
        context["is_favorite"] = str(loaded_review) == favorite_id  
        return context
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs["id"]
    #     selected_review = Review.objects.get(pk=review_id)
    #     context["review"] = selected_review
    #     return context

class AddFavoriteView(View):
    def post(self,request):
        review_id = request.POST["review_id"] # getting the details of the POST request of name review ID 
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)
        
  