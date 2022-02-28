from sources.Data.DataGetter import DataGetter
import numpy as np


class PhraseExpert:
    def gen_co_occurence_matrice(self):
        self.occ_matrix = np.zeros(shape=(self.nb_unique_words, self.nb_unique_words))
        for i in range(self.nb_corpus_words - 1):
            if self.corpus[i] != '' and self.corpus[i + 1] != '':
                self.occ_matrix[self.unique_words.index(self.corpus[i])][self.unique_words.index(self.corpus[i + 1])] += 1

    def __init__(self, corpus):
        self.corpus = corpus
        self.nb_corpus_words = len(corpus)
        self.unique_words = list(set(corpus))
        self.unique_words.remove('')
        self.nb_unique_words = len(self.unique_words)
        self.gen_co_occurence_matrice()

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
    pe = PhraseExpert(DataGetter.get_apple_text_words())
    print(pe.gen_phrase(5))