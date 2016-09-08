# # -- coding: UTF-8 --
#
# # from linecache import getline
# # with open("output.txt") as f:
# #     for ind, line in enumerate(f,1):
# #         if line.rstrip() == "Reference":
# #             print(getline(f.name, ind+1))
# #
# import re
# z='Mainwaring, Scott, and Timothy R. Scully. 1995. "Introduction: Party Systems in Latin America."'
# r='Hall, Peter A., and Soskice David. 2001. "An Introduction to Varieties of Capitalism," Varieties of Capitalism: The Institutional Foundations of Comparative Advantage. Oxford University Press, Chp. 1, pp. 1-68.'
# i='Tajfel, Henri, and John C. Turner. 2001. "The Social Psychology of Intergroup Relations " Intergroup Relations: Essential Readings, ed. Michael A. Hogg and Dominic Abrams. Psychology Press, 94-109.'
# def quotes(x):
#     quoted = re.compile('"[^"]*"')
#     for value in quoted.findall(x):
#         return value
#
# def quotes_x(x):
#     quoted = re.compile('(.+)"[^"]+"')
#     for value in quoted.findall(x):
#         return value
#
#
# o= z+"\n" + r
# print quotes_x()
# print quotes(z) + "\n" + quotes_x(z)



import re
s ="•  Rogowski, Ronald and Mark Andreas Kayser. . "
s = re.sub(r'[^\w\s]','',s)
print s