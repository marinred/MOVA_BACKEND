from django.shortcuts import redirect

def LoginMove(request):
    if request.method == 'GET' :
        return redirect('https://mo-va.site/signup.html')
