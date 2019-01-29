import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file = os.path.join(BASE_DIR, "sonnet_project/sonnet_dataset.txt")
csvfile = os.path.join(BASE_DIR, "sonnet_project/sonnet_csv.csv")


l = []
nl = []

with open(file) as input_data:
    for line in input_data:
        if line.strip() == '0':
            break
    for line in input_data:
        if line.strip() == '155':
            break
        nl.append(line.strip())
        l.append(line.strip().replace(","," ").replace("."," ").replace("?"," ").replace("\n\t\s"," "))

while '' in l:
    l.remove('')


for i in range(len(l)):
    if l[i].isdigit():
        l[i] = int(l[i])
    else:
        l[i] = l[i]+' '

sonnet = {}
s= ''
for i in range(len(l)):
    z = i
    if type(l[z])==int:
        j = i
        while(type(l[j])==str):
            s=s+l[j]
            j=j+1
        sonnet[l[i]] = i
sonnet[155] = len(l)

s_d = {}
for i in range(1,155):
    s = ''
    a = sonnet[i]
    b = sonnet[i+1]
    for x in range(a+1, b):
        s+=l[x]
        s_d[i] = s

# Obtain the complete dataset in a dictionary format. key=sonnet number and value=sonnet
def get_dataset():
    return s_d

# Obtain the ith sonnet.
def get_sonnet(i):
    return s_d[i]
