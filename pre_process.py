import re
import os
import pickle
import doctest
from collections import defaultdict


class Document:
    def __init__(self, path):
        self.path = path
        self.content = self.__read_document_content()
        self.__normalization().__lower_case().__split_file()

    def __read_document_content(self):
        with open(self.path, 'r') as file:
            return file.read()
            
    def __normalization(self):
        self.content = re.sub(r'[^\w\s]', '', self.content)
        return self

    def __lower_case(self):
        self.content = self.content.lower()
        return self

    def __split_file(self):
        self.content = self.content.split()
        return self

    @property
    def word_count(self):
        return len(self.content)

    @property
    def words(self):
        return self.content

    @property
    def name(self):
        return self.path.split('/')[-1]


class TfScores:
    def __init__(self, document):
        self.document = document
        self.tf_scores = defaultdict(float)
        self.__word_count().__tf_scores()

    def __word_count(self):
        for word in self.document.words:
            self.tf_scores[word] += 1
        return self

    def __tf_scores(self):
        for word, count in self.tf_scores.items():
            self.tf_scores[word] = count/self.document.word_count
        return self


class Index:
    def __init__(self, directory_path):
        self.__required_files = self.__required_files(directory_path)
        self.__tf_score_index = defaultdict(list)
        self.__process_files().__sort_scores()
        with open('data/index_data.pkl', 'w') as file:
            pickle.dump(self.__tf_score_index, file)

    def __required_files(self, directory):
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                yield '{}/{}'.format(directory, filename)

    def __process_files(self):
        for file in self.__required_files:
            document = Document(file)
            tf_scores = TfScores(document).tf_scores
            for word, tf_score in tf_scores.items():
                self.__tf_score_index[word].append((document.name, tf_score))
        return self

    def __sort_scores(self):
        for word, tf_scores in self.__tf_score_index.items():
            self.__tf_score_index[word] = sorted(tf_scores, key=lambda x: -x[1])

    @property
    def tf_score_index(self):
        return self.__tf_score_index


if __name__ == "__main__":
    doctest.testmod()