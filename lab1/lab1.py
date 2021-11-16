# -*- coding:utf-8 -*-

import json

json_path = '../data/tramstops.json'
def build_tram_stops(jsonobject):
    with open(jsonobject, 'r', encoding='utf-8') as f:
        temp = json.loads(f.read())
        stop_key = list(temp.keys())

        info_stop = dict()
        for i in stop_key:
            info_stop[i] = dict()
            info_stop[i]['lat'] = float(temp[i]['position'][0])
            info_stop[i]['lon'] = float(temp[i]['position'][1])
    
    return info_stop


lines_path = '../data/tramstops.txt'
def build_tram_lines(txt_path):
    with open(lines_path, "r", encoding='utf-8') as f:
        tram_number = []
        tram_stop = []
        for i in f:
            if len(i)==3 or len(i) ==4:
                tram_number.append(i[:-2])
                tmp = []
                tram_stop.append(tmp)
            if len(i)>6:
                tmp.append(i[:-6].rstrip())
    return dict(zip(tram_number, tram_stop))

def build_tram_times(txt_path):
    tram_lines = build_tram_lines(txt_path)
