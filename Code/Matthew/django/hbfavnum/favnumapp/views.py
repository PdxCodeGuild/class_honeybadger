from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import FavNumReason, FavNum
import json

def index(request):
    reasons = FavNumReason.objects.all().order_by('text')
    # fav_nums = FavNum.objects.filter(user=request.user).order_by('number')
    fav_nums = request.user.fav_nums.order_by('number')

    context = {
        'reasons': reasons,
        'fav_nums': fav_nums
    }
    return render(request, 'favnumapp/index.html', context)

@login_required
def save_favnum(request):
    # print(request.POST)
    number = request.POST['number']
    reason_id = request.POST['reason_id']
    other_reason = request.POST['other_reason']
    user = request.user

    # reason = FavNumReason.objects.get(id=reason_id)
    # fav_num = FavNum(number=number, reason=reason, other_reason=other_reason, user=user)
    # fav_num.save()

    fav_num = FavNum(number=number, reason_id=reason_id, other_reason=other_reason, user=user)
    fav_num.save()

    return HttpResponseRedirect(reverse('favnumapp:index'))

@login_required
def get_fav_nums(request):
    db_fav_nums = request.user.fav_nums.order_by('number')
    fav_nums = []
    for db_fav_num in db_fav_nums:
        number = db_fav_num.number
        reason = db_fav_num.reason.text
        other_reason = db_fav_num.other_reason
        fav_nums.append({
            'number': number,
            'reason': reason,
            'other_reason': other_reason,
        })
    return JsonResponse({'fav_nums': fav_nums})

@login_required
def save_favnum_ajax(request):
    data = json.loads(request.body)
    number = data['number']
    reason_id = data['reason_id']
    other_reason = data['other_reason']
    user = request.user
    
    fav_num = FavNum(number=number, reason_id=reason_id, other_reason=other_reason, user=user)
    fav_num.save()

    return HttpResponse('ok')
