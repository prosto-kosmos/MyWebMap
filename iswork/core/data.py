import json
import random

def getStartObjests():
    objs = {
        'entity_list': [
            {
                'entity_id':'auto1',
                'number':'a777aa99',
                'model':'Mercedes Benz',
                'params':[
                    {
                        'params_id':'speed',
                        'params_alias':'Скорость',
                        'params_value':'30км/ч',
                    },
                    {
                        'params_id':'rpm',
                        'params_alias':'Обороты',
                        'params_value':'3091',
                    },
                    {
                        'params_id':'temp',
                        'params_alias':'Температура',
                        'params_value':'30℃',
                    },
                ],
                'stream_links':[
                    {
                        'stream_id':'camera1',
                        'stream_alias':'Вид спереди',
                        'stream_value':'https://obninsksite.ru/assets/theme/images/blog/slider/1.jpg',
                    },
                    {
                        'stream_id':'camera2',
                        'stream_alias':'Вид сбоку',
                        'stream_value':'https://obninsksite.ru/assets/theme/images/blog/slider/2.jpg',
                    },
                    {
                        'stream_id':'camera3',
                        'stream_alias':'Вид сзади',
                        'stream_value':'https://obninsksite.ru/assets/theme/images/blog/slider/3.jpg',
                    },
                ],
                'position_n':'6977760.708997443',
                'position_e':'4016570.740906363',
            },
            {
                'entity_id':'auto2',
                'number':'e758op36',
                'model':'Volkswagen Jetta',
                'params':[
                    {
                        'params_id':'speed',
                        'params_alias':'Скорость',
                        'params_value':'55км/ч',
                    },
                    {
                        'params_id':'rpm',
                        'params_alias':'Обороты',
                        'params_value':'6892',
                    },
                    {
                        'params_id':'temp',
                        'params_alias':'Температура',
                        'params_value':'94℃',
                    },
                ],
                'stream_links':[
                    {
                        'stream_id':'camera1',
                        'stream_alias':'Вид спереди',
                        'stream_value':'https://obninsksite.ru/assets/theme/images/blog/slider/1.jpg',
                    },
                    {
                        'stream_id':'camera2',
                        'stream_alias':'Вид сбоку',
                        'stream_value':'https://obninsksite.ru/assets/theme/images/blog/slider/2.jpg',
                    },
                ],
                'position_n':'6990748.408997443',
                'position_e':'4016499.440906363',
            },
            {
                'entity_id':'auto3',
                'number':'k918cc57',
                'model':'Nissan Juke',
                'params':[
                    {
                        'params_id':'speed',
                        'params_alias':'Скорость',
                        'params_value':'45км/ч',
                    },
                    {
                        'params_id':'rpm',
                        'params_alias':'Обороты',
                        'params_value':'1234',
                    },
                    {
                        'params_id':'temp',
                        'params_alias':'Температура',
                        'params_value':'14℃',
                    },
                ],
                'stream_links':[
                    {
                        'stream_id':'camera1',
                        'stream_alias':'Вид спереди',
                        'stream_value':'https://obninsksite.ru/assets/theme/images/blog/slider/1.jpg',
                    },
                    {
                        'stream_id':'camera2',
                        'stream_alias':'Вид сбоку',
                        'stream_value':'https://obninsksite.ru/assets/theme/images/blog/slider/2.jpg',
                    },
                    {
                        'stream_id':'camera3',
                        'stream_alias':'Вид сбоку',
                        'stream_value':'https://obninsksite.ru/assets/theme/images/blog/slider/3.jpg',
                    },
                    {
                        'stream_id':'camera4',
                        'stream_alias':'Вид сверху',
                        'stream_value':'https://obninsksite.ru/assets/theme/images/blog/slider/4.jpg',
                    },
                ],
                'position_n':'6990148.408997443',
                'position_e':'4010299.440906363',
            },
            {
                'entity_id':'auto4',
                'number':'k899ae57',
                'model':'Opel Astra',
                'params':[
                    {
                        'params_id':'speed',
                        'params_alias':'Скорость',
                        'params_value':'45км/ч',
                    },
                    {
                        'params_id':'rpm',
                        'params_alias':'Обороты',
                        'params_value':'1234',
                    },
                    {
                        'params_id':'temp',
                        'params_alias':'Температура',
                        'params_value':'14℃',
                    },
                ],
                'stream_links':[
                    {
                        'stream_id':'camera1',
                        'stream_alias':'Вид спереди',
                        'stream_value':'https://obninsksite.ru/assets/theme/images/blog/slider/1.jpg',
                    },
                    {
                        'stream_id':'camera2',
                        'stream_alias':'Вид сбоку',
                        'stream_value':'https://obninsksite.ru/assets/theme/images/blog/slider/2.jpg',
                    },
                    {
                        'stream_id':'camera3',
                        'stream_alias':'Вид сбоку',
                        'stream_value':'https://obninsksite.ru/assets/theme/images/blog/slider/3.jpg',
                    },
                    {
                        'stream_id':'camera4',
                        'stream_alias':'Вид сверху',
                        'stream_value':'https://obninsksite.ru/assets/theme/images/blog/slider/4.jpg',
                    },
                ],
                'position_n':'6957810.398997443',
                'position_e':'4046659.540906363',
            },
            {
                'entity_id':'auto5',
                'number':'e817aa99',
                'model':'Chevrolet Cruze',
                'params':[
                    {
                        'params_id':'speed',
                        'params_alias':'Скорость',
                        'params_value':'45км/ч',
                    },
                    {
                        'params_id':'rpm',
                        'params_alias':'Обороты',
                        'params_value':'1234',
                    },
                    {
                        'params_id':'temp',
                        'params_alias':'Температура',
                        'params_value':'14℃',
                    },
                ],
                'stream_links':[
                    {
                        'stream_id':'camera1',
                        'stream_alias':'Вид спереди',
                        'stream_value':'https://obninsksite.ru/assets/theme/images/blog/slider/1.jpg',
                    },
                    {
                        'stream_id':'camera2',
                        'stream_alias':'Вид сбоку',
                        'stream_value':'https://obninsksite.ru/assets/theme/images/blog/slider/2.jpg',
                    },
                    {
                        'stream_id':'camera3',
                        'stream_alias':'Вид сбоку',
                        'stream_value':'https://obninsksite.ru/assets/theme/images/blog/slider/3.jpg',
                    },
                    {
                        'stream_id':'camera4',
                        'stream_alias':'Вид сверху',
                        'stream_value':'https://obninsksite.ru/assets/theme/images/blog/slider/4.jpg',
                    },
                ],
                'position_n':'6907781.308997443',
                'position_e':'4056477.640906363',
            },
        ]
    }
    return objs

def getNewDataObjests():
    global position_n, position_e
    newData = json.dumps({
        'entity_list': [
            {
                'entity_id':'auto1',
                'position_n':'6977760.708997443',
                'position_e':'4016570.740906363',
                'params':[
                    {
                        'params_id':'speed',
                        'params_alias':'Скорость',
                        'params_value':f'{random.randint(3, 109)}км/ч',
                    },
                    {
                        'params_id':'rpm',
                        'params_alias':'Обороты',
                        'params_value':f'{random.randint(500, 5000)}',
                    },
                    {
                        'params_id':'tereuiruermp',
                        'params_alias':'Температура',
                        'params_value':f'{random.randint(3, 90)}℃',
                    },
                ],
            },
            {
                'entity_id':'auto2',
                'position_n':'6990748.408997443',
                'position_e':'4016499.440906363',
                'params':[
                    {
                        'params_id':'speed',
                        'params_alias':'Скорость',
                        'params_value':f'{random.randint(3, 109)}км/ч',
                    },
                    {
                        'params_id':'rpm',
                        'params_alias':'Обороты',
                        'params_value':f'{random.randint(500, 5000)}',
                    },
                    {
                        'params_id':'tereuiruermp',
                        'params_alias':'Температура',
                        'params_value':f'{random.randint(3, 90)}℃',
                    },
                ],
            },
            {
                'entity_id':'auto3',
                'position_n':'6990148.408997443',
                'position_e':'4010299.440906363',
                'params':[
                    {
                        'params_id':'speed',
                        'params_alias':'Скорость',
                        'params_value':f'{random.randint(3, 109)}км/ч',
                    },
                    {
                        'params_id':'rpm',
                        'params_alias':'Обороты',
                        'params_value':f'{random.randint(500, 5000)}',
                    },
                ],
            },
            {
                'entity_id':'auto4',
                'position_n':'6957810.398997443',
                'position_e':'4046659.540906363',
                'params':[
                    {
                        'params_id':'speed',
                        'params_alias':'Скорость',
                        'params_value':f'{random.randint(3, 109)}км/ч',
                    },
                    {
                        'params_id':'rpm',
                        'params_alias':'Обороты',
                        'params_value':f'{random.randint(500, 5000)}',
                    },
                ],
            },
            {
                'entity_id':'auto5',
                'position_n':'6907781.308997443',
                'position_e':'4056477.640906363',
                'params':[
                    {
                        'params_id':'speed',
                        'params_alias':'Скорость',
                        'params_value':f'{random.randint(3, 109)}км/ч',
                    },
                    {
                        'params_id':'rpm',
                        'params_alias':'Обороты',
                        'params_value':f'{random.randint(500, 5000)}',
                    },
                ],
            },
        ]
    })
    return newData