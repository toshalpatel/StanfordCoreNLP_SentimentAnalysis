import nltk
import re
import pandas as pd
from pycorenlp import StanfordCoreNLP
import sys
import time
import subprocess

def get_clean_text(text):
    fstr = re.sub("[^A-Za-z.']+", ' ', text)
    return fstr

data = pd.read_csv("~/oh_textmining/combined_sentences_141119.csv")

def get_pennt(text):
    text_file = open("eg.txt", "w")
    text_file.write(text)
    text_file.close()
    proc = subprocess.run("java -mx4g -cp \"/NAS/home01/toshal/stanford-corenlp-full-2018-10-05/*\" edu.stanford.nlp.sentiment.SentimentPipeline -file eg.txt -output PENNTREES ", stdout=subprocess.PIPE, shell=True)
    #proc.stdin.write(text)
    #f = open("demofile.txt", "r")
    #print(proc.communicate())
    pennt = proc.stdout
    result = re.search('\n(.*)\n', pennt.decode("utf-8"))
    pennt=result.group(1)
    print(pennt)
    return pennt
    
    
time.sleep(2)

data['penn_t'] = data['text'].apply(lambda row:get_clean_text(row))

for i in data.index:
    try:
        data.loc[i,'penn_t'] = get_pennt(data.loc[i,'text'])
    except:
        continue
    
print(data['penn_t'])
data.to_csv("combined_sentences_141119_with_penn.csv", index=None)
