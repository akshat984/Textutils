# I HAVE CREATED THIS FILE -  AKSHAT
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render,redirect
def index(request):
    return render(request,'index.html')
def analyse(request):
    text = request.POST.get('text','off')
    t1 = text
    rmvpun = request.POST.get('rmvpun','off')
    fullcap = request.POST.get('fullcaps','off')
    newlinermv = request.POST.get('newlinermv','off')
    spacermv = request.POST.get('spacermv','off')
    charcount = request.POST.get('charcount','off')
    pur = []
    if text != "":
        if rmvpun == "off" and fullcap == "off" and newlinermv == "off" and spacermv == "off" and charcount == "off":
            messages.info(request, 'please select one of the feature')
            return redirect('/')
        if rmvpun == "off" and fullcap == "off" and newlinermv == "off" and spacermv == "off" and charcount == "on":
                p5 = "COUNT NUMBER OF CHARACTER"
                char, space = charCount(t1)
                total = char + space
                pur.append(p5)
                ans = False
                return render(request, 'analyse.html',
                  {'purpose': pur, 'answer': ans, 'char': char, 'space': space, 'total': total})
        if rmvpun == "on":
                    p1 = "REMOVE PUNCTUATION"
                    text = removePunctuation(text)
                    pur.append(p1)
        if fullcap == "on":
                    p2 = "UPPER"
                    text = fullcaps(text)
                    pur.append(p2)
        if newlinermv == "on":
                    p3 = "REMOVE NEW LINE"
                    text = newLineRemover(text)
                    pur.append(p3)
        if spacermv == "on":
                    p4 = "REMOVE EXTRA SPACE"
                    text = spaceRemover(text)
                    pur.append(p4)
        if charcount == "on":
                    p5 = "COUNT NUMBER OF CHARACTER"
                    char,space = charCount(t1)
                    total = char+space
                    pur.append(p5)
        else:
            char,space,total = False,False,False
        return render(request,'analyse.html',{'purpose':pur,'answer':text,'char':char,'space':space,'total':total})
    else:
        messages.info(request,'please enter your text')
        return redirect('/')

def removePunctuation(text):
    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    analyse = ""
    for char in text:
        if char not in  punctuations :
            analyse = analyse + char
    return analyse
def fullcaps(text):
    analyse = ""
    for char in text:
        analyse = analyse + char.upper()
    return analyse
def newLineRemover(text):
    analyse = ""
    for index,char in enumerate(text):
        if char != "\n" and char !="\r":
            analyse = analyse + char
        if (text[index]=="\r" and text[index+1]=="\n"):
            analyse = analyse + " "

    return analyse
def spaceRemover(text):
    analyse = ""
    for index, char in enumerate(text):
        if not (text[index] == " " and text[index + 1] == " "):
            analyse = analyse + char
    return analyse
def charCount(text):
    char = 0
    space = 0
    for i in text:
        if i !="\n" and i !="\r" and i !=" ":
            char+=1
        if i ==" ":
            space+=1
    return char,space