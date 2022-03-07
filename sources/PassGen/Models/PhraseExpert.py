from sources.Data.DataGetter import DataGetter
import numpy as np
import json
import os


class PhraseExpert:
    def gen_co_occurence_matrice(self):
        print("nar")
        self.occ_matrix = np.zeros(shape=(self.nb_unique_words, self.nb_unique_words))
        for i in range(self.nb_corpus_words - 1):
            print(i, "/", self.nb_corpus_words - 1)
            if self.corpus[i] != '' and self.corpus[i + 1] != '':
                self.occ_matrix[self.unique_words.index(self.corpus[i])][self.unique_words.index(self.corpus[i + 1])] += 1

    def __init__(self, corpus_getter):
        if os.path.exists(corpus_getter.__name__ + ".json"):
            with open(corpus_getter.__name__ + ".json", 'r') as file:
                print("loading from file")
                phrase_gen_obj = json.load(file)
                self.nb_corpus_words = phrase_gen_obj["nb_corpus_words"]
                self.unique_words = phrase_gen_obj["unique_words"]

                self.occ_matrix = np.loadtxt(corpus_getter.__name__ + ".np")
        else:
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

            phrase_gen_obj = {"nb_corpus_words": self.nb_corpus_words,
                              "unique_words": self.unique_words
                              }

            with open(corpus_getter.__name__ + ".json", 'w') as outfile:
                outfile.write(json.dumps(phrase_gen_obj))

            np.savetxt(corpus_getter.__name__ + ".np", self.occ_matrix)

    def pick_random_word(self):
        return self.unique_words[np.random.randint(0, len(self.unique_words))]

    def gen_phrase(self, length):
        phrase = [self.pick_random_word()]
        current_word_index = self.unique_words.index(phrase[0])
        for i in range(length - 1):
            words_candidate = np.where(self.occ_matrix[current_word_index] > 0)
            if len(words_candidate[0]) > 0:
                phrase.append(self.unique_words[words_candidate[0][np.random.randint(0, len(words_candidate))]])
            else:
                phrase.append(".")
                phrase.append(self.pick_random_word())
            current_word_index = self.unique_words.index(phrase[-1])
        print(phrase)
        return " ".join(phrase)


if __name__ == "__main__":
    #pe = PhraseExpert(DataGetter.get_apple_text_words())
    print("hi")
    pe = PhraseExpert(DataGetter.get_ang_sentences)
    print("coucou")
    print(pe.gen_phrase(10))
