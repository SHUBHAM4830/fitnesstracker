from django.shortcuts import render, redirect, get_object_or_404
from .models import Activity
from .forms import ActivityForm

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm


from django.contrib.auth.decorators import login_required



def index(request):
    return render(request,'trackdashboard/index.html')


@login_required(login_url='/login/')


# List Activities

def activity_list(request):
    activities = Activity.objects.all()
    return render(request, 'trackdashboard/activity.html', {'activities': activities})



# Create Activity
def create_activity(request):
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('activity_list')
    else:
        form = ActivityForm()
    return render(request, 'trackdashboard/activity_form.html', {'form': form})

# View Activity Details
def view_activity(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    return render(request, 'trackdashboard/activity_detail.html', {'activity': activity})

# Update Activity
def update_activity(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == "POST":
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('activity_list')
    else:
        form = ActivityForm(instance=activity)
    return render(request, 'trackdashboard/activity_form.html', {'form': form})

# Delete Activity
def delete_activity(request,pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == "POST":
        activity.delete()
        return redirect('activity_list')
    return render(request, 'trackdashboard/activity_confirm_delete.html', {'activity': activity})




# Signup View
def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after signup
            return redirect('activity_list')  # Redirect to activity page
    else:
        form = SignupForm()
    return render(request, 'trackdashboard/signup.html', {'form': form})

# Login View
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Get the 'next' parameter from the request to redirect user properly
            next_url = request.POST.get('next') or request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('activity_list')  # Redirect to the logged-in user's activities

    else:
        form = AuthenticationForm()

    return render(request, 'trackdashboard/login.html', {'form': form})  # Ensure the function always returns a response
# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout