from django.http import HttpResponse
from django.shortcuts import render
import joblib

# Create your views here.

def choice(request):
    return render(request,'deployml/front.html')

def start1(request):
    return render(request, 'deployml/index1.html')

def start(request):
    return render(request, 'deployml/index.html')


def predict(request):
    cls = joblib.load('refr.joblib')

    lis=[]

    lis.append(request.POST['ram'])
    lis.append(request.POST['rom'])
    lis.append(request.POST['ms'])
    lis.append(request.POST['pri_cam'])
    lis.append(request.POST['sec_cam'])
    lis.append(request.POST['Battery'])
    print(lis)
    ans = cls.predict([lis])
    print(ans)
    if not lis:
        return HttpResponse("Fill in the details")
    else:
        return render(request, 'deployml/predict.html', {'ans':ans})

def result(request):
    
    cls = joblib.load('class.joblib')

    lis=[]

    lis.append(request.POST['ram'])
    lis.append(request.POST['px_height'])
    lis.append(request.POST['battery_power'])
    lis.append(request.POST['px_width'])
    lis.append(request.POST['mobile_wt'])
    lis.append(request.POST['int_memory'])
    lis.append(request.POST['sc_h'])
    lis.append(request.POST['talk_time'])
    lis.append(request.POST['sc_w'])
    lis.append(request.POST['fc'])
    lis.append(request.POST['n_cores'])
    lis.append(request.POST['pc'])
    print(lis)
    ans = cls.predict([lis])
    print(ans)

    return render(request,'deployml/result.html', {'ans': ans})