from django.shortcuts import render_to_response, HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext
from django.core.context_processors import csrf
from intranet.group_manager.models import Group, GroupMember, Project
from intranet.group_manager.forms import GroupForm

# Create your views here.
def main(request):
  groups = Group.objects.all()
  return render_to_response('intranet/group_manager/main.html',{"page":'group','groups':groups})
  
def new(request):
  c = {}
  c.update(csrf(request))
  if request.method == 'POST': # If the form has been submitted...
      form = GroupForm(request.POST,request.FILES) # A form bound to the POST data
      if form.is_valid(): # All validation rules pass
          handle_uploaded_file(request.FILES['logo'])
          form.save()
          return HttpResponseRedirect('/') # Redirect after POST
  else:
      form = GroupForm() # An unbound form

  return render_to_response('intranet/group_manager/form.html',{
      'form': form,
      "page":'group',
      "page_title":"Create new Group"
      },context_instance=RequestContext(request))
  
def edit(request,id):
  return render_to_response('intranet/group_manager/form.html',{"page":'group',"page_title":"Edit Group"})
  