from django.http import HttpResponse
from django.template import loader
from .models import Member
import datetime

# CRUD -> Member
# Create
def create_member(request):
  pass
# Read
# vista de todos los members -> read all / get all

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, slug):
  mymember = Member.objects.get(slug=slug)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

# Update
def update_member(request):
  pass

# Delete
def delete_member(request):
  pass

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
