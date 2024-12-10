from django.shortcuts import render
from .forms import PostForm
from .models import Profile
from django.shortcuts import render, redirect


# Create your views here.


from django.shortcuts import render

def dashboard(request):

    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():

            post = form.save(commit=False)

            post.user = request.user

            post.save()
            return redirect("socialsite:dashboard")
        
    return render(request, "socialsite/dashboard.html", {"form": form})

def profile_list(request):

    profiles = Profile.objects.exclude(user=request.user)

    return render(request, "socialsite/profile_list.html", {"profiles": profiles})

def profile(request, pk):

    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":

        current_user_profile = request.user.profile

        data = request.POST

        action = data.get("follow")

        if action == "follow":

            current_user_profile.follows.add(profile)

        elif action == "unfollow":

            current_user_profile.follows.remove(profile)

        current_user_profile.save()
    return render(request, "socialsite/profile.html", {"profile": profile})