# from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse, HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
import requests
from urllib.parse import urlencode


@csrf_exempt
def ping(request):
    return JsonResponse({'pong': f'{request.GET.get("t", "ping")}'})


@csrf_exempt
def parking_spot_status(request, status_id):
    return JsonResponse({
        "data": {
            "requestId": status_id,
            "confirmed": True,
            "locationTitle": "Fells Wargo's Parking Lot",
            "locationAddress": "15714 Melrose Ave, Beverly Hills, CA 90201",
            "startDateTimeLocal": "2022-11-08T14:28:40-08:00",
            "endDateTimeLocal": "2022-12-31T14:28:40-08:00",
            "parkingSpotDetails": "spot 51",
            "receiptAmount": 272.95,
            "avatarDisplayName": "Annie W.",
            "avatarTitle": "Owner",
            "avatarImageURL": "https://avatars.githubusercontent.com/u/33796817?v=4"
        }
    })


@csrf_exempt
def map(request):
    center = request.GET.get("center")
    if not center:
        raise Http404('An address as the "center" param is a required in the url query string.')
    params = {
        "key": settings.GOOGLE_MAPS_API_KEY,
        "center": center,
        "zoom": request.GET.get("zoom", "15"),
        "format": request.GET.get("format", "JPEG"),
        "size": request.GET.get("size", "2000x2000"),
    }
    url = f"https://maps.googleapis.com/maps/api/staticmap?{urlencode(params)}"
    requests_response = requests.get(url)
    response_obj = HttpResponse(
        content=requests_response.content,
        status=requests_response.status_code,
        content_type=requests_response.headers['Content-Type']
    )
    return response_obj
