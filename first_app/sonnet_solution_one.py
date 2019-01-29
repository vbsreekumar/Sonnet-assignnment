import re, nltk
from first_app import sonnet_helper as sh

# Using the nltk(Natural Language Toolkit) stop words to detect function words that are not necessarily frequent
# within the  sonnet but are frequently used words in the language.
from nltk.corpus import stopwords

def token_frequency(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))


def sonnet_tag(sonnet_number):
    nltk.download("stopwords")

    stop_words = set(stopwords.words('english'))

    st = sh.get_sonnet(sonnet_number)

    # Filtering out the commas from the sonnet.
    s = re.sub(r'[^\w\s]','', st.lower())

    # Tokenizing the sonnet by words.
    wl = s.split()

    # Identifying the stop words in the sonnet.
    unfiltered_sonnet = [w for w in wl if w in stop_words]

    # Identifying the non-stop words in the sonnet
    filtered_sonnet = [w for w in wl if not w in stop_words]

    # Frequency of stop words in the sonnet
    u = token_frequency(unfiltered_sonnet)

    # Frequency of non-stop words in the sonnet
    f = token_frequency(filtered_sonnet)

    # Tagging dictionary
    tagged = dict()

    for i,j in f.items():
        if j==1:
            tagged[i]='important' # Tag words with 1 frequency as 'most important'.
        else:
            tagged[i]='frequent' # Tag words with more than 1 frequency as 'frequent'.

    # These are stop words and cannot be considered as 'most important', therefore, these are tagged as 'frequent'.
    for i,j in u.items():
        tagged[i]='frequent'

    return tagged
