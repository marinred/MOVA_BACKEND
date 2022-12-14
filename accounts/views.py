from django.shortcuts import redirect

def LoginMove(request):
    if request.method == 'GET' :
        return redirect('http://127.0.0.1:5500/templates/user/signup.html')
