import pandas as pd
import random

data = pd.read_csv("engmix.csv")

def chooseword():
	index = random.randrange(1,len(data)+1)
	word = (data['WORDS'][index]).upper()

	if not word.isalpha():
		alphanumeric_filter = filter(str.isalpha, word)
		word = "".join(alphanumeric_filter).upper()
	return word	
