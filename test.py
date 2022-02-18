import pickle
with open("adjSections.txt","rb") as fd:
    dic = pickle.load(fd)
    dic.pop("Testing")
print(dic)
with open("adjSections.txt","wb") as fd:
    pickle.dump(dic,fd)