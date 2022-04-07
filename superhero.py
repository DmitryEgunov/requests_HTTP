import requests

TOKEN = ''

def hero_request():
    heros = ['Hulk', 'Captain America', 'Thanos']
    dict_heros = {}
    i = 0
    while i < len(heros):
        url = f'https://superheroapi.com/api/{TOKEN}/search/{heros[i]}/get'
        response = requests.get(url)
        dict_heros[heros[i]] = response.json()
        i += 1
    return dict_heros

def search_id(heros_dict):
    heros_id = []
    for hero in heros_dict:
        for key, val in heros_dict[hero].items():
            if type(val) == list:
                for item in val:
                    for k, v in item.items():
                        if item['name'] == hero:
                            if k == 'id':
                                heros_id.append([hero, k, v])
    return heros_id

def info_character(ids):
    i = 0
    dict_hero_info = {}
    while i < len(ids):
        IDs = ids[i][2]
        hero = ids[i][0]
        url = f"https://superheroapi.com/api/{TOKEN}/{IDs}"
        response = requests.get(url)
        dict_hero_info[hero] = response.json()
        i += 1
    return dict_hero_info

def hero_intelligence(information):
    heros = []
    for hero in information:
        for key, val in information[hero].items():
            if key == 'powerstats':
                for item in val:
                    if item == 'intelligence':
                        heros.append([hero, item, val[item]])
    print(f'Самый интеллектуальный супергерой - {heros[-1][0]} ({heros[-1][1]}-{heros[-1][2]})')


if __name__ == '__main__':
    hero_request()
    search_id(hero_request())
    info_character(search_id(hero_request()))
    hero_intelligence(info_character(search_id(hero_request())))