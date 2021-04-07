import json

def getStartObjests():
    objs = {
        'auto1': 
        {
            'enabled':'True',
            'number':'a777aa99',
            'model':'Mercedes Benz',
            'stream_link':'https://localhost:8000',
            'position_n':'6977760.708997443',
            'position_e':'4016570.740906363',
        },
        'auto2':
        {
            'enabled':'True',
            'number':'e758op36',
            'model':'Volkswagen Jetta',
            'stream_link':'https://localhost:8000',
            'position_n':'6990748.408997443',
            'position_e':'4016499.440906363',
        },
        'auto3':
        {
            'enabled':'False',
            'number':'k918cc57',
            'model':'Nissan Juke',
            'stream_link':'https://localhost:8000',
            'position_n':'6960655.308997443',
            'position_e':'4035489.640906363',
        },
        'auto4':
        {
            'enabled':'True',
            'number':'k899ae57',
            'model':'Opel Astra',
            'stream_link':'https://localhost:8000',
            'position_n':'6955499.308997443',
            'position_e':'4016601.840906363',
        },
        'auto5':
        {
            'enabled':'False',
            'number':'e817aa99',
            'model':'Chevrolet Cruze',
            'stream_link':'https://localhost:8000',
            'position_n':'6917515.708997443',
            'position_e':'4076666.640906363',
        },
        'auto6':
        {
            'enabled':'True',
            'number':'c832mm36',
            'model':'BMW X5',
            'stream_link':'https://localhost:8000',
            'position_n':'6907781.308997443',
            'position_e':'4056477.640906363',
        },
        'auto7':
        {
            'enabled':'True',
            'number':'e239ea57',
            'model':'Lada Granta',
            'stream_link':'https://localhost:8000',
            'position_n':'6928067.298997443',
            'position_e':'4006345.940906363',
        },
        'auto8':
        {
            'enabled':'True',
            'number':'a221ak36',
            'model':'Audi R8',
            'stream_link':'https://localhost:8000',
            'position_n':'6957810.398997443',
            'position_e':'4046659.540906363',
        },
        'auto9':
        {
            'enabled':'True',
            'number':'o545ko55',
            'model':'Mitsubishi Lancer',
            'stream_link':'https://localhost:8000',
            'position_n':'6958670.398997443',
            'position_e':'4048659.540906363',
        },
        'auto10':
        {
            'enabled':'True',
            'number':'k919ao57',
            'model':'Ford Focus',
            'stream_link':'https://localhost:8000',
            'position_n':'6957810.398997443',
            'position_e':'4040659.540906363',
        },
        'auto11':
        {
            'enabled':'True',
            'number':'c654pc57',
            'model':'Cadillac Escalade',
            'stream_link':'https://localhost:8000',
            'position_n':'6943810.398997443',
            'position_e':'4043659.540906363',
        },
        'auto12':
        {
            'enabled':'False',
            'number':'p112pc57',
            'model':'Jeep Compass',
            'stream_link':'https://localhost:8000',
            'position_n':'6945810.398997443',
            'position_e':'4053987.540906363',
        },
        'auto13':
        {
            'enabled':'False',
            'number':'o056cp777',
            'model':' Hummer EV',
            'stream_link':'https://localhost:8000',
            'position_n':'6950810.398997443',
            'position_e':'4036659.540906363',
        },
        'auto14':
        {
            'enabled':'True',
            'number':'o002pe777',
            'model':'LADA XRay',
            'stream_link':'https://localhost:8000',
            'position_n':'6933810.398997443',
            'position_e':'4076987.540906363',
        },
        'auto15':
        {
            'enabled':'True',
            'number':'e821ok67',
            'model':' LADA Niva',
            'stream_link':'https://localhost:8000',
            'position_n':'6945810.398997443',
            'position_e':'4026659.540906363',
        },
    }
    return objs

position_n = 6977760.708997443
position_e = 4016570.740906363

def getCoordinatesObjests():
    global position_n, position_e
    coor = json.dumps({
        'auto1': 
        {
            'position_n': str(position_n + 11.0),
            'position_e': str(position_e + 181.0),
        },
        'auto2': 
        {
            'position_n': str(position_n + 1188.0),
            'position_e': str(position_e - 15717.0),
        },
        'auto3': 
        {
            'position_n': str(position_n + 14571.0),
            'position_e': str(position_e + 1134.0),
        },
        'auto4': 
        {
            'position_n': str(position_n - 1451.0),
            'position_e': str(position_e + 15721.0),
        },
        'auto5': 
        {
            'position_n': str(position_n - 1134.0),
            'position_e': str(position_e + 1451.0),
        },
        'auto6': 
        {
            'position_n': str(position_n - 8811.0),
            'position_e': str(position_e - 1541.0),
        },
        'auto7': 
        {
            'position_n': str(position_n + 121.0),
            'position_e': str(position_e + 1111.0),
        },
        'auto8': 
        {
            'position_n': str(position_n - 1211.0),
            'position_e': str(position_e + 12471.0),
        },
        'auto9': 
        {
            'position_n': str(position_n + 2141.0),
            'position_e': str(position_e - 45311.0),
        },
        'auto10': 
        {
            'position_n': str(position_n - 1156.0),
            'position_e': str(position_e - 42111.0),
        },
        'auto11': 
        {
            'position_n': str(position_n - 171.0),
            'position_e': str(position_e + 15631.0),
        },
        'auto12': 
        {
            'position_n': str(position_n - 1471.0),
            'position_e': str(position_e - 14571.0),
        },
        'auto13': 
        {
            'position_n': str(position_n + 11091.0),
            'position_e': str(position_e + 11231.0),
        },
        'auto14': 
        {
            'position_n': str(position_n - 143471.0),
            'position_e': str(position_e - 14571.0),
        },
        'auto15': 
        {
            'position_n': str(position_n + 15091.0),
            'position_e': str(position_e + 61231.0),
        },
    })
    position_e += 50.0
    position_n += 50.0
    return coor