from pre_process import Document, TfScores, Index


d = Document('test/test_data.txt')
t = TfScores(d)


def test_document():
    assert d.word_count == 6
    assert 'test' in d.words
    assert d.name == 'test_data.txt'
    assert 'data!.' not in d.words


def test_tf_scores():
    assert t.tf_scores['test'] == float(3)/float(6)
    assert t.tf_scores['this'] == float(1)/float(6)
    assert t.tf_scores['data'] == float(1)/float(6)


def test_index():
    i = Index('test')
    assert i.tf_score_index['test'] == [('test_data.txt', 0.5)]
    assert i.tf_score_index['data'] == [('test_data.txt', float(1)/float(6))]
