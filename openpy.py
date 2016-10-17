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


def after(value, a):
    # Find and validate first part.
    pos_a = value.rfind(a)
    if pos_a == -1: return ""
    # Returns chars after the found string.
    adjusted_pos_a = pos_a + len(a)
    if adjusted_pos_a >= len(value): return ""
    return value[adjusted_pos_a:]

def get_name(lst):
    for i in lst[:]:
        if i=='':
            lst.remove(i)
    return lst

def italics2txt(data):
    with open ('/Users/dipit/Documents/RA/RA/Columbia/200051/italics.txt', 'a') as f:
        f.write('{}'.format(data))


def quotes2txt(data):
    with open ('/Users/dipit/Documents/RA/RA/Columbia/200051/quotes.txt', 'a') as f:
        f.write('{}'.format(data))

def plain2txt(data):
    with open ('/Users/dipit/Documents/RA/RA/Columbia/200071/titles.txt', 'a') as f:
        f.write('{}'.format(data))

# with open('output.txt', 'r+') as fp:
# 	for i in fp:
# 		# print i
# 		print between(i,"author", ',')
# 		# user=i[i.find("author")+i[1:8]:].split()[1]
# 		# print(user)
# 		# d = dict(regex.findall(i))
# 		# print d	
# # dict