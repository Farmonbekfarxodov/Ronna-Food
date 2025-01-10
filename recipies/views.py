from django.shortcuts import render

def recipies_list_view(request):
    return render(request,'recipies/category.html')

def recipies_category_list_view(request):
    return render(request,'recipies/submit-recipe.html')
