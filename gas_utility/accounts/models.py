from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def account_info(request):
    return render(request, 'accounts/account_info.html', {'user': request.user})