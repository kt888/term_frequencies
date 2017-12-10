from max_tf_score import Query


def test_query():
    query = Query('test_data')
    assert query.process('test') == ('test_data.txt', 0.5)
    assert query.process('data') == ('test_data.txt', float(1)/float(6))
    assert query.process('not') == (None, None)

