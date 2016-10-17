# -- coding: UTF-8 --
# import scholarly


# print(next(scholarly.search_author('Catherine Boone')))

# print (next(scholarly.search_pubs_query('The Political Economy Reader')))



# print next(search_query)


# import gsscraper

# query = "Property and Political Order in Africa"
# gsscraper.get_result(query) # (a)
# gsscraper.get_results(query, 5) # (b)
# # gsscraper.get_result_as_xml(query) # (c)
# import re
# from openpy import after
# bTags1=[]
# x=['UNISDR. 2005. Hyogo Framework for Action \xe2\x80\x93 Extract from Final Report. (New York: United ', 'Nations). ', '', 'UNISDR Terminology on Disaster Risk Reduction. 2009.  ', '', 'The Economist. 2012. \xe2\x80\x9cNatural Disasters: Counting the Cost of Calamities,\xe2\x80\x9d January 14. ', 'http://www.economist.com/node/21542755 ', '', 'Ngozo, Claire. 2012. \xe2\x80\x9cCholera in Time of Floods']
# for i in x:
# 	bTags1.append(after(i,'“'))
# 	# if '“' in i:
# 	# 	print i
#     # quotes = re.findall(r'“([^"]*)“', i)
#     # for quote in quotes:
#     #     bTags1.append(quote)
# print bTags1

# import os
# import sys
# os.system("cd Columbia")
# x=[200041,200042,200043,200051,200052,200061,200062,200071]
# for i in x:
# 	y="mkdir " + str(i)
# 	os.system(y)

# os.system()

def between(value, a, b):
    # Find and validate before-part.
    pos_a = value.find(a)
    if pos_a == -1: return ""
    # Find and validate after part.
    pos_b = value.rfind(b)
    if pos_b == -1: return ""
    # Return middle part.
    adjusted_pos_a = pos_a + len(a)
    if adjusted_pos_a >= pos_b: return ""
    return value[adjusted_pos_a:pos_b]

x=["Inside European Political Parties” in Gallagher, Michael, Michael Laver, and Peter Mair. 2005. Representative Government in Modern Europe. Boston: McGraw Hill." 
 
,"Lipset, Seymour, Stein Rokkan. 1967. “Cleavage Structures, Party Systems, and Voter Alignments: An Introduction.” In: Seymour Lipset, Stein Rokkan (eds.), Party Systems and Voter Alignments: Cross-National Perspectives, 1-64. New York: The Free Press.",
 
"Aldrich, John H. 1995. Why Parties? The Origin and Transformation of Political Parties in America. Chicago: University of Chicago Press, Chapters 1 & 2."]
for i in x:
	print between(i,'. ','. ')





