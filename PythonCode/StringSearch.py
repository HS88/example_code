Index = {}# to store word, id, position 
StringID = {}
Words = []
id = 1

def uniqueOrderedIntersection(list1, list2):
        result = {}
        for a in list2.keys():
                if( a in list1.keys()):
                        for position in list1[a] :                                
                                if( position+1 in list2[a]):
                                        if( a not in result ):
                                                result[a] = []                                
                                        result[a].append(position+1)
        return result

def GetWords(inputString):
        wordlist = inputString.split(" ")
        result = []
        for word in wordlist:
                result.append(word.lower())
        return result

#preprocessing step to update the corpus
def PrepareIndex( Corpus ):
        id = 1
        for inputString in Corpus:
                Words = []
                Words = GetWords(inputString)# This functions returns list of words
                StringID[id] = inputString
                position = 1
                for word in Words:                        
                        if( word not in Index):
                                Index[ word ] = {}
                        if id not in Index[word]:
                                Index[word][id]=[]
                        Index[ word ][id].append(position)
                        position = position + 1
                id = id + 1

#runtime function
def GetResultString( queryWord, showState=False ):
        result = []
        Words = GetWords(queryWord)
        Ids = {}
        for word in Words:
                if word not in Index:
                        return []                
                if len(Ids) == 0:
                        Ids = Index[word] #string id and position dictionary
                else:
                        StringIds = Index[word]
                        Ids = uniqueOrderedIntersection(Ids, StringIds)
        if(showState):
                print(Ids)
        for id in Ids.keys():
                result.append(StringID[id])
        return result

corpus = ["I ate food","Foo bar baz","Baz bar foo","There was no mail today"]

PrepareIndex(corpus)
a = GetResultString('foo bar')
print(a)
