# This is a customized view file
from django.http import HttpResponse
from django.shortcuts import render

#code for introduction of view

# def index(request):
#     return HttpResponse("Hello Punit")
#
# def about(request):
#     return HttpResponse("This is a about page")


def index(request):
    # params = {"name":"punit","location":"MUMBAI"}
    return render(request,'index.html')
    # return HttpResponse("""<h1>Home</h1><br><button type="button"><a href = "/">Go Back</a></button>""")

def analyze(request):
    #check the text
    analyze_text = request.POST.get('text','default')
    #check the checkbox for values
    remove_punc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremove = request.POST.get('newlineremove','off')
    spaceremover = request.POST.get('spaceremover','off')
    charcount = request.POST.get('charcount','off')
    # print(remove_punc)
    # print(analyze_text)
    # analyzed = analyze_text
    if remove_punc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in analyze_text:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose':'remove_punctuation','analyzed_text':analyzed}
        # print(params)
        return render(request,"analyze.html",params)

    elif(fullcaps=="on"):
        analyzed = ""
        for char in analyze_text:
            analyzed = analyzed + char.upper()

        parmas = {'purpose':'Upper Case','analyzed_text':analyzed}
        return render(request,"analyze.html",parmas)

    elif(newlineremove=="on"):
        analyzed = ""
        for char in analyze_text:
            if char !="\n" and char!="\r":
                analyzed = analyzed+char


        params = {'purpose':'NEW LINE CHARACTER','analyzed_text':analyzed}
        return render(request,"analyze.html",params)
    elif(spaceremover == "on"):
        analyzed = analyze_text
        analyzed = analyzed.replace(" ","")
        #print(analyzed)
        # analyzed=""
        # for index,char in enumerate(analyze_text):
        #     print(index,char)
        #     if not(analyze_text[index] == " " and analyze_text[index+1]==" "):
        #         analyzed = analyze_text+char
        #         # print(analyzed)

        params = {'purpose':'SPACE REMOVER','analyzed_text':analyzed}
        return render(request,"analyze.html",params)

    elif(charcount=="on"):
        count = 0
        for data in analyze_text:
            count = count + 1
        params = {'purpose':'CHARACTER COUNT','analyzed_text':count}
        return render(request,"analyze.html",params)
    else:
        return HttpResponse("ERROR")


# def remove_punc(request):
#     dj_text = request.GET.get('text','default') #getting the text
#     print(dj_text) #analyze the text
#     return HttpResponse("remove punc")
#
#
# def capitalize_first(request):
#     return HttpResponse("Capitalise First")
#
#
# def newlineremove(request):
#     return HttpResponse("New Line Remove ")
#
# def spaceremove(request):
#     return HttpResponse("Space Remove")
#
# def charcount(request):
#     return HttpResponse("Char Count Remove")
