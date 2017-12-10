import argparse
import pickle
from pre_process import Index

POS_OF_MAX_TF = 0


class Query:
    """
    Query takes in path to directory and a flag called reindex. If reindex
    is false, it reads the tf_score from data/ else, it creates a new Index for
    the documents in the directory and stores them in data/.
    Query.process(word) gives the name of file where the tf score for that word is
    maximum as well as the score
    """
    def __init__(self, path_to_dir="samples", reindex=True):
        if not reindex:
            with open('data/index_data.pkl', 'r') as file:
                self.tf_scores = pickle.load(file)
        else:
            self.tf_scores = Index(path_to_dir).tf_score_index

    def process(self, word):
        if word in self.tf_scores.keys():
            return self.tf_scores[word][POS_OF_MAX_TF]
        return (None, None)


def main(q, words):
    print("Word\tDoc_name\tTF_Score")
    print("------------------------------------------------")
    for word in words:
        filename, tf_score = q.process(word)
        print("{}\t{}\t{}".format(word, filename, tf_score))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='path to input', default='samples')
    parser.add_argument('--reindex', help='Reindex the documents',
                        type=str_2_bool, const=True, nargs='?', default=True)
    parser.add_argument('--words', help='comma separated list of words')
    return parser.parse_args()


def str_2_bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


if __name__ == "__main__":
    args = parse_args()
    words = args.words.split(',')
    reindex = args.reindex
    path = args.path
    print(args)
    q = Query(path, reindex)
    main(q, words)
