import urllib.request
arq = open("list.txt", 'r')
arq2 = open("resultado.txt", 'w')
hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
for linha in arq.readlines():
    try:
        url = 'http://'+linha.rstrip()+'/ads.txt'
        #print(url)
        req = urllib.request.Request(url,headers=hdr)
        pagina = urllib.request.urlopen(req)
        ads = str(pagina.read())
        #txt= ads.decode(pagina.headers.get_content_charset())
        if ads.find('158303') == -1:
            arq2.write('%s - Não\n'%url)
            print(url,', Não')
        else:
            arq2.write('%s - OK\n'%url)
            print(url,', Ok')
    except:
        arq2.write('%s - Sem_adx.txt\n'%url)
        print(url,", Sem adx.txt")
arq.close()