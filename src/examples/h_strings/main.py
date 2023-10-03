#main program

#letter = "A"
#print(letter)

#lang = "python"

#print(len(lang))
#print(lang[2])

import strings

#strings.loop_string_w_while("python")

#strings.loop_string_ww_for("python")
#strings.loop_string_w_special_for("python")

lang = "python"
print (lang[2])
lang = lang.replace ("t", "T")
'''

 replace is just a sequence search
 but can be chained
 lang = lang.replace ("t", "T").replace("o", "O")
 
'''
print (lang)