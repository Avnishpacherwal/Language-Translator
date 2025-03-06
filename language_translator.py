# importing libraries
import datetime
import speech_recognition as sr  #Speech to Text
import pyttsx3     #Text to Speech
import wikipedia
import webbrowser
import os
import random

# importing 
from googletrans import Translator
from tkinter import *
from PIL import Image, ImageTk

# from playsound import playsound
import tkinter as tk
root=Tk()
t=Translator()
root.title("Smasher's Language Translator")
root.geometry("%dx%d+0+0" % (root.winfo_screenwidth(), root.winfo_screenheight()))
root.configure(bg="light blue")

# functions_row-2
def funcHindi():
    msg=varin.get()
    res=t.translate(msg,"Hi")
    res_data=res.text
    # print(res_data)
    varout.set(res_data)

def funcPunjabi():
    msg=varin.get()
    res=t.translate(msg,"pa")
    res_data=res.text
    varout.set(res_data)

def funcEnglish():
    msg=varin.get()
    res=t.translate(msg,"en")
    res_data=res.text
    varout.set(res_data)

def funcBengali():
    msg=varin.get()
    res=t.translate(msg,"bn")
    res_data=res.text
    varout.set(res_data)

def funcTelugu():
    msg = varin.get()
    res = t.translate(msg, "te")
    res_data = res.text
    varout.set(res_data)

# functions_row-3
def funcUrdu():
    msg = varin.get()
    res = t.translate(msg, "ur")
    res_data = res.text
    varout.set(res_data)

def funcGujarati():
    msg = varin.get()
    res = t.translate(msg, "gu")
    res_data = res.text
    # print(res_data)
    varout.set(res_data)

def funckannada():
    msg = varin.get()
    res = t.translate(msg, "kn")
    res_data = res.text
    varout.set(res_data)

def funcOdia():
    msg = varin.get()
    res = t.translate(msg, "or")
    res_data = res.text
    varout.set(res_data)

def funcMalayalam():
    msg = varin.get()
    res = t.translate(msg, "ml")
    res_data = res.text
    varout.set(res_data)

# functions_row-4
def funcSpanish():
    msg = varin.get()
    res = t.translate(msg, "es")
    res_data = res.text
    varout.set(res_data)

def funcFrench():
    msg = varin.get()
    res = t.translate(msg, "fr")
    res_data = res.text
    varout.set(res_data)

def funcGerman():
    msg = varin.get()
    res = t.translate(msg, "de")
    res_data = res.text
    varout.set(res_data)

def funcChinese():
    msg = varin.get()
    res = t.translate(msg, "zh-cn")
    res_data = res.text
    varout.set(res_data)

def funcArabic():
    msg = varin.get()
    res = t.translate(msg, "ar")
    res_data = res.text
    varout.set(res_data)

# functions_row-5
def funcRussian():
    msg = varin.get()
    res = t.translate(msg, "ru")
    res_data = res.text
    varout.set(res_data)

def funcPortuguese():
    msg = varin.get()
    res = t.translate(msg, "pt")
    res_data = res.text
    varout.set(res_data)

def funcJapanese():
    msg = varin.get()
    res = t.translate(msg, "ja")
    res_data = res.text
    varout.set(res_data)

def funcItalian():
    msg = varin.get()
    res = t.translate(msg, "it")
    res_data = res.text
    varout.set(res_data)

def funcKorean():
    msg = varin.get()
    res = t.translate(msg, "ko")
    res_data = res.text
    varout.set(res_data)

# functions_row-6
def funcDutch():
    msg = varin.get()
    res = t.translate(msg, "nl")
    res_data = res.text
    varout.set(res_data)

def funcTurkish():
    msg = varin.get()
    res = t.translate(msg, "tr")
    res_data = res.text
    varout.set(res_data)

def funcPolish():
    msg = varin.get()
    res = t.translate(msg, "pl")
    res_data = res.text
    varout.set(res_data)

def funcSwedish():
    msg = varin.get()
    res = t.translate(msg, "sv")
    res_data = res.text
    varout.set(res_data)

def funcThai():
    msg = varin.get()
    res = t.translate(msg, "th")
    res_data = res.text
    varout.set(res_data)

# functions_row-7
def funcIndonesian():
    msg = varin.get()
    res = t.translate(msg, "id")
    res_data = res.text
    varout.set(res_data)

def funcGreek():
    msg = varin.get()
    res = t.translate(msg, "el")
    res_data = res.text
    varout.set(res_data)

def funcVietnamese():
    msg = varin.get()
    res = t.translate(msg, "vi")
    res_data = res.text
    varout.set(res_data)

def funcFinnish():
    msg = varin.get()
    res = t.translate(msg, "fi")
    res_data = res.text
    varout.set(res_data)

def funcCzech():
    msg = varin.get()
    res = t.translate(msg, "cs")
    res_data = res.text
    varout.set(res_data)

# functions_row-8
def funcDanish():
    msg=varin.get()
    res=t.translate(msg,"da")
    res_data=res.text
    # print(res_data)
    varout.set(res_data)

def funcNorwegian():
    msg=varin.get()
    res=t.translate(msg,"no")
    res_data=res.text
    varout.set(res_data)

def funcHungarian():
    msg=varin.get()
    res=t.translate(msg,"hu")
    res_data=res.text
    varout.set(res_data)

def funcRomanian():
    msg=varin.get()
    res=t.translate(msg,"ro")
    res_data=res.text
    varout.set(res_data)

def funcCatalan():
    msg = varin.get()
    res = t.translate(msg, "ca")
    res_data = res.text
    varout.set(res_data)

# functions_row-9
def funcHebrew():
    msg = varin.get()
    res = t.translate(msg, "he")
    res_data = res.text
    varout.set(res_data)

def funcUkrainian():
    msg = varin.get()
    res = t.translate(msg, "uk")
    res_data = res.text
    # print(res_data)
    varout.set(res_data)

def funcSlovak():
    msg = varin.get()
    res = t.translate(msg, "sk")
    res_data = res.text
    varout.set(res_data)

def funcAfghanistan():
    msg = varin.get()
    res = t.translate(msg,"AF")
    res_data = res.text
    varout.set(res_data)

def funcMalay():
    msg = varin.get()
    res = t.translate(msg, "ms")
    res_data = res.text
    varout.set(res_data)

# functions_row-10
def funcCroatian():
    msg = varin.get()
    res = t.translate(msg, "hr")
    res_data = res.text
    varout.set(res_data)

def funcLithuanian():
    msg = varin.get()
    res = t.translate(msg, "lt")
    res_data = res.text
    varout.set(res_data)

def funcSlovenian():
    msg = varin.get()
    res = t.translate(msg, "sl")
    res_data = res.text
    varout.set(res_data)

def funcSerbian():
    msg = varin.get()
    res = t.translate(msg, "sr")
    res_data = res.text
    varout.set(res_data)

def funcBulgarian():
    msg = varin.get()
    res = t.translate(msg, "bg")
    res_data = res.text
    varout.set(res_data)

# functions_row-11
def funcEstonian():
    msg = varin.get()
    res = t.translate(msg, "et")
    res_data = res.text
    varout.set(res_data)

def funcLatvian():
    msg = varin.get()
    res = t.translate(msg, "lv")
    res_data = res.text
    varout.set(res_data)

def funcIcelandic():
    msg = varin.get()
    res = t.translate(msg, "is")
    res_data = res.text
    varout.set(res_data)

def funcAlbanian():
    msg = varin.get()
    res = t.translate(msg, "sq")
    res_data = res.text
    varout.set(res_data)

def funcMacedonian():
    msg = varin.get()
    res = t.translate(msg, "mk")
    res_data = res.text
    varout.set(res_data)

# Translate function
def funcTranslate():
    msg = varin.get()
    selected_language = varLanguage.get()
    res = t.translate(msg, selected_language)
    res_data = res.text
    varout.set(res_data)

# mic
def voice_search():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            varin.set(text)
            translate_text("English") 
        except:
            print("Sorry could not recognize what you said")

# clear
def funcTranslate():
    msg = varin.get()
    selected_language = varLanguage.get()
    res = t.translate(msg, selected_language)
    res_data = res.text
    varout.set(res_data)
    txt.delete('1.0', 'end')  # Clear the Text widget
    txt.insert('end', res_data)  # Insert the translated text

def funcClear():
    varin.set("")
    txt.delete('1.0', 'end')

# option_language_code(letter a)
def funcAfrikaans():
    msg = varin.get()
    res = t.translate(msg, "af")
    res_data = res.text
    varout.set(res_data)

def funcAlbanian():
    msg = varin.get()
    res = t.translate(msg, "sq")
    res_data = res.text
    varout.set(res_data)

def funcAmharic():
    msg = varin.get()
    res = t.translate(msg, "am")
    res_data = res.text
    varout.set(res_data)

def funcArabic():
    msg = varin.get()
    res = t.translate(msg, "ar")
    res_data = res.text
    varout.set(res_data)

def funcArmenian():
    msg = varin.get()
    res = t.translate(msg, "hy")
    res_data = res.text
    varout.set(res_data)

def funcAzerbaijani():
    msg = varin.get()
    res = t.translate(msg, "az")
    res_data = res.text
    varout.set(res_data)

def funcAfrikaans():
    msg = varin.get()
    res = t.translate(msg, "af")
    res_data = res.text
    varout.set(res_data)

def funcAmharic():
    msg = varin.get()
    res = t.translate(msg, "am")
    res_data = res.text
    varout.set(res_data)

# option_language_code(letter b)

def funcBasque():
    msg = varin.get()
    res = t.translate(msg, "eu")
    res_data = res.text
    varout.set(res_data)

def funcBelarusian():
    msg = varin.get()
    res = t.translate(msg, "be")
    res_data = res.text
    varout.set(res_data)

def funcBosnian():
    msg = varin.get()
    res = t.translate(msg, "bs")
    res_data = res.text
    varout.set(res_data)

def funcBulgarian():
    msg = varin.get()
    res = t.translate(msg, "bg")
    res_data = res.text
    varout.set(res_data)

# option_language_code(letter c)
def funcCzech():
    msg = varin.get()
    res = t.translate(msg, "cs")
    res_data = res.text
    varout.set(res_data) 

def funcCroatian():
    msg = varin.get()
    res = t.translate(msg, "hr")
    res_data = res.text
    varout.set(res_data)

def funcCorsican():
    msg = varin.get()
    res = t.translate(msg, "co")
    res_data = res.text
    varout.set(res_data)

def funcChichewa():
    msg = varin.get()
    res = t.translate(msg, "ny")
    res_data = res.text
    varout.set(res_data)

def funcCatalan():
    msg = varin.get()
    res = t.translate(msg, "ca")
    res_data = res.text
    varout.set(res_data)

# option_language_code(letter d)

def funcDutch():
    msg = varin.get()
    res = t.translate(msg, "nl")
    res_data = res.text
    varout.set(res_data)

def funcDanish():
    msg = varin.get()
    res = t.translate(msg, "da")
    res_data = res.text
    varout.set(res_data)

# option_language_code(letter e)

def funcEstonian():
    msg = varin.get()
    res = t.translate(msg, "et")
    res_data = res.text
    varout.set(res_data)

def funcEsperanto():
    msg = varin.get()
    res = t.translate(msg, "eo")
    res_data = res.text
    varout.set(res_data)

def funcEnglish():
    msg = varin.get()
    res = t.translate(msg, "en")
    res_data = res.text
    varout.set(res_data)

# option_language_code(letter f)
def funcFula():
    msg = varin.get()
    res = t.translate(msg, "ff")
    res_data = res.text
    varout.set(res_data)

def funcFrench():
    msg = varin.get()
    res = t.translate(msg, "fr")
    res_data = res.text
    varout.set(res_data)

def funcFinnish():
    msg = varin.get()
    res = t.translate(msg, "fi")
    res_data = res.text
    varout.set(res_data)

# option_language_code(letter g)
def funcGujarati():
    msg = varin.get()
    res = t.translate(msg, "gu")
    res_data = res.text
    varout.set(res_data)

def funcGreek():
    msg = varin.get()
    res = t.translate(msg, "el")
    res_data = res.text
    varout.set(res_data)

def funcGerman():
    msg = varin.get()
    res = t.translate(msg, "de")
    res_data = res.text
    varout.set(res_data)

def funcGeorgian():
    msg = varin.get()
    res = t.translate(msg, "ka")
    res_data = res.text
    varout.set(res_data)

def funcGalician():
    msg = varin.get()
    res = t.translate(msg, "gl")
    res_data = res.text
    varout.set(res_data)

# option_language_code(letter h)
def funcHungarian():
    msg = varin.get()
    res = t.translate(msg, "hu")
    res_data = res.text
    varout.set(res_data)

def funcHindi():
    msg = varin.get()
    res = t.translate(msg, "hi")
    res_data = res.text
    varout.set(res_data)

def funcHerero():
    msg = varin.get()
    res = t.translate(msg, "hz")
    res_data = res.text
    varout.set(res_data)

def funcHebrew():
    msg = varin.get()
    res = t.translate(msg, "he")
    res_data = res.text
    varout.set(res_data)

def funcHausa():
    msg = varin.get()
    res = t.translate(msg, "ha")
    res_data = res.text
    varout.set(res_data)

def funcHaitianCreole():
    msg = varin.get()
    res = t.translate(msg, "ht")
    res_data = res.text
    varout.set(res_data)

# option_language_code(letter i)
def funcItalian():
    msg = varin.get()
    res = t.translate(msg, "it")
    res_data = res.text
    varout.set(res_data)

def funcIndonesian():
    msg = varin.get()
    res = t.translate(msg, "id")
    res_data = res.text
    varout.set(res_data)

def funcIgbo():
    msg = varin.get()
    res = t.translate(msg, "ig")
    res_data = res.text
    varout.set(res_data)

def funcIdo():
    msg = varin.get()
    res = t.translate(msg, "io")
    res_data = res.text
    varout.set(res_data)

# option_language_code(letter j)
def funcJavanese():
    msg = varin.get()
    res = t.translate(msg, "jv")
    res_data = res.text
    varout.set(res_data)

def funcJapanese():
    msg = varin.get()
    res = t.translate(msg, "ja")
    res_data = res.text
    varout.set(res_data)

# option_language_code(letter k)

def funcKorean():
    msg = varin.get()
    res = t.translate(msg, "ko")
    res_data = res.text
    varout.set(res_data)

def funcKyrgyz():
    msg = varin.get()
    res = t.translate(msg, "ky")
    res_data = res.text
    varout.set(res_data)

def funcKhmer():
    msg = varin.get()
    res = t.translate(msg, "km")
    res_data = res.text
    varout.set(res_data)

def funcKazakh():
    msg = varin.get()
    res = t.translate(msg, "kk")
    res_data = res.text
    varout.set(res_data)

def funcKannada():
    msg = varin.get()
    res = t.translate(msg, "kn")
    res_data = res.text
    varout.set(res_data)

# option_language_code(letter l)
def funcLuxembourgish():
    msg = varin.get()
    res = t.translate(msg, "lb")
    res_data = res.text
    varout.set(res_data)

def funcLithuanian():
    msg = varin.get()
    res = t.translate(msg, "lt")
    res_data = res.text
    varout.set(res_data)
    
def funcLatvian ():
    msg = varin.get()
    res = t.translate(msg, "lv")
    res_data = res.text
    varout.set(res_data)

def funcLatin():
    msg = varin.get()
    res = t.translate(msg, "la")
    res_data = res.text
    varout.set(res_data)

def funcLao():
    msg = varin.get()
    res = t.translate(msg, "lo")
    res_data = res.text
    varout.set(res_data)

# option_language_code(letter m)
def funcMongolian():
    msg = varin.get()
    res = t.translate(msg, "mn")
    res_data = res.text
    varout.set(res_data)

def funcMarathi():
    msg = varin.get()
    res = t.translate(msg, "mr")
    res_data = res.text
    varout.set(res_data)

def funcMaori():
    msg = varin.get()
    res = t.translate(msg, "mi")
    res_data = res.text
    varout.set(res_data)

def funcMaltese():
    msg = varin.get()
    res = t.translate(msg, "mt")
    res_data = res.text
    varout.set(res_data)

def funcMalayalam():
    msg = varin.get()
    res = t.translate(msg, "ml")
    res_data = res.text
    varout.set(res_data)

def funcMalay():
    msg = varin.get()
    res = t.translate(msg, "ms")
    res_data = res.text
    varout.set(res_data)

def funcMalagasy():
    msg = varin.get()
    res = t.translate(msg, "mg")
    res_data = res.text
    varout.set(res_data)
    
def funcMacedonian():
    msg = varin.get()
    res = t.translate(msg, "mk")
    res_data = res.text
    varout.set(res_data)

# option_language_code(letter n)

def funcNorwegian():
    msg = varin.get()
    res = t.translate(msg, "no")
    res_data = res.text
    varout.set(res_data)
    
def funcNepali():
    msg = varin.get()
    res = t.translate(msg, "ne")
    res_data = res.text
    varout.set(res_data)

# option_language_code(letter p)
def funcPunjabi ():
    msg = varin.get()
    res = t.translate(msg, "pa")
    res_data = res.text
    varout.set(res_data)

def funcPolish():
    msg = varin.get()
    res = t.translate(msg, "pl")
    res_data = res.text
    varout.set(res_data)

def funcPersian():
    msg = varin.get()
    res = t.translate(msg, "fa")
    res_data = res.text
    varout.set(res_data)

def funcPashto():
    msg = varin.get()
    res = t.translate(msg,"ps")
    res_data = res.text
    varout.set(res_data)

# option_language_code(letter r)
def funcRussian():
    msg = varin.get()
    res = t.translate(msg, "ru")
    res_data = res.text
    varout.set(res_data)

def funcRomanian():
    msg = varin.get()
    res = t.translate(msg, "ro")
    res_data = res.text
    varout.set(res_data)

# option_language_code(letter s)
def funcSwedish():
    msg=varin.get()
    res=t.translate(msg,"sv")
    res_data=res.text
    varout.set(res_data)

def funSundanese():
    msg=varin.get()
    res=t.translate(msg,"su")
    res_data=res.text
    varout.set(res_data)

def funcSwahili():
    msg = varin.get()
    res = t.translate(msg, "swa")
    res_data = res.text
    varout.set(res_data)

def funcSpanish():
    msg = varin.get()
    res = t.translate(msg, "es")
    res_data = res.text
    varout.set(res_data)

def funcSomali():
    msg = varin.get()
    res = t.translate(msg, "so")
    res_data = res.text
    varout.set(res_data)

def funcSlovenian():
    msg = varin.get()
    res = t.translate(msg, "sl")
    res_data = res.text
    varout.set(res_data)

def funcSlovak():
    msg = varin.get()
    res = t.translate(msg, "sk")
    res_data = res.text
    varout.set(res_data)

def funcSindhi():
    msg = varin.get()
    res = t.translate(msg, "sd")
    res_data = res.text
    varout.set(res_data)

def funcShona():
    msg = varin.get()
    res = t.translate(msg, "sn")
    res_data = res.text
    varout.set(res_data)

def funcSerbian():
    msg = varin.get()
    res = t.translate(msg, "sr")
    res_data = res.text
    varout.set(res_data)

def funcSamoan():
    msg = varin.get()
    res = t.translate(msg, "sm")
    res_data = res.text
    varout.set(res_data)

# option_language_code(letter t)
def funcTurkish():
    msg = varin.get()
    res = t.translate(msg, "tr")
    res_data = res.text
    varout.set(res_data)

def funcThai():
    msg = varin.get()
    res = t.translate(msg, "th")
    res_data = res.text
    varout.set(res_data)

def funcTelugu():
    msg = varin.get()
    res = t.translate(msg, "te")
    res_data = res.text
    varout.set(res_data)

def funcTamil():
    msg = varin.get()
    res = t.translate(msg, "ta")
    res_data = res.text
    varout.set(res_data)

def funcTajik():
    msg = varin.get()
    res = t.translate(msg, "tg")
    res_data = res.text
    varout.set(res_data)

# option_language_code(letter u)
def funcUzbek():
    msg = varin.get()
    res = t.translate(msg, "uz")
    res_data = res.text
    varout.set(res_data)


def funcUrdu():
    msg = varin.get()
    res = t.translate(msg, "ur")
    res_data = res.text
    varout.set(res_data)

def funcUkrainian():
    msg = varin.get()
    res = t.translate(msg, "uk")
    res_data = res.text
    varout.set(res_data)

def funcUyghur():
    msg = varin.get()
    res = t.translate(msg, "ug")
    res_data = res.text
    varout.set(res_data)

# option_language_code(letter v)

def funcVietnamese():
    msg = varin.get()
    res = t.translate(msg, "vi")
    res_data = res.text
    varout.set(res_data)

# option_language_code(letter w)

def funcWolof():
    msg = varin.get()
    res = t.translate(msg, "wo")
    res_data = res.text
    varout.set(res_data)

# option_language_code(letter x)
def funcXhosa():
    msg=varin.get()
    res=t.translate(msg,"xho")
    res_data=res.text
    varout.set(res_data)

# option_language_code(letter y)
def funcYoruba():
    msg=varin.get()
    res=t.translate(msg,"en")
    res_data=res.text
    varout.set(res_data)

def funYiddish():
    msg = varin.get()
    res = t.translate(msg, "yid")
    res_data = res.text
    varout.set(res_data)

# option_language_code(letter z)
def funcZulu():
    msg=varin.get()
    res=t.translate(msg,"zu")
    res_data=res.text
    # print(res_data)
    varout.set(res_data)

# language options
options = ["English", "Albanian" ,"Amharic", "Arabic", "Armenian","Azerbaijani","Afrikaans","Amharic","Basque","Belarusian","Bosnian","Bulgarian","Catalan","Chichewa","Chinese","Corsican","Croatian","Czech","Danish","Dutch","English","Estonian","Esperanto","French","Finnish","Fula","Gujarati","Greek","German","Georgian","Galician","Hungarian","Hindi","Herero","Hebrew","Hausa","Haitian Creole","Italian","Indonesian","Igbo","Ido","Icelandic","Javanese","Japanese","Korean","Kyrgyz","Khmer","Kazakh","Kannada","Luxembourgish","Lithuanian","Latvian","Latin","Lao","Mongolian","Marathi","Maori","Maltese","Malayalam","Malay","Malagasy","Macedonian","Norwegian","Nepali","Punjabi","Polish","Persian","Pashto","Russian","Romanian","Swedish","Swahili","Sundanese","Spanish","Somali","Slovenian","Slovak","Sindhi","Shona","Serbian","Samoan","Turkish","Thai","Telugu","Tamil","Tajik","Uzbek","Urdu","Ukrainian","Uyghur","Vietnamese","Wolof","Xhosa","Yoruba","Yiddish","Zulu"]

# mic image
mic_icon = ImageTk.PhotoImage(Image.open("mic.png"))
voice_btn = Button(root, image=mic_icon, width=20,command=voice_search,height=16.5)
voice_btn.grid(row=1, column=0,padx=(220,0))

engine = pyttsx3.init()
voices=engine.getProperty('voices')
text = "Opening Language Translator......Created By BCA Smasher's"
engine.say(text)
# play the speech
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',130)
engine.runAndWait()

# default language
varLanguage = StringVar(root)
varLanguage.set("English") #default value
drop = OptionMenu(root, varLanguage, *options)
drop.grid(row=1, column=1,padx=(100,0))

# Button translator
btn = Button(root, text="Translate", command=funcTranslate)
btn.grid(row=1, column=3)

# clear button
btnClear = Button(root, text="Clear", command=funcClear)
btnClear.grid(row=1, column=4)

# labeling input
lbl=Label(root,text="Enter Text in Any Language",font=20,width=150,foreground="Green")
lbl.grid(row=0,column=0,pady=(20,10),columnspan=5)

# entryin visit
varin=StringVar()
entrin=Entry(root,textvariable=varin,font=20)
entrin.grid(row=1,column=0)

# buttons_row-2
btnHindi=Button(root,text="Hindi",font=20,bg="Yellow",width=20,height=2,command=funcHindi)
btnHindi.grid(row=2,column=0)

btnPunjabi=Button(root,text="Punjabi",font=20,bg="Orange",width=20,height=2,command=funcPunjabi)
btnPunjabi.grid(row=2,column=1)

btnEnglish=Button(root,text="English",font=20,bg="Yellow",width=20,height=2,command=funcEnglish)
btnEnglish.grid(row=2,column=2)

btnBengali=Button(root,text="Bengali",font=20,bg="Orange",width=20,height=2,command=funcBengali)
btnBengali.grid(row=2,column=3)

btnTelugu=Button(root,text="Telugu",font=20,bg="Yellow",width=20,height=2,command=funcTelugu)
btnTelugu.grid(row=2,column=4)

# buttons_row-3
btnUrdu=Button(root,text="Urdu",font=20,bg="Orange",width=20,height=2,command=funcUrdu)
btnUrdu.grid(row=3,column=0)

btnGujarati=Button(root,text="Gujarati",font=20,bg="Yellow",width=20,height=2,command=funcGujarati)
btnGujarati.grid(row=3,column=1)

btnkannada=Button(root,text="Kannada",font=20,bg="Orange",width=20,height=2,command=funckannada)
btnkannada.grid(row=3,column=2)

btnOdia=Button(root,text="Odia",font=20,bg="Yellow",width=20,height=2,command=funcOdia)
btnOdia.grid(row=3,column=3)

btnMalayalam=Button(root,text="Malayalam",font=20,bg="Orange",width=20,height=2,command=funcMalayalam)
btnMalayalam.grid(row=3,column=4)

# buttons_row-4
btnSpanish=Button(root,text="Spanish",font=20,bg="Yellow",width=20,height=2,command=funcSpanish)
btnSpanish.grid(row=4,column=0)

btnFrench=Button(root,text="French",font=20,bg="Orange",width=20,height=2,command=funcFrench)
btnFrench.grid(row=4,column=1)

btnGerman=Button(root,text="German",font=20,bg="Yellow",width=20,height=2,command=funcGerman)
btnGerman.grid(row=4,column=2)

btnChinese=Button(root,text="Chinese",font=20,bg="Orange",width=20,height=2,command=funcChinese)
btnChinese.grid(row=4,column=3)

btnArabic=Button(root,text="Arabic",font=20,bg="Yellow",width=20,height=2,command=funcArabic)
btnArabic.grid(row=4,column=4)

# buttons_row-5
btnRussian=Button(root,text="Russian",font=20,bg="Orange",width=20,height=2,command=funcRussian)
btnRussian.grid(row=5,column=0)

btnPortuguese=Button(root,text="Portuguese",font=20,bg="Yellow",width=20,height=2,command=funcPortuguese)
btnPortuguese.grid(row=5,column=1)

btnJapanese=Button(root,text="Japanese",font=20,bg="Orange",width=20,height=2,command=funcJapanese)
btnJapanese.grid(row=5,column=2)

btnItalian=Button(root,text="Italian",font=20,bg="Yellow",width=20,height=2,command=funcItalian)
btnItalian.grid(row=5,column=3)

btnKorean=Button(root,text="Korean",font=20,bg="Orange",width=20,height=2,command=funcKorean)
btnKorean.grid(row=5,column=4)

# buttons_row-6
btnDutch=Button(root,text="Dutch",font=20,bg="Yellow",width=20,height=2,command=funcDutch)
btnDutch.grid(row=6,column=0)

btnTurkish=Button(root,text="Turkish",font=20,bg="Orange",width=20,height=2,command=funcTurkish)
btnTurkish.grid(row=6,column=1)

btnPolish=Button(root,text="Polish",font=20,bg="Yellow",width=20,height=2,command=funcPolish)
btnPolish.grid(row=6,column=2)

btnSwedish=Button(root,text="Swedish",font=20,bg="Orange",width=20,height=2,command=funcSwedish)
btnSwedish.grid(row=6,column=3)

btnThai=Button(root,text="Thai",font=20,bg="Yellow",width=20,height=2,command=funcThai)
btnThai.grid(row=6,column=4)

# buttons_row-7
btnIndonesian=Button(root,text="Indonesian",font=20,bg="Orange",width=20,height=2,command=funcIndonesian)
btnIndonesian.grid(row=7,column=0)

btnGreek=Button(root,text="Greek",font=20,bg="Yellow",width=20,height=2,command=funcGreek)
btnGreek.grid(row=7,column=1)

btnVietnamese=Button(root,text="Vietnamese",font=20,bg="Orange",width=20,height=2,command=funcVietnamese)
btnVietnamese.grid(row=7,column=2)

btnFinnish=Button(root,text="Finnish",font=20,bg="Yellow",width=20,height=2,command=funcFinnish)
btnFinnish.grid(row=7,column=3)

btnCzech=Button(root,text="Czech",font=20,bg="Orange",width=20,height=2,command=funcCzech)
btnCzech.grid(row=7,column=4)

# buttons_row-8
btnDainsh=Button(root,text="Dainsh",font=20,bg="Yellow",width=20,height=2,command=funcDanish)
btnDainsh.grid(row=8,column=0)

btnNorwegian=Button(root,text="Norwegian",font=20,bg="Orange",width=20,height=2,command=funcNorwegian)
btnNorwegian.grid(row=8,column=1)

btnHungarian=Button(root,text="Hungarian",font=20,bg="Yellow",width=20,height=2,command=funcHungarian)
btnHungarian.grid(row=8,column=2)

btnRomanian=Button(root,text="Romanian",font=20,bg="Orange",width=20,height=2,command=funcRomanian)
btnRomanian.grid(row=8,column=3)

btnCatalan=Button(root,text="Catalan",font=20,bg="Yellow",width=20,height=2,command=funcCatalan)
btnCatalan.grid(row=8,column=4)

# buttons_row-9
btnHebrew=Button(root,text="Hebrew",font=20,bg="Orange",width=20,height=2,command=funcHebrew)
btnHebrew.grid(row=9,column=0)

btnUkrainian=Button(root,text="Ukrainian",font=20,bg="Yellow",width=20,height=2,command=funcUkrainian)
btnUkrainian.grid(row=9,column=1)

btnSlovak=Button(root,text="Slovak",font=20,bg="Orange",width=20,height=2,command=funcSlovak)
btnSlovak.grid(row=9,column=2)

btnAfghanistan=Button(root,text="Afghanistan",font=20,bg="Yellow",width=20,height=2,command=funcAfghanistan)
btnAfghanistan.grid(row=9,column=3)

btnMalay=Button(root,text="Malay",font=20,bg="Orange",width=20,height=2,command=funcMalay)
btnMalay.grid(row=9,column=4)

# buttons_row-10
btnCroatian=Button(root,text="Croatian",font=20,bg="Yellow",width=20,height=2,command=funcCroatian)
btnCroatian.grid(row=10,column=0)

btnLithuanian=Button(root,text="Lithuanian",font=20,bg="Orange",width=20,height=2,command=funcLithuanian)
btnLithuanian.grid(row=10,column= 1)

btnSlovenian=Button(root,text="Slovenian",font=20,bg="Yellow",width=20,height=2,command=funcSlovenian)
btnSlovenian.grid(row=10,column=2)

btnSerbian=Button(root,text="Serbian",font=20,bg="Orange",width=20,height=2,command=funcSerbian)
btnSerbian.grid(row=10,column=3)

btnBulgarian=Button(root,text="Bulgarian",font=20,bg="Yellow",width=20,height=2,command=funcBulgarian)
btnBulgarian.grid(row=10,column=4)


# buttons_row-11
btnEstonian=Button(root,text="Estonian",font=20,bg="Orange",width=20,height=2,command=funcEstonian)
btnEstonian.grid(row=11,column=0)

btnLatvian=Button(root,text="Latvian",font=20,bg="Yellow",width=20,height=2,command=funcLatvian)
btnLatvian.grid(row=11,column=1)

btnIcelandic=Button(root,text="Bulgarian",font=20,bg="Orange",width=20,height=2,command=funcIcelandic)
btnIcelandic.grid(row=11,column=2)

btnAlbanian=Button(root,text="Albanian",font=20,bg="Yellow",width=20,height=2,command=funcAlbanian)
btnAlbanian.grid(row=11,column=3)

btnMacedonian=Button(root,text="Macedonian",font=20,bg="Orange",width=20,height=2,command=funcMacedonian)
btnMacedonian.grid(row=11,column=4)

# entryout visit
varout=StringVar()
entrout=Entry(root,textvariable=varout,font=20)
entrout.grid(row=15,column=0,pady=(10,20))

# Labeling exit
lbl=Label(root,text="Thankyou For Using My Translator",font=20,width=150)
lbl.grid(row=16,column=0,columnspan=5,pady=(20,20))
root.mainloop()