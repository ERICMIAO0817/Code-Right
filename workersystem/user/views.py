import uuid

from django.core.cache import cache
from django.http import JsonResponse
from django.views.decorators.cache import cache_page

from user.models import User
from workersystem.views_constant import hax_str, send_email


# Create your views here.


@cache_page(60 * 30)
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        name = request.POST.get('name')
        id_card = request.POST.get('idcard')
        user = User.objects.filter(u_email=email)
        if user.exists():
            return JsonResponse({'msg': 'The user already exists', 'status': 201})
        password = hax_str(password)
        password = password[0:30]
        user = User()
        user.u_username = username
        user.u_password = password
        user.u_email = email
        user.u_idcard = id_card
        user.u_name = name
        print(password)
        user.save()
        u_token = uuid.uuid4().hex
        cache.set(u_token, user.pk, 60 * 30)
        send_email(username, email, u_token)
        data = {
            'status': 200,
            'msg': '注册成功，前往邮箱激活',
            'token': u_token,
        }
        return JsonResponse(data)


def check_user(request):
    username = request.POST.get('username')
    user = User.objects.filter(u_email=username)
    if user.exists():
        return JsonResponse({'msg': 'The user name already exists', 'status': 901})
    else:
        return JsonResponse({'msg': 'The user name is reasonable', 'status': 200})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password = hax_str(password)
        users = User.objects.filter(u_email=username)
        print(password[0:30])
        if users.exists():
            user = users.first()
            if password[0:30] == user.u_password:
                if user.is_active:
                    request.session['user_id'] = user.pk
                    return JsonResponse({'msg': 'Successful login', 'status': 200})
                else:
                    return JsonResponse({'msg': 'User not activated', 'status': 202})
            else:
                return JsonResponse({'msg': 'Wrong password', 'status': 201})
        else:
            return JsonResponse({'msg': 'User does not exist', 'status': 203})


def active(request):
    u_token = request.GET.get('u_token')
    u_id = cache.get(u_token)
    if u_id:
        user = User.objects.get(pk=u_id)
        user.is_active = True
        user.save()
        return JsonResponse({'msg': 'Activation successful'})
    else:
        return JsonResponse({'msg': 'Activation failed'})
