from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .decorators import group_required

@login_required
@group_required('view_one')
def view_one(self):
    return HttpResponse("This is View 1")


@login_required
@group_required('view_two')
def view_two(self):
    return HttpResponse("This is View 2")
