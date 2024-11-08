# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1c6OUFMZqpjvleYtpbYp57srmAxPt0YUD
"""

import pandas as pd
baza={
    "FISH": [ "Aliyev Ali", "ALiyeva Aziza" , "Soliyev Bahrom" , "Asrorov Bekzod", "Mo'ydinova Guli", "Abdurahimova Farzona", "Ismoilov Nodir", "Sirojiddinov Asror", "Yigitaliyeva Maftuna", "Bakirov Farrux"           ],
    "Yoshi": [ "11" , "17"  , "19", "20", "21", "21", "18", "19" ,"11" , "17"      ],
     "Jinsi": [ "erkak" , "ayol" , "erkak", "erkak", "ayol", "ayol", "erkak", "erkak", "ayol"  , "erkak"    ],
     "Maktabi": [ "2-maktab", "Prezident maktabi", "11-maktab" , "15-maktab" , "4-maktab" , "9-maktab" , "21-maktab" , "7-maktab" , "3-maktab" , "1-maktab"             ],
     "Manzili": [ "Farg'ona shahar", "Marg'ilon shahar" , "Andijon shahar", "Namangan shahar", "Samarqand shahar", "Nukus shahar", "Andijon shahar", "Andijon shahar", "Namangan shahar", "Toshkent shahar"         ],
     "Tel raqami": [ "99 345 55 66" , "91 567 78 78"    , "90 700 90 71"   , "50 980 55 78"   , "90 500 55 78"   , "90 671 55 78"   , "50 998 55 78"   , "990 823 55 78"   , "50 776 55 78"   , "50 856 55 78"           ],





}
db =pd.DataFrame(baza)
print(db)

filtr =db[db['Jinsi']=="ayol"]
print(filtr)

filtr=db[(db['Jinsi']=="ayol") & (db["Yoshi"]>"15")]
print(filtr)

filtr=db[(db['Jinsi']=="ayol") & (db["Yoshi"]>"15") & (db["Tel raqami"].str.startswith =="90")]
print(filtr)