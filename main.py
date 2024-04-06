from pieChart import PieChart

config = {
    'diametro':50,
    'set_line_width':1,
    'ubicacion':{
        'x':35,
        'y':45
    },
    'graficoMarco':{
        'set_fill_color':{
            'r':255,
            'g':255,
            'b':255
        },
        'rect':{
            'x':30, 
            'y':30,
            'w':150,
            'h':100,
            'style':'FD'
        }        
    },
    'graficoTitulo':{
        'set_text_color':{
            'r': 0,
            'g': 0,
            'b': 0
        },
        'set_font':{
            'family':'Times',
            'style':'',
            'size':24
        },
        'text':{
            'x':35,
            'y':40,
            'text':'Asistentes al evento'
        }
    },
    'graficoPie':{
        'set_text_color':{
            'r':0,
            'g':0,
            'b':0
        },
        'set_font':{
            'family': 'Times',
            'style': 'B',
            'size': 12
        },
        'text':{
            'x':31, 
            'y':128, 
            'text':'fuente: DANE - Webservice SIPSA'
        }
    },
    'leyendaMarquito':{
        'set_fill_color':{
            'r':255,
            'g':255,
            'b':255
        },
        'rect':{
            'x':105, 
            'y':49.6, 
            'w':85, 
            'h':45, 
            'style':"FD"
        }
    },
    'data':[
        {
            'text':'mujeres',
            'graficoCircularSector': {
                'solid_arc':{
                    'a':50,
                    'b':50,
                    'start_angle':0,
                    'end_angle':80,
                    'style':"FD"
                }
            },
            'color':{
                'r':255,
                'g':0,
                'b':0
            }
        },
        {
            'text':'hombres',
            'graficoCircularSector': {
                'solid_arc':{
                    'a':50,
                    'b':50,
                    'start_angle':80,
                    'end_angle':180,
                    'style':"FD"
                }
            },
            'color':{
                'r':50,
                'g':255,
                'b':50
            }
        },
        {
            'text':'niños y niñas',
            'graficoCircularSector': {
                'solid_arc':{
                    'a':50,
                    'b':50,
                    'start_angle':180,
                    'end_angle':360,
                    'style':"FD"
                }
            },
            'color':{
                'r':0,
                'g':255,
                'b':255
            }
        }
    ]
}

pdf = PieChart()
pdf.add_page()
pdf.dibujaGrafico(config)
pdf.output('./reports/graficoCircular.pdf')
