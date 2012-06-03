# Create your views here.
from django.template import Context, loader
from checklist.models import Check
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
	latest_Check_list = Check.objects.all().order_by('-pub_date')[:5]
	t = loader.get_template('io_inspect/index.html')
	c = Context({
		'latest_Check_list': latest_Check_list
	})

	output = ', '.join([p.question for p in latest_Check_list])
	return HttpResponse(t.render(c))

def detail(request, Check_id):
#		return render_to_response('polls/index.html', {
#			'latest_Check_list': latest_Check_list
#		})
		return HttpResponse('This is the detail for %s.' % Check_id)
		
def results(request, Check_id):
	return HttpResponse('This is the results for %s.' % Check_id)

def vote(request, Check_id):
	return HttpResponse('This is the vote for %s.' % Check_id)