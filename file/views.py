import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from django.contrib.auth.decorators import login_required

from models import File

@csrf_exempt
@require_POST
@login_required
def upload(request, is_img=False):
	files = []
	for f in request.FILES.getlist('file'):
		obj = File.objects.create(upload=f, is_image=is_img)
		files.append({'filelink': obj.upload.url, 'filename':  obj.upload.url})
	return HttpResponse(json.dumps(files), mimetype="application/json")


@login_required
def recent(request, is_img=False):
	files = [
		{"thumb": obj.upload.url, "file": obj.upload.url}
		for obj in File.objects.filter(is_image=is_img).order_by("-created")[:20]	
	]
	return HttpResponse(json.dumps(files), mimetype="application/json")