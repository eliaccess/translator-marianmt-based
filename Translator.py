from abc import ABC, abstractmethod
from transformers import MarianMTModel, MarianTokenizer
import time

class Translator(ABC):
    def __init__(self):
        tokenizer = None
        model = None
        src = None
        tar = None
    
    @abstractmethod
    def loadModel(self):
        pass
    
    @abstractmethod
    def translate(self):
        pass
    
class MarianMT_Translator(Translator):
    def loadModel(self, src="fr", tar="en"):
        self.src = src
        self.tar = tar
        model_name = "Helsinki-NLP/opus-mt-"+src+"-"+tar
        tic = time.perf_counter()
        self.tokenizer = MarianTokenizer.from_pretrained(model_name)
        self.model = MarianMTModel.from_pretrained(model_name)
        toc = time.perf_counter()
        print(f"~~~~~~~ Model loaded in {toc - tic:0.4f} seconds ~~~~~~~")
        self.supportedCodes = self.tokenizer.supported_language_codes
        
    def splittingSequence(self, text):
        total = list()
        if len(text) >= 512:
            d = "."
            total =  [e+d for e in text.split(d) if e]
        else:
            total.append(text)
        return total
    
    def translate(self, text):
        tic = time.perf_counter()
        text = ">>"+self.tar+"<< " + text
        text = self.splittingSequence(text)
        translated = self.model.generate(**self.tokenizer(text, return_tensors="pt", padding=True))
        result = [self.tokenizer.decode(t, skip_special_tokens=True) for t in translated]
        toc = time.perf_counter()
        print(f"~~~~~~~ Translated in {toc - tic:0.4f} seconds ~~~~~~~")
        return result