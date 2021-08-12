from langdetect import detect

lang = detect("Hola buenos dias como estas")
print(lang)
lang2 = detect("Good morning")
print(lang2)