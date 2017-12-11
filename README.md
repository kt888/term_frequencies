# term_frequencies

## How to run

```
git clone git@github.com:kt888/term_frequencies.git
cd term_frequencies
```

* More than 1 word
```
python max_tf_score.py --words "whale,sea,queequeg" --path "samples"
```

* 1 word 
```
python max_tf_score.py --words "whale" --path "samples"
```

* Run all tests

```
pytest
```

## Code Flow

There are two main modules - pre_process.py which has the following classes
> module pre_process.py
* Document
* TfScores
* Index

These classes calculate the tf_scores of all the words in the directory and write it to file in /data
If reindex is set to True, the files in samples/ are read and tf scores are calculated. Otherwise, the tf_scores are
read from /data/index_data.pkl.

> module max_tf_score
* This module has the Query class which takes in a word and outputs the file with the max tf_score for that word and the word.

For eg, for the given words whale,sea,queequeg the results are
```
Word	Doc_name	TF_Score
------------------------------------------------
whale	mobydick-chapter1.txt	0.00135440180587
sea	mobydick-chapter1.txt	0.00451467268623
queequeg	mobydick-chapter4.txt	0.00663449939686
```

Note: while processing the files, I did not remove the 's. For eg, queequeg's is different from queequeg. The punctuations have been stripped, text is converted to lower case and split by space.



