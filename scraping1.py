from urllib.request import urlopen
from bs4 import BeautifulSoup as bs


def ngram(input,n):
    
    input = input.split(' ')
    output = []
    for i in range(len(input)-n+1):
        output += input[i:i+n]
    return output


if __name__ == '__main__':
    html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
    bsObj = bs(html,'html.parser')
    content = bsObj.find(id='mw-content-text').get_text()
    ngrams = ngram(content,2)
    #print (ngrams)
    print ('2-grams count is: %s' % len(ngrams))
