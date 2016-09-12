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
# #     for value in quoted.findall(x):
# #         return value
# #
# #
# # o= z+"\n" + r
# # print quotes_x()
# # print quotes(z) + "\n" + quotes_x(z)
#
#
#
# import re
# import string
#
# s ="•  Rogowski, Ronald and Mark Andreas Kayser. . "
# s = re.sub(r'[^\w\s]','',s)
# print s
#
# p= ['hello', '...', 'h3.a', 'ds4,']
# x = [''.join(x for x in par if x not in string.punctuation) for par in p]
# print x
#
# j= ['world', 'good', 'plce']
#
# print x + j
#
# z=zip(x,j)
# print "zipped:", z
# print "djc", z[1][1]
# i=0
# j=0
# for i in range(3):
#     print " test " + z[i][0]  + " succeed " + z[i][1]
#
# # for i, j in range(0,4):
# #     print  z[i][j]
import re
from string import digits
import string
identity = string.maketrans("", "")
t = ['\xe2\x80\xa2  Migdal, Joel. 1997. ', '\xe2\x80\xa2  Ziblatt, Daniel. 2004. ', '\xe2\x80\xa2  Ganev, Venelin I. 2005. ', '\xe2\x80\xa2  Putnam, Robert D. 1995. ', '\xe2\x80\xa2  Berman, Sheri. 1997. ', '\xe2\x80\xa2  Haddad, Mary Alice. 2006. ', '\xe2\x80\xa2  Henderson, Sarah. 2002. ', '\xe2\x80\xa2  Kubik, Jan. 2005. ', '\xe2\x80\xa2  Melucci, Alberto. 1994. "A Strange Kind of Newness: What\'s "New', '\xe2\x80\xa2  Goodwin, Jeff, and James M. Jasper. 2004. ', '\xe2\x80\xa2  Gould, Deborah. 2004. ', '\xe2\x80\xa2  Swidler, Ann. 1986. ', '\xe2\x80\xa2  Tajfel, Henri, and John C. Turner. 2001. ', '\xe2\x80\xa2  Wedeen, Lisa. 2002. ', '\xe2\x80\xa2  Wright, Erik Olin. 2005. "Introduction" and ', '\xe2\x80\xa2  Hancock, Ange-Marie. 2007. ', '\xe2\x80\xa2  Baldez, Lisa. 2010. ', '\xe2\x80\xa2  Fearon, James D., and David D. Laitin. 2003. ', '\xe2\x80\xa2  Staniland, Paul. 2012. ', '\xe2\x80\xa2  Levitsky, Steven and Lucan Way. 2002. ', '\xe2\x80\xa2  Treir, Shawn, and Simon Jackman. 2008. ', '\xe2\x80\xa2  Carothers, Thomas. 2002. ', '\xe2\x80\xa2  Way, Lucan, and Steven Levitsky. 2007. ', '\xe2\x80\xa2  Hall, Peter A., and Rosemary C. R.  Taylor. 1998. ', '\xe2\x80\xa2  Moe, Terry M. 2005. ', '\xe2\x80\xa2  March, James G., and Johan P. Olsen. 2006. ', '\xe2\x80\xa2  Kitschelt, Herbert. 2000. ', '\xe2\x80\xa2  Bates, Robert H. 1981. ', '\xe2\x80\xa2  Rodrik, Dani. 1996. ', '\xe2\x80\xa2  Hellman, Joel. 1998. ', '\xe2\x80\xa2  Canes-Wrone, Bradice and Jee-Kwang Park.  2012. ', '\xe2\x80\xa2  Hall, Peter A., and Soskice David. 2001. ', '\xe2\x80\xa2  Moene, Karl O. and Michael Wallerstein. 2001. ', '\xe2\x80\xa2  Rogowski, Ronald and Mark Andreas Kayser. 2002. ']

p =['Migdal Joel1997', 'test+']
y = [s.translate(identity, "0123456789") for s in p]
print y