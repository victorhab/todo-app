from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Activity
from .forms import ActivityForm
from django.shortcuts import redirect


# Create your views here.
def activity_list(request):
    #activities = Activity.objects.all()
    if not request.user.is_authenticated:
        activities = None
    else:
        activities = Activity.objects.filter(author=request.user)
    return render(request, 'todo/activity_list.html', {'activities': activities})

def activity_detail(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    return render(request, 'todo/activity_detail.html', {'activity': activity})

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
