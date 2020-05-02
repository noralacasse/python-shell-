import urllib.request, webbrowser
def downlaod():
    print('Beginning file downlaod...')
    url = input('Url> ')
    dirc = input('Directory> ')
    urllib.request.urlretrieve(url, dirc)

def browse():
    site = input('website> ')
    def check():
        try: 
            urllib.request.urlopen('https://%s' %site)
            return True
        except:
            return False
    
    check()
    if check():
        webbrowser.open(site)
    else:
        print('We cannot find that website/server')
    

   