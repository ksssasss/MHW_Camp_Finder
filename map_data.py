MAP_DATA = {
    'Ruins_of_Wyveria': {
        1: {1: 0, 2: 150, 3: 200, 4: 250},
        2: {1: 150, 2: 0, 3: 100, 4: 150},
        3: {1: 200, 2: 100, 3: 0, 4: 100},
        4: {1: 250, 2: 150, 3: 100, 4: 0}
    },
    'Iceshard_Cliffs': {
        1: {1: 0, 2: 180, 3: 220, 4: 280},
        2: {1: 180, 2: 0, 3: 120, 4: 160},
        3: {1: 220, 2: 120, 3: 0, 4: 140},
        4: {1: 280, 2: 160, 3: 140, 4: 0}
    },
    'Oilwell_Basin': {
        1: {1: 0, 2: 160, 3: 240, 4: 300},
        2: {1: 160, 2: 0, 3: 140, 4: 180},
        3: {1: 240, 2: 140, 3: 0, 4: 120},
        4: {1: 300, 2: 180, 3: 120, 4: 0}
    },
    'Scarlet_Forest': {
        1: {1: 0, 2: 140, 3: 200, 4: 260},
        2: {1: 140, 2: 0, 3: 100, 4: 140},
        3: {1: 200, 2: 100, 3: 0, 4: 120},
        4: {1: 260, 2: 140, 3: 120, 4: 0}
    },
    'Windward_Plains': {
        'camps': {
            'ベースキャンプ': {1: 15, 2: 35, 3: 30, 4: 35, 5: 40, 6: 40, 7: 10, 8: 20, 9: 30, 10: 30, 11: 45, 12: 30, 13: 50, 14: 60, 15: 60, 16: 60, 17: 90},
            '風音の村 クナファ': {1: 30, 2: 30, 3: 35, 4: 50, 5: 50, 6: 20, 7: 25, 8: 20, 9: 35, 10: 35, 11: 20, 12: 20, 13: 30, 14: 40, 15: 40, 16: 40, 17: 70},
            'エリア 3 南部': {1: 20, 2: 10, 3: 5, 4: 25, 5: 20, 6: 5, 7: 30, 8: 40, 9: 50, 10: 50, 11: 20, 12: 40, 13: 30, 14: 30, 15: 55, 16: 45, 17: 75},
            'エリア 4 鉱脈洞窟': {1: 15, 2: 30, 3: 15, 4: 10, 5: 20, 6: 25, 7: 25, 8: 35, 9: 45, 10: 45, 11: 40, 12: 50, 13: 50, 14: 50, 15: 75, 16: 65, 17: 95},
            'エリア 4 西部': {1: 20, 2: 35, 3: 20, 4: 5, 5: 10, 6: 30, 7: 35, 8: 45, 9: 55, 10: 60, 11: 40, 12: 45, 13: 55, 14: 55, 15: 80, 16: 70, 17: 100},
            'エリア 6 谷の隠れ家': {1: 25, 2: 20, 3: 10, 4: 30, 5: 30, 6: 5, 7: 35, 8: 45, 9: 55, 10: 60, 11: 15, 12: 40, 13: 30, 14: 30, 15: 55, 16: 45, 17: 75},
            'エリア 8 南西部': {1: 25, 2: 30, 3: 25, 4: 45, 5: 40, 6: 35, 7: 10, 8: 10, 9: 25, 10: 25, 11: 30, 12: 10, 13: 30, 14: 55, 15: 40, 16: 40, 17: 70},
            'エリア 8 南東部': {1: 40, 2: 45, 3: 45, 4: 60, 5: 55, 6: 50, 7: 20, 8: 10, 9: 25, 10: 15, 11: 45, 12: 25, 13: 45, 14: 70, 15: 55, 16: 70, 17: 80},
            'エリア 9 見晴らし丘': {1: 30, 2: 45, 3: 40, 4: 55, 5: 50, 6: 45, 7: 10, 8: 15, 9: 5, 10: 15, 11: 55, 12: 30, 13: 50, 14: 75, 15: 60, 16: 60, 17: 90},
            'エリア 10 南東部': {1: 40, 2: 50, 3: 45, 4: 65, 5: 60, 6: 55, 7: 25, 8: 15, 9: 15, 10: 5, 11: 55, 12: 30, 13: 55, 14: 80, 15: 60, 16: 60, 17: 90},
            'エリア 13 オアシス': {1: 40, 2: 25, 3: 35, 4: 55, 5: 50, 6: 30, 7: 50, 8: 45, 9: 60, 10: 60, 11: 15, 12: 25, 13: 5, 14: 20, 15: 35, 16: 20, 17: 45},
            'エリア 13 西部': {1: 40, 2: 20, 3: 30, 4: 50, 5: 45, 6: 30, 7: 50, 8: 50, 9: 65, 10: 65, 11: 10, 12: 30, 13: 10, 14: 25, 15: 40, 16: 30, 17: 55},
            'エリア 14 地下水脈': {1: 50, 2: 30, 3: 40, 4: 55, 5: 55, 6: 35, 7: 60, 8: 65, 9: 80, 10: 80, 11: 25, 12: 45, 13: 20, 14: 5, 15: 15, 16: 35, 17: 65},
            'エリア 16 骨砂漠': {1: 60, 2: 40, 3: 50, 4: 70, 5: 65, 6: 50, 7: 60, 8: 55, 9: 70, 10: 70, 11: 30, 12: 35, 13: 20, 14: 40, 15: 30, 16: 10, 17: 25},
            'エリア 16 北西部': {1: 55, 2: 30, 3: 45, 4: 65, 5: 60, 6: 45, 7: 55, 8: 50, 9: 65, 10: 65, 11: 25, 12: 30, 13: 15, 14: 35, 15: 25, 16: 5, 17: 20}
        },
        'camp_names': {
            1: 'ベースキャンプ',
            2: '風音の村 クナファ',
            3: 'エリア 3 南部',
            4: 'エリア 4 鉱脈洞窟',
            5: 'エリア 4 西部',
            6: 'エリア 6 谷の隠れ家',
            7: 'エリア 8 南西部',
            8: 'エリア 8 南東部',
            9: 'エリア 9 見晴らし丘',
            10: 'エリア 10 南東部',
            11: 'エリア 13 オアシス',
            12: 'エリア 13 西部',
            13: 'エリア 14 地下水脈',
            14: 'エリア 16 骨砂漠',
            15: 'エリア 16 北西部'
        }
    }
} 