# -*- coding:utf-8 -*-

import json


def build_tram_stops(jsonobject):
    with open(jsonobject, 'r', encoding='utf-8') as f:
        temp = json.loads(f.read())
        stop_key = list(temp.keys())

        info_stop = dict()
        for i in stop_key:
            info_stop[i] = dict()
            info_stop[i]['lat'] = temp[i]['position'][0]
            info_stop[i]['lon'] = temp[i]['position'][1]
    return info_stop



def build_tram_lines(lines_path):
    with open(lines_path, "r", encoding='utf-8') as f:
        tram_number = []
        tram_stop = []
        tram_time = []
        for i in f:
            if len(i)==3 or len(i) ==4:
                tram_number.append(i[:-2])
                tmp = []
                tram_stop.append(tmp)

                time_tmp = []
                tram_time.append(time_tmp)

            if len(i)>6:
                tmp.append(i[:-6].replace(" ", ""))
        
                time_tmp.append( list(map(int, (i[-6:].replace("\n", "")).split(':')))      )

        
    tram_lines = dict(zip(tram_number, tram_stop))
    tram_time = dict(zip(tram_number, tram_time))

    all_stop = list( set( [j for i in tram_lines.keys() for j in tram_lines[i]] ) )
    all_stop = dict(zip(all_stop, [i for i in range(len(all_stop))]))


    stop_time = dict()
    for i in tram_lines.keys():
        for j in range(len(tram_lines[i])):
            if j <= (len(tram_lines[i])-2):
                tmp = dict()
                tmp[tram_lines[i][j+1]] = (tram_time[i][j+1][0] - tram_time[i][j][0])*60 + (tram_time[i][j+1][1] - tram_time[i][j][1])
                stop_time[tram_lines[i][j]] = tmp
            
            if j <= (len(tram_lines[i])-2):
                j = j+1
                tmp = dict()
                tmp[tram_lines[i][-j-1]] = (tram_time[i][-j][0] - tram_time[i][-j-1][0])*60 + (tram_time[i][-j][1] - tram_time[i][-j-1][1])
                stop_time[tram_lines[i][-j]] = tmp
    
    return tram_lines,stop_time

def build_tram_network(jsonobject, lines_path):
    info_stop = build_tram_stops(jsonobject)
    tram_lines,stop_time  = build_tram_lines(lines_path)
    tramnetwork = {'stops':info_stop, 'lines':tram_lines, 'times':stop_time}
    return tramnetwork



