from django.shortcuts import render

# Create your views here.
def activity_list(request):
    return render(request, 'todo/activity_list.html')
