from .squads_data import SQUADS_DATA
from .assignment_1 import players_as_dictionaries
from pprint import pprint

def players_by_position(squads_list):
    position_dict = {}
    position_GK = []
    position_DF = []
    position_MF = []
    position_FW = []
    for player in players_as_dictionaries(SQUADS_DATA):
        position = player['position']
        if position == 'GK':
            position_GK.append(player)
        if position == 'DF':
            position_DF.append(player)
        if position == 'MF':
            position_MF.append(player)
        if position == 'FW':
            position_FW.append(player)
    if len(position_GK) > 0:
        position_dict.update({'GK': position_GK})
    if len(position_DF) > 0:
        position_dict.update({'DF': position_DF})
    if len(position_MF) > 0:
        position_dict.update({'MF': position_MF})
    if len(position_FW) > 0:
        position_dict.update({'FW': position_FW})
    return position_dict
players_by_position(SQUADS_DATA)


    
