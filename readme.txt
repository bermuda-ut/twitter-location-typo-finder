Requires Python 3
         Java 8

#### Installation ####

Install NLTK:
    sudo pip3 install -U nltk
    sudo pip3 install -U ngram

Then install following required packages for NLTK using nltk.download():
    brown
    wordnet
    stopwords
    averaged_perceptron_tagger
    punkt
    names


#### Tutorial ####

STEP1
    First, let's do some pre-processing.

        cd preProcess
        python3 ./main.py <US-loc-names> <X_tweets.txt>

    Now terminal should wait for command

    Type d, this will build the dictionary.
    Type t, this will build the tweets.

    The processed file have "-minXX.txt" or "-custom.txt" at the end of the file name.
    Both processing time should take less than a minute (calculated on big file).

STEP2
    Now that we have pre-processed, let's look for some typos.

    First, Global Edit Distance

    Go to bin/ directory in the project root and run 'Program':
        cd bin
        java Program <processed-dict> <processed-tweet> > ged-output.txt

    output.txt will have output of typos and Tweet IDs.
    Note that you can pipe log with 2>

STEP3
    For N-Gram, in bin folder:
        python3 ./ngramProcess <processed-dict> <processed-tweet> > ngram-output.txt


#### Further Information ####

Global Edit Distance and N-Gram outputs to stdout and logs to stderr

Output format is:
typo    tweetId tweetId ..
Note that the big gaps are tabs
