#import as needed from wordnik usage APIs
from wordnik import *
apiUrl = 'http://api.wordnik.com/v4'
apiKey = '9fd570b79ede09df0600e002c6b0f9b14571c3ecfe4a35c13'

def definition(word):
    res = wordApi.getDefinitions(word, limit = 3)
    return res

def relatedwords(word):
    res = wordApi.getRelatedWords(word, limit = 10)
    return res