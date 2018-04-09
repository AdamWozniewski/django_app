from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from forms import UserProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance = request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/loggedin/')
    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance = profile)

    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render_to_response('user_profile.html', args)