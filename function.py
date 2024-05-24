import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#gensim
from gensim.models import Word2Vec
from gensim.models import KeyedVectors

class function:
    def __init__(self):
        return
    
    def text(self,path):
        with open(path) as f:
            text=f.read()
        
        return text
    
    def corpus(self,text,seq_length):
        table=str.maketrans({".":None, "," : None,":" : None,";" : None,"!" : None,'"' :None,"#" :None,"$" :None,"%" :None,"&" :None,"'" :None,'"':None,"(" :None,")" :None,"=" :None,"~" :None,"{" :None,"}" :None,"[" :None,"]" :None,"/":None,"-":None,"_":None,"^":None,"©":None})
        text=text.lower()
        text=text.translate(table)
        words=text.split()
        corpus=[]
        
        for i in range(len(words)-seq_length):
            texts.append(words[i:i+seq_length])
            
        return corpus 

        
    
