{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf460
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;\red16\green19\blue26;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl358\partightenfactor0

\f0\fs26 \cf2 \expnd0\expndtw0\kerning0
\
from __future__ import division\
from math import log10\
import glob\
import sys\
import os\
#from NBClassifier import NBClassifier\
from collections import defaultdict\
from collections import Counter\
\
def main():\
   # if len(sys.argv) != 1:\
    #    print "Error:Need atleast 1 path "\
    #    return\
    #train_path="/Users/manasranjanmahanta/Downloads/op_spam_train"\
    train_path = sys.argv[1]\
    '''\
    stopWords=["a","about","again","all","am","an","and","any","are","aren't","as","at","be","been","before","being","below","both","but","by","doing","don't","down","during","each","few","for","from","having","he","he'd","he'll","he's","her","here","here's","hers","herself","him","himself","his","how","how's"]\
    stopWords.extend(["i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's","its","itself","let's","me","more","mustn't"])\
    stopWords.extend(["my","myself","no","nor","not","of","off","on","once","only","or","other","ought","our","ours","ourselves","out","over","own"])\
    stopWords.extend(["same","shan't","she","she'd","she'll","she's","so","some","such","than","that","that's","the","their"])\
    stopWords.extend(["theirs","them","then","there","these","they","they'd","they'll","they're","they've","this","those"])\
    stopWords.extend(["to","too","until","up","very","was","wasn't","we","we'd","we'll","we're","we've","were","weren't","what"])\
    stopWords.extend(["what's","when","when's","where","where's","which","while","who","who's","whom","why","why's","with"])\
    stopWords.extend(["you","","you'd","you'll","you're","you've","your","yours","yourself","i"])\
    '''\
\
    #print len(stopWords)\
    stopWords= ['secondly', 'all', 'consider', 'whoever', 'results', 'four', 'edu', 'go', 'mill', 'evermore', 'causes', 'seemed', 'rd', 'certainly', 'biol', 'system', "when's", 'vs', 'ts', 'to', 'asking', 'present', 'th', 'under', 'sorry', 'promptly', "a's", 'mug', 'sent', 'outside', 'far', 'mg', 'every', 'yourselves', "we'll", 'went', 'did', 'forth', "they've", 'fewer', 'hereafter', 'try', 'p', 'thereupon', 'round', 'added', "it'll", "i'll", 'someday', 'approximately', 'says', "you'd", 'ten', 'yourself', 'd', 'past', 'likely', 'invention', 'notwithstanding', 'further', 'shows', 'even', 'index', 'what', 'appear', 'giving', 'section', 'brief', 'run', 'goes', 'sup', 'new', 'poorly', 'ever', 'thin', 'full', "c'mon", 'whose', 'youd', 'respectively', 'sincere', 'never', 'here', 'himse\\xe2\\x80\\x9d', 'let', 'others', 'along', 'fifteen', 'suggest', 'obtained', 'ref', 'ahead', 'k', 'allows', 'proud', 'amount', "i'd", 'resulting', 'howbeit', 'usually', 'whereupon', "i'm", 'makes', 'thereto', 'thats', 'hither', 'via', 'followed', 'merely', 'while', 'till', 'ninety', 'vols', 'viz', 'ord', 'readily', 'everybody', 'use', 'from', 'would', 'contains', 'two', 'next', 'few', 'call', 'therefore', 'taken', 'themselves', 'thru', 'tell', 'more', 'knows', 'becomes', 'hereby', 'herein', 'particular', 'known', "who'll", 'must', 'me', 'none', 'thanks', 'f', 'this', 'ml', 'oh', 'anywhere', 'nine', 'can', 'mr', 'following', 'my', 'example', 'indicated', 'give', 'neverf', 'states', 'indicates', 'something', 'want', 'arise', 'information', 'needs', 'end', 'thing', 'rather', 'meanwhile', 'id', 'how', 'low', "'ve", 'instead', 'de', 'okay', 'tried', 'may', 'stop', 'after', 'eighty', 'different', 'hereupon', 'whilst', 'ff', 'date', 'such', 'undoing', 'a', 'thered', 'third', 'whenever', 'maybe', 'appreciate', 'q', 'ones', 'so', 'specifying', 'allow', 'keeps', "that's", 'thirty', 'six', 'help', 'indeed', 'over', 'move', 'mainly', 'soon', 'course', 'through', 'looks', 'fify', 'still', 'its', 'refs', 'before', 'thank', "he's", 'selves', 'inward', 'fix', 'actually', 'better', 'whether', 'willing', 'whole', 'thanx', 'ours', 'might', "haven't", 'versus', 'then', 'non', 'someone', 'somebody', 'thereby', 'auth', 'underneath', "you've", 'they', 'half', 'now', 'nos', 'several', 'name', 'always', 'reasonably', 'whither', "she's", 'sufficiently', 'each', 'found', 'entirely', 'mean', 'everyone', 'directly', 'doing', 'ed', 'eg', 'related', 'tip', 'owing', 'ex', 'substantially', 'et', 'beyond', 'couldnt', 'out', 'by', 'them', "needn't", 'furthermore', 'since', 'forty', 'research', 'looking', 're', 'seriously', "shouldn't", "they'll", 'got', 'cause', "one's", "you're", 'million', 'given', 'quite', "what'll", 'que', 'besides', 'x', 'ask', 'anyhow', 'beginning', 'backwards', 'g', 'could', 'hes', 'put', 'tries', 'keep', 'caption', 'w', 'ltd', 'hence', 'onto', 'think', 'first', 'myse\\xe2\\x80\\x9d', 'already', 'seeming', 'omitted', 'thereafter', 'thereof', 'awfully', 'done', 'adopted', 'another', 'thick', 'miss', "doesn't", 'little', 'necessarily', 'their', 'together', 'top', 'accordingly', 'least', 'anyone', 'indicate', 'too', 'hundred', 'gives', 'mostly', 'that', 'nobody', 'took', 'immediate', 'resulted', 'regards', 'somewhat', 'off', 'believe', 'herself', 'than', "here's", 'begins', 'b', 'unfortunately', 'showed', 'accordance', 'gotten', 'second', 'i', 'r', 'amid', 'toward', 'minus', 'are', 'and', 'youre', 'ran', 'thoughh', 'alongside', 'beforehand', 'mine', 'say', 'unlikely', 'have', 'need', 'seen', 'seem', 'saw', 'any', 'relatively', 'zero', 'thoroughly', 'latter', 'downwards', 'aside', 'thorough', 'predominantly', 'also', 'take', 'which', 'begin', 'exactly', 'unless', 'opposite', 'who', "where's", 'most', 'eight', 'but', 'significant', 'why', 'sub', 'forever', 'kg', 'especially', 'noone', 'later', 'm', 'amoungst', 'mrs', 'heres', "you'll", 'definitely', 'neverless', 'effect', 'normally', 'came', 'saying', 'particularly', 'show', 'anyway', 'page', 'ending', "that'll", 'find', 'fifth', 'one', 'specifically', 'keys', "daren't", 'behind', 'should', 'only', 'going', 'specify', 'announce', 'itd', "there've", 'do', 'his', 'above', 'get', 'between', 'overall', 'truly', "they'd", 'hid', 'nearly', 'words', 'despite', 'during', 'him', 'regarding', 'qv', 'h', 'cry', 'state', 'twice', 'she', 'though', 'contain', "what've", 'where', 'greetings', 'ignored', 'km', 'theirs', 'up', 'namely', 'computer', 'sec', 'anyways', "that've", 'throug', 'no-one', 'best', 'wonder', 'said', "there'd", 'away', 'currently', 'please', 'ups', 'enough', "there's", 'various', 'hopefully', 'affecting', 'probably', 'neither', 'across', 'co.', 'available', 'we', 'recently', 'useful', 'importance', 'were', 'however', 'meantime', 'come', 'both', 'c', 'last', 'thou', 'many', 'taking', 'thence', 'according', 'against', 'etc', 's', 'became', 'com', 'otherwise', 'among', 'liked', 'co', 'afterwards', 'seems', 'ca', 'whatever', 'alone', 'moreover', 'throughout', 'considering', "he'd", 'pp', 'described', "it's", 'three', 'been', 'quickly', 'whom', "there're", 'much', 'wherein', 'interest', 'certain', 'whod', 'hardly', "it'd", 'wants', 'corresponding', 'fire', 'latterly', 'concerning', 'else', 'hers', 'former', 'those', 'myself', 'novel', 'look', 'unlike', 'these', 'means', 'bill', 'twenty', 'value', 'n', 'will', 'near', 'theres', 'seven', 'whereafter', 'almost', 'wherever', 'is', 'thus', 'it', 'itself', 'im', 'in', 'affected', 'ie', 'y', 'if', 'containing', 'anymore', 'perhaps', 'insofar', 'make', 'same', 'clearly', 'beside', 'when', 'potentially', 'widely', 'gets', 'fairly', 'used', 'slightly', 'see', 'somewhere', 'I', 'upon', 'herse\\xe2\\x80\\x9d', 'uses', 'yours', "he'll", 'wheres', 'recent', 'lower', 'kept', 'whereby', 'largely', 'nevertheless', 'changes', 'nonetheless', 'well', 'anybody', 'obviously', 'without', 'comes', 'very', 'the', 'con', 'self', 'inc.', 'lest', 'things', 'world', "she'll", 'just', 'less', 'being', 'able', 'therere', 'presumably', 'front', 'farther', 'immediately', 'regardless', 'yes', 'yet', 'unto', 'wed', "we've", 'had', 'except', 'thousand', 'lets', 'has', 'adj', 'ought', 'gave', "t's", 'around', "who's", 'possible', 'usefully', 'possibly', 'whichever', 'five', 'know', 'similarly', 'using', 'part', "who'd", 'dare', 'apart', 'abst', 'nay', 'necessary', 'like', 'follows', 'noted', 'either', 'become', 'whomever', 'towards', 'therein', "why's", 'www', 'because', 'old', 'often', 'successfully', 'some', 'back', 'l', 'ah', 'sure', 'shes', 'specified', 'home', 'theyre', 'ourselves', 'happens', 'provided', 'vol', "there'll", 'for', 'bottom', 'affects', 'shall', 'per', 'everything', 'does', 'provides', 'tends', 't', 'be', 'sensible', 'obtain', 'nowhere', 'although', 'sixty', 'abroad', 'on', 'about', 'ok', 'anything', 'getting', 'of', 'v', 'o', 'side', 'whence', 'plus', 'act', 'consequently', 'or', 'seeing', 'own', 'whats', 'formerly', 'twelve', 'previously', 'somethan', 'into', 'within', 'shed', 'due', 'down', 'appropriate', 'right', 'primarily', 'theyd', "c's", 'whos', 'your', 'significantly', 'fill', "how's", 'her', 'eleven', 'aren', 'apparently', 'there', 'amidst', 'pages', 'hed', 'inasmuch', 'inner', 'way', 'forward', 'was', 'himself', 'elsewhere', "i've", 'becoming', 'amongst', 'somehow', 'hi', 'et-al', 'line', 'trying', 'with', 'he', 'usefulness', "they're", 'made', 'wish', 'inside', 'j', 'us', 'until', 'placed', 'below', 'un', 'whim', 'empty', 'z', 'similar', "we'd", 'strongly', 'gone', 'sometimes', 'associated', 'likewise', 'describe', 'am', 'itse\\xe2\\x80\\x9d', 'an', 'as', 'sometime', 'at', 'our', 'inc', 'again', 'uucp', "'ll", 'no', 'na', 'whereas', 'nd', 'detail', 'lately', 'til', 'other', 'you', 'really', "what's", 'showns', 'briefly', 'beginnings', 'welcome', 'shown', "let's", 'ours ', 'important', 'serious', 'upwards', 'ago', 'e', "she'd", 'having', 'u', "we're", 'everywhere', 'backward', 'hello', 'once']\
    train_posnegpath=train_path+"/positive_polarity/deceptive_from_MTurk/"\
    train_pospospath=train_path+"/positive_polarity/truthful_from_TripAdvisor/"\
    train_negnegpath=train_path+"/negative_polarity/deceptive_from_MTurk/"\
    train_negpospath=train_path+"/negative_polarity/truthful_from_Web/"\
    #test_posnegpath="/Users/manasranjanmahanta/Desktop/testnlp/posneg/"\
    #test_pospospath="/Users/manasranjanmahanta/Desktop/testnlp/pospos/"\
    #test_negnegpath="/Users/manasranjanmahanta/Desktop/testnlp/negneg/"\
    #test_negpospath="/Users/manasranjanmahanta/Desktop/testnlp/negpos/"\
\
\
\
\
    posposwords = []\
    posnegwords = []\
    negnegwords = []\
    negposwords = []\
    #noOfWordsPosNeg,noOfWordsPosPos,noOfWordsNegNeg,noOfWordsNegPos=0\
    ##PosNegative\
    for subdir, dirs, files in os.walk(train_posnegpath):\
        for file in files :\
            if file.endswith(".txt") and file != "README.txt":\
                text=open(os.path.join(subdir, file),"r")\
                posnegwords.extend(text.read().split())\
\
\
    posnegwordsTrimList=[''.join(char for char in word if char.isalnum())for word in posnegwords]\
    posnegwordsReal= [x.lower() for x in posnegwordsTrimList if x.lower() not in stopWords ]\
    #print posnegwordsReal\
    mapPosNeg=dict(Counter(posnegwordsReal))\
\
\
\
\
\
    ##PosPositive\
    for subdir, dirs, files in os.walk(train_pospospath):\
        for file in files :\
            if file.endswith(".txt") and file != "README.txt":\
                text=open(os.path.join(subdir, file),"r")\
                posposwords.extend(text.read().split())\
\
    posposwordsTrimList=[''.join(char for char in word if char.isalnum())for word in posposwords]\
    posposwordsReal= [x.lower() for x in posposwordsTrimList if x.lower() not in stopWords]\
    mapPosPos=dict(Counter(posposwordsReal))\
\
\
\
    ##NegNegative\
    for subdir, dirs, files in os.walk(train_negnegpath):\
        for file in files :\
            if file.endswith(".txt") and file != "README.txt":\
                text=open(os.path.join(subdir, file),"r")\
                negnegwords.extend(text.read().split())\
\
    negnegwordsTrimList=[''.join(char for char in word if char.isalnum())for word in negnegwords]\
    negnegwordsReal=[x.lower() for x in negnegwordsTrimList if x.lower() not in stopWords]\
    mapNegNeg=dict(Counter(negnegwordsReal))\
\
\
\
    ##NegPositive\
    for subdir, dirs, files in os.walk(train_negpospath):\
        for file in files :\
            if file.endswith(".txt") and file != "README.txt":\
                text=open(os.path.join(subdir, file),"r")\
                negposwords.extend(text.read().split())\
\
    negposwordsTrimList=[''.join(char for char in word if char.isalnum())for word in negposwords]\
    negposwordsReal=[x.lower() for x in negposwordsTrimList if x.lower() not in stopWords]\
    mapNegPos=dict(Counter(negposwordsReal))\
\
\
    dicts=[mapPosNeg,mapPosPos,mapNegNeg,mapNegPos]\
    modelpath="nbmodel.txt"\
    target=open(modelpath,"w")\
    target.write(str(mapPosNeg))\
    target.write("\\n"+str(mapPosPos))\
    target.write("\\n"+str(mapNegNeg))\
    target.write("\\n"+str(mapNegPos))\
\
\
    #superdict=defaultdict(list)\
    #for d in dicts:\
    #    for k,v in d.iteritems():\
    #        superdict[k].append(v)\
    #print superdict\
    CounterWords=Counter(posnegwordsReal)+Counter(posposwordsReal)+Counter(negnegwordsReal)+Counter(negposwordsReal)\
\
\
   # print "TotalCount%s" % (dict(CounterWords),)\
    uniqueWords=dict(CounterWords).keys()\
    superdict=defaultdict(list)\
    noOfUniqueWords=len(uniqueWords)\
    target.write("\\nUniqueWords,"+str(noOfUniqueWords))\
    #print noOfUniqueWords\
    for word in uniqueWords:\
        for d in dicts:\
            if word in d:\
                superdict[word].append(d.get(word))\
            else:\
                superdict[word].append(0)\
\
\
\
if __name__ == '__main__':\
    main()\
\
}