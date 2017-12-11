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
python max_tf_score.py --words "whale," --path "samples"
```

* Run all tests

```
pytest
```

## Code Flow

There are two main modules - pre_process.py which has the following classes
* Document
* TfScores
* Index

These classes calculate the tf_scores of all the words in the directory and write it to file in /data
If reindex is set to True, 


