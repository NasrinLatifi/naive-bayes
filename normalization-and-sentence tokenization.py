#!/usr/bin/env python
# -*- coding: utf-8 -*-

#this file does sentence tokenize

from hazm import sent_tokenize


def readData(fileName):
    file = open(fileName, 'r')
    data = file.read().split(u".")
    sample_set = []
    for sample in data:
        if sample.__len__() > 1:
            sample_set.append(sample)
    return sample_set

fileo1 = open("train1.txt", "w")
fileo2 = open("train12.txt", "w")
#reading data
file1 = 'ahmadinejad.txt'
file2 = "mirhossein.txt"
sample_set1 = readData(file1)
sample_set2 = readData(file2)

print('************* SENTENCE TOKENIZATION ***************')
all_sentences1 = []
for sample in sample_set1:
    sentences1 = sent_tokenize(sample)
    all_sentences1.extend(sentences1)
#print(all_sentences)

print('************* SENTENCE TOKENIZATION ***************')
all_sentences2 = []
for sample in sample_set2:
    sentences2 = sent_tokenize(sample)
    all_sentences2.extend(sentences2)

size2 = all_sentences2.__len__()
size1 = all_sentences1.__len__()

for k in range(0, size1):
    fileo1.write(all_sentences1[k] + "\n")


for i in range(0, size2):
    fileo2.write(all_sentences2[i] + "\n")


fileo1.close()
fileo2.close()