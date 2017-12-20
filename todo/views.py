from django.shortcuts import render
from django.utils import timezone
from .models import Activity
from django.shortcuts import render, get_object_or_404

# Create your views here.
def activity_list(request):
    activities = Activity.objects.all()
    return render(request, 'todo/activity_list.html', {'activities': activities})

def activity_detail(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    return render(request, 'todo/activity_detail.html', {'activity': activity})
