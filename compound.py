#compound conditions
#and both sides have to be true to evaluate as true
#or 1 side have to be true to evaluate as true
#not  De Morgna's Law
# order is Not then And then Or


x = 2
y = 4

compound = False or y + 2 > 3
print(compound)

compond = not True == False
print(compond)

compoud = True or False and not True or False
#True or False and False or False
#True or False or False
#True
print(compoud)

comp = not (True or False) and not False or 2 < 3 or True
print(comp)


#DeMorgan's Law
#not (x and y) == (not x) or (not y)
#not (x or y) == not x and not y
not(w and z or (not w))
#not ((w and z) or (not w))
#(not (w and z)) and (not (not w))
#((not w) or (not z)) and w
#not w or not z and w
# it is 2 ^ (number of variables) this gives you the lenght of the columns


'''
W Z
---
T F > True
F F > True
T T > False
F T > True
'''

not true or not True or True