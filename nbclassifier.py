{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf460
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;\red16\green19\blue26;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl358\partightenfactor0

\f0\fs26 \cf2 \expnd0\expndtw0\kerning0
from __future__ import division\
import os,ast,sys\
from math import log10\
\
\
def main():\
    '''\
    stopWords=["a","about","again","all","am","an","and","any","are","aren't","as","at","be","been","before","being","below","both","but","by","doing","don't","down","during","each","few","for","from","having","he","he'd","he'll","he's","her","here","here's","hers","herself","him","himself","his","how","how's"]\
    stopWords.extend(["i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's","its","itself","let's","me","more","mustn't"])\
    stopWords.extend(["my","myself","no","nor","not","of","off","on","once","only","or","other","ought","our","ours","ourselves","out","over","own"])\
    stopWords.extend(["same","shan't","she","she'd","she'll","she's","so","some","such","than","that","that's","the","their"])\
    stopWords.extend(["theirs","them","then","there","these","they","they'd","they'll","they're","they've","this","those"])\
    stopWords.extend(["to","too","until","up","very","was","wasn't","we","we'd","we'll","we're","we've","were","weren't","what"])\
    stopWords.extend(["what's","when","when's","where","where's","which","while","who","who's","whom","why","why's","with"])\
    stopWords.extend(["you","","you'd","you'll","you're","you've","your","yours","yourself","i"])\
\
    '''\
    stopWords= ['secondly', 'all', 'consider', 'whoever', 'results', 'four', 'edu', 'go', 'mill', 'evermore', 'causes', 'seemed', 'rd', 'certainly', 'biol', 'system', "when's", 'vs', 'ts', 'to', 'asking', 'present', 'th', 'under', 'sorry', 'promptly', "a's", 'mug', 'sent', 'outside', 'far', 'mg', 'every', 'yourselves', "we'll", 'went', 'did', 'forth', "they've", 'fewer', 'hereafter', 'try', 'p', 'thereupon', 'round', 'added', "it'll", "i'll", 'someday', 'approximately', 'says', "you'd", 'ten', 'yourself', 'd', 'past', 'likely', 'invention', 'notwithstanding', 'further', 'shows', 'even', 'index', 'what', 'appear', 'giving', 'section', 'brief', 'run', 'goes', 'sup', 'new', 'poorly', 'ever', 'thin', 'full', "c'mon", 'whose', 'youd', 'respectively', 'sincere', 'never', 'here', 'himse\\xe2\\x80\\x9d', 'let', 'others', 'along', 'fifteen', 'suggest', 'obtained', 'ref', 'ahead', 'k', 'allows', 'proud', 'amount', "i'd", 'resulting', 'howbeit', 'usually', 'whereupon', "i'm", 'makes', 'thereto', 'thats', 'hither', 'via', 'followed', 'merely', 'while', 'till', 'ninety', 'vols', 'viz', 'ord', 'readily', 'everybody', 'use', 'from', 'would', 'contains', 'two', 'next', 'few', 'call', 'therefore', 'taken', 'themselves', 'thru', 'tell', 'more', 'knows', 'becomes', 'hereby', 'herein', 'particular', 'known', "who'll", 'must', 'me', 'none', 'thanks', 'f', 'this', 'ml', 'oh', 'anywhere', 'nine', 'can', 'mr', 'following', 'my', 'example', 'indicated', 'give', 'neverf', 'states', 'indicates', 'something', 'want', 'arise', 'information', 'needs', 'end', 'thing', 'rather', 'meanwhile', 'id', 'how', 'low', "'ve", 'instead', 'de', 'okay', 'tried', 'may', 'stop', 'after', 'eighty', 'different', 'hereupon', 'whilst', 'ff', 'date', 'such', 'undoing', 'a', 'thered', 'third', 'whenever', 'maybe', 'appreciate', 'q', 'ones', 'so', 'specifying', 'allow', 'keeps', "that's", 'thirty', 'six', 'help', 'indeed', 'over', 'move', 'mainly', 'soon', 'course', 'through', 'looks', 'fify', 'still', 'its', 'refs', 'before', 'thank', "he's", 'selves', 'inward', 'fix', 'actually', 'better', 'whether', 'willing', 'whole', 'thanx', 'ours', 'might', "haven't", 'versus', 'then', 'non', 'someone', 'somebody', 'thereby', 'auth', 'underneath', "you've", 'they', 'half', 'now', 'nos', 'several', 'name', 'always', 'reasonably', 'whither', "she's", 'sufficiently', 'each', 'found', 'entirely', 'mean', 'everyone', 'directly', 'doing', 'ed', 'eg', 'related', 'tip', 'owing', 'ex', 'substantially', 'et', 'beyond', 'couldnt', 'out', 'by', 'them', "needn't", 'furthermore', 'since', 'forty', 'research', 'looking', 're', 'seriously', "shouldn't", "they'll", 'got', 'cause', "one's", "you're", 'million', 'given', 'quite', "what'll", 'que', 'besides', 'x', 'ask', 'anyhow', 'beginning', 'backwards', 'g', 'could', 'hes', 'put', 'tries', 'keep', 'caption', 'w', 'ltd', 'hence', 'onto', 'think', 'first', 'myse\\xe2\\x80\\x9d', 'already', 'seeming', 'omitted', 'thereafter', 'thereof', 'awfully', 'done', 'adopted', 'another', 'thick', 'miss', "doesn't", 'little', 'necessarily', 'their', 'together', 'top', 'accordingly', 'least', 'anyone', 'indicate', 'too', 'hundred', 'gives', 'mostly', 'that', 'nobody', 'took', 'immediate', 'resulted', 'regards', 'somewhat', 'off', 'believe', 'herself', 'than', "here's", 'begins', 'b', 'unfortunately', 'showed', 'accordance', 'gotten', 'second', 'i', 'r', 'amid', 'toward', 'minus', 'are', 'and', 'youre', 'ran', 'thoughh', 'alongside', 'beforehand', 'mine', 'say', 'unlikely', 'have', 'need', 'seen', 'seem', 'saw', 'any', 'relatively', 'zero', 'thoroughly', 'latter', 'downwards', 'aside', 'thorough', 'predominantly', 'also', 'take', 'which', 'begin', 'exactly', 'unless', 'opposite', 'who', "where's", 'most', 'eight', 'but', 'significant', 'why', 'sub', 'forever', 'kg', 'especially', 'noone', 'later', 'm', 'amoungst', 'mrs', 'heres', "you'll", 'definitely', 'neverless', 'effect', 'normally', 'came', 'saying', 'particularly', 'show', 'anyway', 'page', 'ending', "that'll", 'find', 'fifth', 'one', 'specifically', 'keys', "daren't", 'behind', 'should', 'only', 'going', 'specify', 'announce', 'itd', "there've", 'do', 'his', 'above', 'get', 'between', 'overall', 'truly', "they'd", 'hid', 'nearly', 'words', 'despite', 'during', 'him', 'regarding', 'qv', 'h', 'cry', 'state', 'twice', 'she', 'though', 'contain', "what've", 'where', 'greetings', 'ignored', 'km', 'theirs', 'up', 'namely', 'computer', 'sec', 'anyways', "that've", 'throug', 'no-one', 'best', 'wonder', 'said', "there'd", 'away', 'currently', 'please', 'ups', 'enough', "there's", 'various', 'hopefully', 'affecting', 'probably', 'neither', 'across', 'co.', 'available', 'we', 'recently', 'useful', 'importance', 'were', 'however', 'meantime', 'come', 'both', 'c', 'last', 'thou', 'many', 'taking', 'thence', 'according', 'against', 'etc', 's', 'became', 'com', 'otherwise', 'among', 'liked', 'co', 'afterwards', 'seems', 'ca', 'whatever', 'alone', 'moreover', 'throughout', 'considering', "he'd", 'pp', 'described', "it's", 'three', 'been', 'quickly', 'whom', "there're", 'much', 'wherein', 'interest', 'certain', 'whod', 'hardly', "it'd", 'wants', 'corresponding', 'fire', 'latterly', 'concerning', 'else', 'hers', 'former', 'those', 'myself', 'novel', 'look', 'unlike', 'these', 'means', 'bill', 'twenty', 'value', 'n', 'will', 'near', 'theres', 'seven', 'whereafter', 'almost', 'wherever', 'is', 'thus', 'it', 'itself', 'im', 'in', 'affected', 'ie', 'y', 'if', 'containing', 'anymore', 'perhaps', 'insofar', 'make', 'same', 'clearly', 'beside', 'when', 'potentially', 'widely', 'gets', 'fairly', 'used', 'slightly', 'see', 'somewhere', 'I', 'upon', 'herse\\xe2\\x80\\x9d', 'uses', 'yours', "he'll", 'wheres', 'recent', 'lower', 'kept', 'whereby', 'largely', 'nevertheless', 'changes', 'nonetheless', 'well', 'anybody', 'obviously', 'without', 'comes', 'very', 'the', 'con', 'self', 'inc.', 'lest', 'things', 'world', "she'll", 'just', 'less', 'being', 'able', 'therere', 'presumably', 'front', 'farther', 'immediately', 'regardless', 'yes', 'yet', 'unto', 'wed', "we've", 'had', 'except', 'thousand', 'lets', 'has', 'adj', 'ought', 'gave', "t's", 'around', "who's", 'possible', 'usefully', 'possibly', 'whichever', 'five', 'know', 'similarly', 'using', 'part', "who'd", 'dare', 'apart', 'abst', 'nay', 'necessary', 'like', 'follows', 'noted', 'either', 'become', 'whomever', 'towards', 'therein', "why's", 'www', 'because', 'old', 'often', 'successfully', 'some', 'back', 'l', 'ah', 'sure', 'shes', 'specified', 'home', 'theyre', 'ourselves', 'happens', 'provided', 'vol', "there'll", 'for', 'bottom', 'affects', 'shall', 'per', 'everything', 'does', 'provides', 'tends', 't', 'be', 'sensible', 'obtain', 'nowhere', 'although', 'sixty', 'abroad', 'on', 'about', 'ok', 'anything', 'getting', 'of', 'v', 'o', 'side', 'whence', 'plus', 'act', 'consequently', 'or', 'seeing', 'own', 'whats', 'formerly', 'twelve', 'previously', 'somethan', 'into', 'within', 'shed', 'due', 'down', 'appropriate', 'right', 'primarily', 'theyd', "c's", 'whos', 'your', 'significantly', 'fill', "how's", 'her', 'eleven', 'aren', 'apparently', 'there', 'amidst', 'pages', 'hed', 'inasmuch', 'inner', 'way', 'forward', 'was', 'himself', 'elsewhere', "i've", 'becoming', 'amongst', 'somehow', 'hi', 'et-al', 'line', 'trying', 'with', 'he', 'usefulness', "they're", 'made', 'wish', 'inside', 'j', 'us', 'until', 'placed', 'below', 'un', 'whim', 'empty', 'z', 'similar', "we'd", 'strongly', 'gone', 'sometimes', 'associated', 'likewise', 'describe', 'am', 'itse\\xe2\\x80\\x9d', 'an', 'as', 'sometime', 'at', 'our', 'inc', 'again', 'uucp', "'ll", 'no', 'na', 'whereas', 'nd', 'detail', 'lately', 'til', 'other', 'you', 'really', "what's", 'showns', 'briefly', 'beginnings', 'welcome', 'shown', "let's", 'ours ', 'important', 'serious', 'upwards', 'ago', 'e', "she'd", 'having', 'u', "we're", 'everywhere', 'backward', 'hello', 'once']\
    map=\{\}\
    count=0\
    testPath="nbmodel.txt"\
    with open(testPath,"r") as f:\
        for line in f:\
            map[count]=line\
            count+=1\
\
#??print map[0],map[1],map[2],map[3],map[4]\
    mapPosNeg=ast.literal_eval(map[0])\
    mapPosPos=ast.literal_eval(map[1])\
    mapNegNeg=ast.literal_eval(map[2])\
    mapNegPos=ast.literal_eval(map[3])\
    noOfUniqueWords=int(map[4].split(",")[1])\
\
    #Probability PosNeg\
    noOfWordsPosNeg=sum(mapPosNeg.values())\
    map_Values=[log10((x+1)/(float)(noOfWordsPosNeg+noOfUniqueWords)) for x in mapPosNeg.values()]\
    P_mapPosNeg=dict(zip(mapPosNeg.keys(),map_Values))\
\
    #Probability PosPos\
    noOfWordsPosPos=sum(mapPosPos.values())\
    map_Values=[log10((x+1)/(float)(noOfWordsPosPos+noOfUniqueWords)) for x in mapPosPos.values()]\
    P_mapPosPos=dict(zip(mapPosPos.keys(),map_Values))\
\
    #Probability NegNeg\
    noOfWordsNegNeg=sum(mapNegNeg.values())\
    map_Values=[log10((x+1)/(float)(noOfWordsNegNeg+noOfUniqueWords)) for x in mapNegNeg.values()]\
    P_mapNegNeg=dict(zip(mapNegNeg.keys(),map_Values))\
\
    #Probability NegPos\
    noOfWordsNegPos=sum(mapNegPos.values())\
    map_Values=[log10((x+1)/(float)(noOfWordsNegPos+noOfUniqueWords)) for x in mapNegPos.values()]\
    P_mapNegPos=dict(zip(mapNegPos.keys(),map_Values))\
\
    #print "MapPosNeg",P_mapPosNeg,"\\nMapPosPos",P_mapPosPos,"\\nMapNegNeg",P_mapNegNeg,"\\nMapNegPos",P_mapNegPos\
\
    TotalNoOfWords=noOfWordsPosNeg+noOfWordsPosPos+noOfWordsNegNeg+noOfWordsNegPos\
    P_PosNeg=noOfWordsPosNeg/float(TotalNoOfWords)\
    P_PosPos=noOfWordsPosPos/float(TotalNoOfWords)\
    P_NegNeg=noOfWordsNegNeg/float(TotalNoOfWords)\
    P_NegPos=noOfWordsNegPos/float(TotalNoOfWords)\
\
    #print "probalities map:",P_PosNeg,P_PosPos,P_NegNeg,P_NegPos\
\
    testpath=sys.argv[1]\
    print sys.argv[1]\
    #testpaths=[test_posnegpath,test_pospospath,test_negnegpath,test_negpospath]\
    constant=log10(1/noOfUniqueWords)\
\
    #count=0\
    #for test_tempPath in testpaths:\
    #   posdec=0\
    #  postru=0\
    #  negdec=0\
    # negtru=0\
    target=open("nboutput.txt","w")\
\
    for subdir, dirs, files in os.walk(testpath):\
        for file in files :\
                #countFiles=0\
                L_PosNeg=[]\
                L_PosPos=[]\
                L_NegNeg=[]\
                L_NegPos=[]\
                if file.endswith(".txt") and file != "README.txt":\
                    #countFiles+=1\
                    textfile=open(os.path.join(subdir, file),"r")\
                    testwords=textfile.read().split()\
                   # print "test:",testwords\
                    testwordstrim=[''.join(char for char in word if char.isalnum())for word in testwords]\
                    testwordsReal=[x.lower() for x in testwordstrim if x.lower() not in stopWords]\
                   # print "testwordsReal:",testwordsReal\
                    for word in testwordsReal:\
                        ##PosNeg\
                        if word in P_mapPosNeg:\
                            L_PosNeg.append(P_mapPosNeg[word])\
                        else:\
                            L_PosNeg.append(constant)\
\
                        ##PosPos\
                        if word in P_mapPosPos:\
                            L_PosPos.append(P_mapPosPos[word])\
                        else:\
                            L_PosPos.append(constant)\
\
                        ##NegNeg\
                        if word in P_mapNegNeg:\
                            L_NegNeg.append(P_mapNegNeg[word])\
                        else:\
                            L_NegNeg.append(constant)\
\
\
                         ##NegPos\
                        if word in P_mapNegPos:\
                            L_NegPos.append(P_mapNegPos[word])\
                        else:\
                            L_NegPos.append(constant)\
\
                    P_textPosNeg=sum(L_PosNeg)+log10(P_PosNeg)\
                    P_textPosPos=sum(L_PosPos)+log10(P_PosPos)\
                    P_textNegNeg=sum(L_NegNeg)+log10(P_NegNeg)\
                    P_textNegPos=sum(L_NegPos)+log10(P_NegPos)\
\
                    #print "Ans:",P_textPosNeg,P_textPosPos,P_textNegNeg,P_textNegPos\
                    # nbc = NBClassifier(False, True, False, util)\
                    # nbc.classify()\
                    ListAnswer=[P_textPosNeg,P_textPosPos,P_textNegNeg,P_textNegPos]\
                    indexAnswer=ListAnswer.index(max(ListAnswer))\
                    options=\{"0":"deceptive positive","1":"truthful positive","2":"deceptive negative","3":"truthful negative"\}\
\
\
                    #print options.get(str(indexAnswer))+" "+str(os.path.join(subdir, file))\
                    if options.get(str(indexAnswer))=="deceptive positive":\
                        target.write("deceptive positive "+str(os.path.join(subdir, file))+"\\n")\
                    elif options.get(str(indexAnswer))=="truthful positive":\
                        target.write("truthful positive "+str(os.path.join(subdir, file))+"\\n")\
                    elif options.get(str(indexAnswer))=="deceptive negative":\
                        target.write("deceptive negative "+str(os.path.join(subdir, file))+"\\n")\
                    elif options.get(str(indexAnswer))== "truthful negative":\
                        target.write("truthful negative "+str(os.path.join(subdir, file))+"\\n")\
\
        '''\
        if(count==0):\
            accuracy=posdec/(posdec+postru+negdec+negtru)\
            print "PosDec Accuracy:",accuracy\
        if(count==1):\
            accuracy=postru/(posdec+postru+negdec+negtru)\
            print "PosTru Accuracy:",accuracy\
        if(count==2):\
            accuracy=negdec/(posdec+postru+negdec+negtru)\
            print "NegDec Accuracy:",accuracy\
        if(count==3):\
            accuracy=negtru/(posdec+postru+negdec+negtru)\
            print "NegTru Accuracy:",accuracy\
        count+=1\
            '''\
\
if __name__ == '__main__':\
    main()}