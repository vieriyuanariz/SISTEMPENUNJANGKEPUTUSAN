<?php

import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import json

with open("intents.json") as file:
	data = json.load(file)

print(data["intents"])
?>