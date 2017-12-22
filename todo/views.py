from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Activity
from .forms import ActivityForm
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm


# If the user is not logged in, they will get an empty activity List
# If the user is logged in, they get the list of objects which they are author of
def activity_list(request):
    loginform = AuthenticationForm(request.POST)
    if not request.user.is_authenticated:
        activities = None
    else:
        activities = Activity.objects.filter(author=request.user)
    return render(request, 'todo/activity_list.html', {'activities': activities}, {'form': loginform})

#If a user requests an activity which they did not write, they are redirected to their activity_list
def activity_detail(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.user==activity.author:
        return render(request, 'todo/activity_detail.html', {'activity': activity})
    else:
        return redirect('activity_list')

def add_new(request):
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.author = request.user
            activity.save()
            return redirect('activity_detail', pk=activity.pk)

    else:
        form = ActivityForm()
    return render(request, 'todo/activity_edit.html', {'form': form})

def register(request):
    return render(request, 'todo/register.html')
