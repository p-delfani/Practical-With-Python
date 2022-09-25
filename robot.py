import pyttsx3 as pt
import os
import webbrowser
url='https://google.com'
nameuser = input('enter your name')
pt.speak('hi'+nameuser)
pt.speak('i ready to help you write your requset ...')
request = input('enter your request ')

if(request=='open FileExplorer'):
    os.system(url)
    pt.speak('ok i opened it') 
