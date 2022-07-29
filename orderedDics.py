import pickle
from utils import loadPickle,dumpPickle



#Here are your ordered arrays of English keys
past = loadPickle("Sections/Past.txt")
#print("Section in order" , list(past.keys()))

future = loadPickle("Sections/Future.txt")
#print("Section in order" , list(future.keys()))

present = loadPickle("Sections/Present.txt")
#print("Section in order" , list(present.keys()))

conditional = loadPickle("Sections/Conditional.txt")
#print("Section in order" , list(conditional.keys()))

progressive = loadPickle("Sections/Progressive.txt")
print("Section in order" , list(progressive.keys()))

participles = loadPickle("Sections/Participles.txt")
print("Section in order" , list(participles.keys()))

toBe = loadPickle("Sections/To Be & To Have.txt")
#print("Section in order" , list(toBe.keys()))

subjunctive = loadPickle("Sections/Subjunctive.txt")
#print("Section in order" , list(subjunctive.keys()))

futurePerfect = loadPickle("Sections/Future Perfect.txt")
#print("Section in order" , list(futurePerfect.keys()))

presentPerfect = loadPickle("Sections/Present Perfect.txt")
#print("Section in order" , list(presentPerfect.keys()))

pastPerfect = loadPickle("Sections/Past Perfect.txt")
#print("Section in order" , list(pastPerfect.keys()))


past = ['I ate', 'you ate', 'he ate', 'she ate', 'it ate', 'we ate', 'they ate', 'I speak', 'you speak', 'he spoke', 'she spoke', 'it spoke', 'we spoke', 'they spoke', 'I did', 'he/she did', 'you did', 'they did', 'we did', 'I said', 'you \
said', 'he/she said', 'we said', 'they said', 'I went', 'he/she went', 'you went', 'they went', 'we went', 'I got', 'he/she got', 'you got', 'they got', 'we got', 'I made', 'he/she made', 'you made', 'we made', 'they made', 'I knew', 'he/she knew', 
'you knew', 'they knew', 'we knew', 'I thought', 'he/she thought', 'you thought', 'we thought', 'they thought', 'I took', 'he/she took', 'you took', 'we took', 'they took', 'I saw', 'he/she saw', 'you saw', 'we saw', 'they saw', 'I came', 'he/she came', 'you came', 'we came', 'they came', 'I wanted', 'he/she wanted', 'you wanted', 'they wanted', 'we wanted', 'I looked', 'he/she looked', 'you looked', 'we looked', 'they looked', 'I used', 'he/she used', 'you used', 'we used', 'they used', 'I found', 'he/she found', 'you found', 'we found', 'they found', 'I gave', 'he/she gave', 'you gave', 'we gave', 'they gave', 'I told', 'he/she told', 'you told', 'we told', 'they told', 'I worked', 'he/she worked', 'you worked', 'we worked', 'they worked', 'I tried', 'he/she tried', 'you tried', 'we tried', 'they tried', 'I called', 'he/she called', 'you called', 'we called', 'they called', 'I asked', 'he/she asked', 'you asked', 'we asked', 'they asked', 'I needed', 'he/she needed', 'you needed', 'we needed', 'they needed', 'I felt', 'he/she felt', 'you felt', 'we felt', 'they felt']

future = ['I will run', 'He will run', 'she will run', 'you will run', 'they will run', 'we will run', 'I will go', 'He will go', 'She will go', 'You will go', 'They will go', 'We will go', 'I will do', 'he/she will do', 'you will do', 'we will do', 'they will do', 'I will say', 'he/she will say', 'you will say', 'we will say', 'they will say', 'I will get', 'he/she will get', 'you will get', 'we will get', 'they will get', 'I will know', 'he/she will know', 'you will know', 'we will know', 'they will know', 'I will think', 'he/she will think', "you'll think", "we'll think", "they'll think", 'I will take', 'he/she will take', 'they will take', 'we will take', 'I will see', 'he/she will see', 'you will see', 'we will see', 'they will see', 'I will come', 'he/she will come', 'you will come', 'they will come', 'we will come', 'I will want', 'he/she will want', 'you will want', 'they will want', 'we will want', "I'll look", "he'll look", "she'll look", "we'll look", "they'll look", "I'll use", "he'll use", "you'll use", "they'll use", "we'll use", 'I will find', 'he/she will find', 'you will find', 'they will find', 'we will find', 'I will give', 'he/she will give', 'you will give', 'they will give', 'we will give', 'I will tell', 'he/she will tell', 'you will tell', 'they will tell', 'we will tell', 'I will work', 'he/she will work', 'you will work', 'they will work', 'we will work', 'I will try', 'he/she will try', 'you will try', 'they will try', 'we will try', "I'll call", "she'll call", "you'll call", "we'll call", "they'll call", "I'll ask", "he'll ask", 'you will ask', 'we will ask', "they'll ask", 'I will need', 'you will need', 'he/she will need', "we'll need", "they'll need", 'I will feel', 'he/she will feel', 'you will feel', 'we will feel', 'they will feel']

present = ['I speak', 'you speak', 'he/she speaks', 'we speak', 'they speak', 'I do', 'He/she does', 'you do', 'we do', 'they do', 'I say', 'he/she says', 'you say', 'we say', 'they say', 'I go', 'he/she goes', 'you go', 'we go', 'they go', 'I get', 'he/she gets', 'you get', 'we get', 'they get', 'I make', 'he/she makes', 'you make', 'we make', 'they make', 'I know', 'he/she knows', 'you know', 'we know', 'they know', 'I think', 'he/she thinks', 'you think', 'we think', 'they think', 'I take', 'he/she takes', 'you take', 'we take', 'they take', 'I see', 'he/she sees', 'you see', 'we see', 'they see', 'I come', 'he/she comes', 'you come', 'we come', 'they come', 'I want', 'he/she wants', 'you want', 'we want', 'they want', 'I look', 'he/she looks', 'you look', 'we look', 'they look', 'I use', 'he/she uses', 'you use', 'we use', 'they use', 'I find', 'he/she finds', 'you find', 'we find', 'they find', 'I give', 'he/she gives', 'you give', 'we give', 'they give', 'I tell', 'he/she tells', 'you tell', 'we tell', 'they tell', 'I work', 'he/she works', 'you work', 'we work', 'they work', 'I try', 'he/she tries', 'you try', 'we try', 'they try', 'I call', 'he/she calls', 'you call', 'we call', 'they call', 'I ask', ' ', 'he/she asks', 'you ask', 'we ask', 'they ask', 'I need', 'he/she needs', 'you need', 'we need', 'they need', 'I feel', 'he/she feels', 'you feel', 'we feel', 'they feel']

conditional = ['I would go', 'you would go', 'he/she would go', 'they would go', 'we would go', 'I would do', "you'd do", 'he/she would do', "we'd do", "they'd do", 'I would say', 'he/she would say', 'you would say', 'we would say', 'they would say', "I'd get", "she'd get", "you'd get", "they'd get", "we'd get", 'I would know', 'he/she would know', 'you would know', 'we would know', 'they would know', "I'd think", "he'd think", "you'd think", "we'd think", "they'd think", 'I would take', 'she would take', 'you would take', 'we would take', 'they would take', "I'd see", "he'd see", "you'd see", "we'd see", "they'd see", 'I would come', 'he would come', 'you would come', 'we would come', 'they would come', "I'd want", "she'd want", "you'd want", "we'd want", "they'd want", 'I would look', 'he/she would look', 'you would look', 'we would look', 'they would look', 'I would use', 'he/she would use', 'you would use', 'they would use', 'we would use', "I'd find", "he'd find", "you'd find", "they'd find", "we'd find", 'I would give', 'you would give', 'he/she would give', 'they would give', 'we would give', "I'd tell", "she'd tell", "you'd tell", "we'd tell", "they'd tell", "I'd work", "you'd work", "he'd work", "they'd work", "we'd work", 'I would try', 'you would try', 'he would try', 'we would try', 'they would try', "I'd call", "you'd call", "he'd call", "they'd call", "we'd call", 'I would ask', 'he would ask', 'you would ask', 'we would ask', 'they would ask', 'I would need', 'he/she would need', 'you would need', 'we would need', 'they would need', "you'd feel", "I'd feel", "he'd feel", "they'd feel", "we'd feel"]

subjunctive = ['I hope that I say', 'I hope that he says', 'I hope that you say', 'I hope that they say', 'I hope that we say', 'I hope that I go', 'I hope that he/she goes', 'I hope that you go', 'I hope that we go', 'I hope that they go', 'I hope that I do', 'I hope that you do', 'I hope that we do', 'I hope that they do', 'I hope that he does', 'I hope that I speak', 'I hope that she speaks', 'I hope that you speak', 'I hope that we speak', 'I hope that they speak', 'I hope that I get', 
'I hope that you get', 'I hope that we get', 'I hope that he/she gets', 'I hope that they get', 'I hope that I know', 'I hope that you know', 'I hope that we know', 'I hope that they know', 'I hope that I think', 'I hope that you think', 'I hope that we think', 'I hope that I take', 'I hope that you take', 'I hope that they take', 'I hope that I see', 'I hope that you see', 'I hope that we see', 'I hope that they see', 'I hope that he sees', 'I hope that I come', 'I hope that you come', 'I hope that we come', 'I hope that they come', 'I hope that I want', 'I hope that they want', 'I hope that you want', 'I hope that I find', 'I hope that you find', 'I hope that they find', 'I hope that we find', 'I hope that I use', 'I hope that we use', 'I hope that you use', 'I hope that I look', 'I hope that we look', 'I hope that you look', 'I hope that I feel', 'I hope that you feel', 'I hope that we feel', 'I hope that I need', 'I hope that we need', 'I hope that he needs', 'I hope that I ask', 'I hope that she asks', 'I hope that they ask', 'I hope that I give', 'I hope that theygive', 'I hope that she gives', 'I hope that I call', 'I hope that she calls', 'I hope that we call', 'I hope that they call']

toBe = ['to be', 'I am', 'you are', 'he is', 'she is', 'it is', 'they are', 'we are', 'I was', 'you were', 'he was', 'she was', 'it was', 'they were', 'we were', 'I will be', 'you will be', 'He/she will be', 'they will be', 'we will be', 'I would be', 'you would be', 'he/she would be', 'they would be', 'we would be', 'I have been', "you've been", "he's been", "we've been", "they've been", "I've been", "I'm being", "you're being", "they're being", "we're being", "I'll have been", "you'll have been", "he'll have been", "we'll have been", "they'll have been", "I'd have been", "you'd have been", "he'd have been", "we'd have been", "they'd have been"]

"""
pastPerfect = ['I had done', 'he/she had done', 'you had done', 'we had done', 'they had done', 'I had made', "he'd made", "you'd made", "we'd made", "they'd made", 'I had said', 'he/she had said', 'you had said', 'we had said', 'they had said', 
'I had gone', 'he/she had gone', 'you had gone', 'we had gone', 'they had gone', 'I had gotten', 'he had gotten', 'you had gotten', "we'd gotten", "they'd gotten", 'I had known', 'he had known', 'you had known', 'we had known', 'they had known', 'I \ 
had thought', 'she had thought', 'you had thought', 'we had thought', 'they had thought', 'I had taken', 'she had taken', "you'd taken", "they'd taken", "we'd taken", 'I had seen', 'he had seen', 'you had seen', 'they had seen', 'we had seen', 'I had come', 'you had come', 'we had come', 'they had come', 'he had come', 'I had wanted', 'you had wanted', 'he had wanted', 'we had wanted', 'they had wanted', 'I had looked', 'he had looked', 'you had looked', 'they had looked', 'we had looked', 'I \ 
had used', 'you had used', 'we had used', 'they had used', 'she had used', 'I had found', 'you had found', 'we had found', 'he had found', 'I had given', 'you had given', 'he had given', 'we had given', 'they had given', 'I had told', 'you had told', 'we had told', 'I had worked', 'we had worked', 'you had worked', 'I had tried', 'you had tried', 'we had tried', 'I had called', 'you had called', 'we had called', 'I had asked', 'you had asked', 'we had asked', 'I had needed', 'you had needed', 
'we had needed', 'I had felt', 'you had felt', 'we had felt']"""

futurePerfect = ['I will have done', 'you will have done', 'he/she will have done', 'we will have done', 'they will have done', "I'll have said", "you'll have said", "he'll have said", "we'll have said", "they'll have said", "I'll have gone", "you'll have gone", "we'll have gone", "she'll have gone", "they'll have gone", "I'll have gotten", "he'll have gotten", "she'll have gotten", "we'll have gotten", "they'll have gotten", "I'll have known", "you'll have known", "we'll have known", "she'll have known", "they'll have known", "I'll have thought", "you'll have thought", 'we will have thought', "I'll have taken", "you'll have taken", "we'll have taken", "I'll have seen", "you'll have seen", "we'll have seen", "I'll have come", "you'll have come", "they'll have come", "I'll have wanted", "he'll have wanted", "they'll have wanted", "I'll have looked", "you'll have looked", "we'll have looked", "I'll have used", "they'll have used", "you'll have used", "I'll have found", "she'll have \
found", "we'll have found", "I'll have given", "you'll have given", "we'll have given", "I'll have told", "he'll have told", "they'll have told", "I'll have worked", "he'll have worked", "we'll have worked", "I'll have tried", "you'll have tried", "they'll have tried", "I'll have called", "you'll have called", "they'll have called", "I'll have asked", "she'll have asked", "we'll have asked", "I'll have needed", "you'll have neede", "you'll have needed", "we'll have needed", "I'll have felt", "you'll have felt", "they'll have felt"]

presentPerfect = ['I have done', 'you have done', 'he/she has done', 'they have done', 'we have done', 'I have said', 'he/she has said', 'you have said', 'we have said', 'they have said', "I've gone", "you've gone", "he's gone", "they've gone", "we've gone", 'I have gotten', 'you have gotten', 'he/she has gotten', 'we have gotten', 'they have gotten', 'I have made', 'you have made', 'she has made', 'they have made', 'we have made', 'I have known', 'you have known', 'he/she has known', 'they have known', 'we have known', 'I have thought', 'you have thought', 'we have thought', 'he/she has thought', "I've taken", 'you have taken', "we've taken", "they've taken", 'I have seen', 'you have seen', 'we have seen', 'they have seen', 'I have come', 'you have come', 'they have come', 'we have come', 'I have wanted', 'you have wanted', 'he/she has wanted', 'they have wanted', 'I have looked', 'he/she has looked', 'they have looked', 'I have used', 'you have used', 'they have used', 'he/she has used', 'I have found', 'you have found', 'they have found', 'I have given', 'you have given', 'they have given', 'we have given', 'I have told', 'you have told', 'we have told', 'I have worked', "you've worked", "we've worked", "I've tried", "you've tried", "we've tried", "I've called", 'he/she has called', "we've called", "I've asked", "you've asked", "they've asked", "I've needed", "you've needed", "they've needed", "I've felt", 'he/she has felt', "we've felt", "they've felt"]

participles = ['spoken', 'been', 'had', 'gone', 'eaten', 'written', 'jumped', 'done', 'said', 'gotten', 'received', 'thought', 'taken', 'seen', 'wanted', 'looked', 'used', 'found', 'given', 'worked', 'told', 'tried', 'asked', 'needed', 'felt', 'called', 'arisen', 'awoken', 'beaten', 'begun', 'bound', 'blown', 'broken', 'brought', 'built', 'burnt', 'burst', 'caught', 'chosen', 'clapped', 'clung', 'crept', 'dared', 'dealt', 'dug', 'dived', 'drawn', 'dreamt', 'drunk', 'driven', 'dwelt', 'fallen', 'fed', 'fought', 'fitted', 'fled', 'flung', 'flown', 'forbidden', 'foretold', 'forgotten', 'forgiven', 'forsaken', 'frozen', 'grown', 'hanged', 'heard', 'hidden', 'held', 'kept', 'knelt', 'knitted', 'known', 'laid', 'led', 'leaned', 'leaped', 'learned', 'had left', 'had lent', 'had let', 'had lit', 'had lost', 'had made', 'meant', 'had met', 'melted', 'had mistaken', 'had mown', 'had overdrawn', 'overheard', 'overtaken', 'paid', 'proved', 'had put', 'had quit', 'had read', 'ridden', 'had rung', 'risen', 'had run', 'sawed', 'sought', 'had sold', 'had sent', 'had set', 'sewed', 'shaken', 'shorn', 'had shed', 'had shone', 'had shot', 'had shrunk', 'had shut', 'had sung', 'had sunk', 'sat', 'had slain', 'slept', 'had slit', 'had smelt', 
'had snuck', 'had sown', 'had sped', 'spelt', 'spent', 'spilt', 'spun', 'had spat', 'had split', 'spoilt', 'had spread', 'sprung', 'stood', 'had stuck', 'stung', 'stunk', 'stricken', 'had strung', 'stipped', 'striven', 'sunburnt', 'sworn', 'sweated', 'swept', 'swollen', 'swum', 'swung', 'taught', 'torn', 'thrived', 'thrown', 'had thrust', 'trodden', 'had undergone', 'had understood', 'had undertaken', 'had undone', 'had upset', 'woken', 'worn', 'woven', 'wedded', 'wept', 'had won', 'had withdrawn', 'had withheld', 'had withstood', 'had wrung']

progressive =  ['I am speaking', 'you are speaking', 'he is speaking', 'we are speaking', 'they are speaking', 'I will be speaking', 'you will be speaking', 'we will be speaking', 'they will be speaking', 'I was speaking', 'you were speaking', 'he was speaking', 'they were speaking', 'we were speaking', 'would be speaking', 'I am going', 'you are going', 'he is going', 'we are going', 'they are going', 'I would be going', 'you would be going', 'he would be going', 'they would be going', 'we \
would be going', 'I am eating', 'you are eating', 'he is eating', 'they are eating', 'we are eating', 'I will be doing', 'I would be doing', 'I was doing', 'I am doing', 'he will be having', 'he would be having', 'he was having', 'he is having', 'you will be writing', 'you were writing', 'you would be writing', 'you are writing', 'we will be going', 'we were going', 'I will be running', 'I was running', 'I would be running', 'I am running']