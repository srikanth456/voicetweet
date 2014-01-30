from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login as django_login
from django.contrib.auth.views import logout as django_logout
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_GET


def home(req):
    return render(req,"main.html")

@login_required
def ct_user(req):
    return render(req,"ct/vt-admin.html")

def login(req, template_name="ct/vt-login.html"):
    return django_login(req, **{"template_name": template_name})
