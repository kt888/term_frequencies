from pre_process import Document, TfScores, Index


doc = Document('test_data/test_data.txt')
tf = TfScores(doc)
index = Index('test_data')


def test_document():
    assert doc.word_count == 6
    assert 'test' in doc.words
    assert doc.name == 'test_data.txt'
    assert 'data!.' not in doc.words


def test_tf_scores():
    assert tf.tf_scores['test'] == float(3)/float(6)
    assert tf.tf_scores['this'] == float(1)/float(6)
    assert tf.tf_scores['data'] == float(1)/float(6)


def test_index():
    assert index.tf_score_index['test'] == [('test_data.txt', 0.5)]
    assert index.tf_score_index['data'] == [('test_data.txt', float(1)/float(6))]
