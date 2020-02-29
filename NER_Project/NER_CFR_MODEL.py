from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all"
%matplotlib inline
import warnings
warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt
#plt.style.use('ggplot')
from itertools import chain

import pandas as pd
import random
import io
import shutil
import nltk
from nltk.tokenize import PunktSentenceTokenizer
import sklearn
import scipy.stats
from sklearn.metrics import make_scorer
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RandomizedSearchCV

import sklearn_crfsuite
from sklearn_crfsuite import scorers
from sklearn_crfsuite import metrics


nltk.corpus.conll2002.fileids()

%%time
train_sents=list(nltk.corpus.conll2002.iob_sents('esp.train'))
test_sents=list(nltk.corpus.conll2002.iob_sents('esp.testb'))

# for taking input from file:

path='F:\Paul Data Science\Python Projects\Project I O\\test_input.txt'
leng=0

with open(path, 'r') as f1:
    paragraph=f1.readlines()
with open('F:\Paul Data Science\Python Projects\Project I O\\test_input.txt', 'r') as f:
    for leng,j in enumerate(f):
        pass

leng=leng+1    

#execute:

path='F:\Paul Data Science\Python Projects\Project I O\\test_input.txt' // Give your os path by importins OS python module

r1 = random.randint(0, 50)
with open(path, 'w') as f1:
    f1.write(str(test_sents[r1]))
print(r1)    

train_sents=list(nltk.corpus.conll2002.iob_sents('esp.train'))
#[[('Melbourne', 'NP', 'B-LOC')]]
test_sents=[[tuple(paragraph[i].split(" ")) for i in range(leng)]]
print(test_sents)        


# for taking input from file:

test_sents=[paragraph[i] for i in range(leng)]

sent_tokens=[]
for i in range(leng):
    tokens=nltk.sent_tokenize(test_sents[i])
    sent_tokens.append(tokens)
        

print(sent_tokens)

sent_tokens = []
for l in test_sents:
    for item in l:
        sent_tokens.append(item)


#exeute:

def word2features(sent, i):
    word=sent[i][0]
    postag=sent[i][1]
    
    features={
        'bias': 1.0,
        'word.lower()': word.lower(),
        'word[-3:]': word[-3:],
        'word.isupper()': word.isupper(),
        'word.istitle()': word.istitle(),
        'postag': postag,
        'postag[:2]': postag[:2],
    }
    if i > 0:
        word1=sent[i-1][0]
        postag1=sent[i-1][1]
        features.update({
            '-1:word.lower()': word1.lower(),
            '-1:word.istitle()': word1.istitle(),
            '-1:word.isupper()': word1.isupper(),
            '-1:postag': postag1,
            '-1postag[:2]': postag[:2],
        })
    else:
        features['BOS']=True
    
    if i < len(sent)-1:
        word1=sent[i+1][0]
        postag1=sent[i+1][1]
        features.update({
            '+1:word.lower()': word1.lower(),
            '+1:word.istitle()': word1.istitle(),
            '+1:word.isupper()': word1.isupper(),
            '+1:potag': postag1,
            '+1:postag[:2]': postag1[:2],
        })
    else:
        features['EOS']=True
    return features



def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]

def sent2labels(sent):
    return [label for token, postag, label in sent]

def sent2tokens(sent):
    return [token for token, postag, label in sent]

def sent2features2(sent):
    return [word2features2(sent, i) for i in range(len(sent))]

X_train = [sent2features(s) for s in train_sents]
y_train = [sent2labels(s) for s in train_sents]

X_test = [sent2features(s) for s in test_sents]
y_test = [sent2labels(s) for s in test_sents]


#execute:

path='F:\Paul Data Science\Python Projects\Project I O\\test_input.txt'

my_list=[]

for i in test_sents[r1]:
    my_list.append(i[0])
print(my_list)
            


r1 = random.randint(0, 50)
with open(path, 'w') as f1:
    f1.write(str(my_list))
print(r1)    


#execute

crf = sklearn_crfsuite.CRF(
    algorithm='lbfgs',
    c1=0.1,
    c2=0.1,
    max_iterations=100,
    all_possible_transitions=True,
)


%%time
crf.fit(X_train, y_train)

list_of_tuples=list(zip(my_list, y_pred[r1]))

print(list_of_tuples)

df=pd.DataFrame(list_of_tuples, columns=['Named-Entity','Class-lebel'])


#execute

path2='F:\Paul Data Science\Python Projects\Project I O\\test_results.txt'
with open(path2, 'w+') as f2:
    f2.write('\n\nOutput: lebels-- ')
    for item in y_pred[r1]:
        f2.write("[%s] " % item)
                
path3='F:\Paul Data Science\Python Projects\Project I O\\merged_output.txt'
with open(path3, 'a+') as f3:
    pass


# execute

# Python Program - Merge Two Files


filename1 = f1
filename2 = f2
filename3 = f3

print();
print("Merging the content of two file in",f3.name);
with open(path3, "ab") as wfd:
    for f in [path, path2]:
        with open(f, "rb") as fd:
            shutil.copyfileobj(fd, wfd, 1024*1024*10);


#group B and I results:
sorted_labels=sorted(
    labels,
    key=lambda name: (name[1:], name[0])
)
print(metrics.flat_classification_report(
    y_test,y_pred,labels=sorted_labels,digits=3
))


#Hyper parameter optimization:-
crf=sklearn_crfsuite.CRF(
    algorithm='lbfgs',
    max_iterations=100,
    all_possible_transitions=True
)
params_space={
    'c1': scipy.stats.expon(scale=0.5),
    'c2': scipy.stats.expon(scale=0.05)
    
}
#use the same metric for evaluation
f1_scorer=make_scorer(metrics.flat_f1_score,
                      average='weighted',labels=labels)
# search
rs=RandomizedSearchCV(crf,params_space,
                      cv=3,
                      verbose=1,
                      n_jobs=1,
                      n_iter=5,
                      #n_iter=50,
                      scoring=f1_scorer)
rs.fit(X_train, y_train)


#score after hyper parameter (c1, c2) optimization:-
new_pred=rs.predict(X_test)
metrics.flat_f1_score(y_test,new_pred,average='weighted',labels=labels)

#Finding the best CRF:-

print('best paams: ',rs.best_params_)
print('best_CV score: ',rs.best_score_)
print('model size: {:0.2f}M'.format(rs.best_estimator_.size_ / 1000000))


#Scatter ploting Best Hyper Parameters:-

_x= [s for s.parameters['c1'] in rs.grid_scores_]
_y= [s for s.parameters['c2'] in rs.grid_scores_]
_c= [s for s.mean_validation_score in rs.grid_scocres_]

fig=plt.figure()
fig.set_vscale('log')
ax=plt.gca()
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlabel('c1')
ax.set_ylabel('c2')
ax.set_tittle("Randomizedsized Hyparameter Search CV Results (min={:0.3}, max={:0.3})".format(
    min(_c), max(_c)
))

ax.sctter(_x,_y,c=_c,s=60, alpha=0.9,edgecolor=[0,0,0])

print("Dark blue =>", min(_c)," dark red => ", max(_c))


print(metrics.flat_classification_report(
    y_test,new_pred,labels=sorted_labels,digits=3
))

shutil.copyfileobj?

for i in range(2):
    print(i)

