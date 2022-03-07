from sources.Data.DataGetter import DataGetter
import numpy as np
import json
import os


class PhraseExpert:
    def gen_co_occurence_matrice(self):
        self.occ_matrix = np.zeros(shape=(self.nb_unique_words, self.nb_unique_words))
        for i in range(self.nb_corpus_words - 1):
            #print(i, "/", self.nb_corpus_words - 1)
            if self.corpus[i] != '' and self.corpus[i + 1] != '':
                self.occ_matrix[self.unique_words.index(self.corpus[i])][self.unique_words.index(self.corpus[i + 1])] += 1

    def __init__(self, corpus_getter):
        corpus = corpus_getter()
        self.corpus = corpus
        self.nb_corpus_words = len(corpus)
        self.unique_words = list(set(corpus))
        # noinspection PyBroadException
        try:
            self.unique_words.remove('')
        except Exception as e:
            pass
        self.nb_unique_words = len(self.unique_words)
        self.gen_co_occurence_matrice()


    def pick_random_word(self):
        return self.unique_words[np.random.randint(0, len(self.unique_words))]

    def gen_phrase(self, length,word_delimitor=""):
        phrase = [self.pick_random_word()]
        current_word_index = self.unique_words.index(phrase[0])
        for i in range(length - 1):
            words_candidate = np.where(self.occ_matrix[current_word_index] > 0)
            if len(words_candidate[0]) > 0:
                phrase.append(self.unique_words[words_candidate[0][np.random.randint(0, len(words_candidate))]])
            else:
                phrase[-1]+="."
                # phrase.append(".")
                phrase.append(self.pick_random_word())
            current_word_index = self.unique_words.index(phrase[-1])
        print(phrase)
        password=""
        for i in phrase:
            if len(password)>1 and password[len(password)-1]==".":
                i=i.capitalize()
            if i[len(i)-1]!=".":
                password+=i+word_delimitor
            else:
                password+=i
        return password[:len(password)-1]
        # return word_delimitor.join(phrase)


if __name__ == "__main__":
    pe = PhraseExpert(DataGetter.get_ang_sentences)
    print(pe.gen_phrase(10,""))
