# coding=utf-8
import json
from django.http import HttpResponse
from django.views.generic import View
import time


class Suggetion(View):

    def get(self, request):

        def getUrls(url_get):
            next_url = {
                            'next':None,
                            'last':None,
                            'first':None,
                            'prev':None
                        }

            response = requests.get(url_get)
            conteudo = response.content
            header = response.headers
            header_link = header.get('link', None)
            if header_link:
                m = re.search('<(?P<next>https?://[^\s]+)>.+(next).+<(?P<last>https?://[^\s]+)>.+(last)', str(header_link))
                if not m:
                    m = re.search('<(?P<first>https?://[^\s]+)>.+(first).+<(?P<prev>https?://[^\s]+)>.+(prev)',str(header_link))
                if m:
                    for k,v in m.groupdict().iteritems():
                        next_url[k] = v

            if next_url['next']:
                url_get = next_url['next']
                # print "Next: %s" % (url_get)
            else:
                url_get = None
                if next_url['prev']:
                    # print "Prev: %s" % (next_url['prev'])
                    pass
            return conteudo, header, url_get


        import json
        import re
        import requests


        per_page = 100

        # username = 'joaoleite'
        # token_user = '7721ba5b9341b3fc623c341493dfca482eca1247'

        username = request.user.username
        token_user = access_token = request.user.social_auth.get(provider='github').tokens

        sugestoes = {}
        usuarios = {}

        user_to_following = {}
        dict_url = None

        url_get = 'https://api.github.com/users/%s/following?per_page=%s&access_token=%s' % (username, per_page, token_user)

        count = 1

        while(url_get):

            conteudo, header, next_url = getUrls(url_get)
            seguindo = json.loads(conteudo)
            url_get = next_url

            for seguido in seguindo:
                i_url_get = 'https://api.github.com/users/%s/following?per_page=%s&access_token=%s' % (seguido['login'], per_page, token_user)
                i_count = 1
                while(i_url_get):
                    i_conteudo, i_header, i_next_url = getUrls(i_url_get)
                    i_url_get = i_next_url

                    user_following_folloging = json.loads(i_conteudo)

                    #print "%s - Procurando pelos amigos de %s - %s" % (count, seguido['login'], i_count)

                    for user_following in user_following_folloging:
                        user_count = user_to_following.get(user_following['login'], 0)
                        if user_following not in seguindo and user_following['login'] != username:
                            #usuario que meu amigo segue que eu nao sigo
                            user_to_following[user_following['login']] = user_count + 1
                            usuarios[user_following['login']] = user_following
                        else:
                            #usuario que meu amigo segue que eu sigo
                            user_to_following[user_following['login']] = 0
                    i_count += 1
                count += 1


        #print user_to_following

        #debug
        #user_to_following = {u'umgeher': 1, u'romulojales': 1, u'jessevdk': 1, u'rodsenra': 1, u'technoweenie': 1, u'igoralves': 1, u'gabrielengel': 1, u'felipecruz': 1, u'JoaoFelipe': 1, u'omaciel': 1, u'gerardon': 4, u'tapajos': 1, u'vitorpamplona': 1, u'amandinhakee': 1, u'victornovais': 0, u'tarsis': 1, u'vandersonmota': 2, u'rafaeldx7': 1, u'rafaeldepaula': 1, u'marinho': 1, u'zacharyvoase': 1, u'ramiroluz': 1, u'marcussousa': 1, u'cvmello': 1, u'lucianosousa': 1, u'rennerocha': 1, u'scanferla': 4, u'rochacbruno': 1, u'mion': 2, u'renatooliveira': 1, u'flaviamissi': 1, u'hugomaiavieira': 1, u'lucianoratamero': 1, u'dacruz': 1, u'heynemann': 2, u'etandel': 3, u'pedromenezes': 1, u'mayzaoliveira': 1, u'maurobaraldi': 1, u'pydanny': 1, u'douglascamata': 1, u'alex': 1, u'jeanpimentel': 1, u'matschaffer': 1, u'edubraga': 1, u'nicolasteodosio': 2, u'dojopiaui': 1, u'pablobcb': 1, u'caioreigota': 2, u'flaviocdc': 1, u'kneipp': 1, u'fabricioer': 1, u'valdineidossantos': 1, u'achvaicer': 1, u'flavioamieiro': 2, u'DenisLP': 1, u'dojoufjf': 1, u'raphaeldealmeida': 1, u'marcosteixeira': 1, u'joaoleite': 0, u'stephenmcd': 1, u'trsouz': 1, u'thatch45': 1, u'tatiana': 1, u'mitsuhiko': 1, u'annacruz': 1, u'douglas': 1, u'ricobl': 1, u'murix': 1, u'pepedias': 2, u'aleborba': 1, u'chriiscardozo': 2, u'matheussl': 1, u'charettes': 1, u'gauperes': 1, u'kennethreitz': 2, u'davidsonfellipe': 1, u'jesuejunior': 4, u'infsaulo': 3, u'hallison': 1, u'FlavioAugusto': 2, u'fsouza': 1, u'jdahlin': 1, u'satanas': 1, u'adelgado': 1, u'fernandogrd': 1, u'Unitech': 1, u'flavioschuindt': 4, u'ricbit': 1, u'allandieguez': 3, u'denilsonsa': 1, u'myusuf3': 2, u'paivaNatasha': 1, u'ceci': 1, u'zaiste': 1, u'thiagoh': 1, u'robertomoulin': 1, u'santagada': 1, u'joerabelo': 1, u'eduardostalinho': 2, u'rafaelmws': 1, u'gustavohenrique': 1, u'felipealmeida': 1, u'heloisa': 1, u'leonardodavila': 1, u'setanta': 1, u'gchapim': 2, u'arthurfurlan': 1, u'cathoderay': 3, u'daltonmatos': 1, u'TiuTalk': 1, u'berrondo': 1, u'gilsondev': 1, u'zatosource': 1, u'rdtorres': 1, u'ijverig': 1, u'ehabkost': 1, u'ebertti': 0, u'gmorada': 1, u'berinhard': 4, u'gpaOliveira': 1, u'marcelcaraciolo': 2, u'rafaelcaricio': 1, u'renatolmorais': 1, u'marcelnicolay': 1, u'pyzen': 1, u'ramalho': 1, u'gladson': 1, u'TeeBSD': 1, u'apyb': 2, u'progrium': 1, u'rtopitt': 1, u'jpedrojpedro': 3, u'zedshaw': 1, u'pedroteixeira': 1, u'vitormazzi': 1, u'elyezer': 1, u'marcoacarvalho': 1, u'cabello': 1, u'brunousml': 4, u'walbon': 1, u'vim-scripts': 1, u'halan': 1, u'salvini': 1, u'jezdez': 1, u'cesarFrias': 3, u'semente': 1, u'thulio': 0, u'samuelclay': 1, u'henriquebastos': 4, u'jacobian': 1, u'funkotron': 1, u'lcmattoso': 1, u'fjcaetano': 1, u'hacktoon': 1, u'rafaelp': 1, u'jhudson8': 1, u'diegodukao': 1, u'turicas': 2, u'geron': 3, u'vitorcavalcanti': 1, u'luanfonceca': 1, u'andrewsmedina': 1, u'marco-jardim': 1, u'lquixada': 2, u'pedroargento': 1, u'iurims': 1, u'mayckxavier': 1, u'rcsilva83': 1, u'EvandroLG': 1, u'osantana': 1, u'niwibe': 1, u'luizBonsaver': 1, u'aureliojargas': 1, u'cloudson': 1}

        #Agrupa ordenacao
        indicacao = {}
        for k,v in user_to_following.iteritems():
            tmp = []
            tmp = indicacao.get(v,[])
            tmp.append(k)
            indicacao[v] = tmp

        #Exibe os mais ordenados
        # for k,v in indicacao.iteritems():
        #     print k
        #     for user in v:
        #         print user

        qtd_follow = 0
        lista_users = []
        qtd_vezes = indicacao.keys()
        while(qtd_follow < 16):
            if qtd_vezes:
                max_indicacao = max(qtd_vezes)
                for usuario in indicacao[max_indicacao]:
                    lista_users.append(usuarios[usuario])
                    qtd_follow += 1
                qtd_vezes.remove(max_indicacao)
            else:
                break


        users = []
        for usuario in lista_users:
            tmp = {
                'avatar_url':usuario.get('avatar_url', None),
                'login':usuario.get('login', None),
                'bio':usuario.get('bio', None)
            }
            users.append(tmp)


        users2 = [{
                "avatar_url": 'https://2.gravatar.com/avatar/8f8d53501d40286f6a2f228326926909',
                "login": 'cesarFrias',
                "bio": 'minimin'
            },{
                "avatar_url": 'https://2.gravatar.com/avatar/8f8d53501d40286f6a2f228326926909',
                "login": 'cesarFrias',
                "bio": 'minimin'
            },{
                "avatar_url": 'https://2.gravatar.com/avatar/8f8d53501d40286f6a2f228326926909',
                "login": 'cesarFrias',
                "bio": 'minimin'
            },{
                "avatar_url": 'https://2.gravatar.com/avatar/8f8d53501d40286f6a2f228326926909',
                "login": 'cesarFrias',
                "bio": 'minimin'
            }]

        return HttpResponse(json.dumps(users), mimetype='application/json')

