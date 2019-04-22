import requests
import json

def loadJson(name):
    CACHE_FNAME = str(name) + '.json'
    try:
        cache_file = open(CACHE_FNAME, 'r')
        cache_contents = cache_file.read()
        CACHE_DICTION = json.loads(cache_contents)
        cache_file.close()
    except:
        CACHE_DICTION = {}
    return CACHE_DICTION

def cacheRequest(BASEURL,params,header, cacheName, specifier):
    baseurl = BASEURL

    complete_url = baseurl + str(specifier)
    #header = {'User-Agent': 'hope'}
    header = header

    CACHE_DICTION = loadJson(str(cacheName))

    unique_ident = complete_url

    if unique_ident in CACHE_DICTION:
        page_text = CACHE_DICTION[unique_ident]
    else:
        page_text = requests.get(complete_url,params=params,headers=header).text #original
        #page_text = requests.get(complete_url,headers=header) #bad
        CACHE_DICTION[unique_ident] = page_text
        dumped_json_cache = json.dumps(CACHE_DICTION,indent=4)
        fw = open(str(cacheName)+'.json',"w")
        fw.write(dumped_json_cache)
        fw.close() # Close the open file


    #page_soup = BeautifulSoup(page_text, 'html.parser')
    #return page_soup
    return page_text