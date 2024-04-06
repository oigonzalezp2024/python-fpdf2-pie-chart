# https://py-self.github.io/fpdf2/Shapes.html

from fpdf import FPDF

class PieChart(FPDF):

    def dibujaGrafico(self, config):
        self.config = config
        self.data = config['data']
        self.ubicacion = config['ubicacion']
        self.diametro = config['diametro']
        self.calculos()
        self.graficoMarco()
        self.graficoTitulo()
        self.graficoLeyenda()
        self.graficoCircular()
        self.graficoPie()

    def calculos(self):
        ubicacion = self.ubicacion
        diametro = self.diametro
        self.circleX = int(ubicacion['x'])+(int(diametro)/4)
        self.circleY = int(ubicacion['y'])+(int(diametro)/4)
        self.circleR = int(diametro)/2

    def graficoMarco(self):
        config = self.config
        set_fill_color = config['graficoMarco']['set_fill_color']
        rect           = config['graficoMarco']['rect']
        diametro = int(config['diametro'])
        nroRegistros = len(self.data)
        self.set_fill_color(
            r=int(set_fill_color['r']),
            g=int(set_fill_color['g']),
            b=int(set_fill_color['b'])
        )
        
        if((diametro+15) > ((nroRegistros*10)+20)):
            h=diametro+20
        else:
            h=(nroRegistros*10)+25

        self.rect(
            x=rect['x'],
            y=rect['y'],
            w=rect['w'],
            h=h,
            style=rect['style']
        )

    def graficoTitulo(self):
        config = self.config
        set_font       = config['graficoTitulo']['set_font']
        set_text_color = config['graficoTitulo']['set_text_color']
        text           = config['graficoTitulo']['text']
        self.set_font(
            family=set_font['family'],
            style=set_font['style'],
            size=set_font['size']
        )
        self.set_text_color(
            r=set_text_color['r'],
            g=set_text_color['g'],
            b=set_text_color['b']
        )
        self.text(
            x=text['x'],
            y=text['y'],
            text=text['text']
        )

    def graficoPie(self):
        config = self.config
        set_font       = config['graficoPie']['set_font']
        set_text_color = config['graficoPie']['set_text_color']
        text           = config['graficoPie']['text']
        nroRegistros = len(self.data)
        ubicacion = self.config['ubicacion']
        diametro = self.config['diametro']
        self.set_font(
            family = set_font['family'],
            style = set_font['style'],
            size = set_font['size']
        )
        self.set_text_color(
            r = set_text_color['r'],
            g = set_text_color['g'],
            b = set_text_color['b']
        )

        if((diametro+15) > ((nroRegistros*10)+20)):
            y = ubicacion['y']+diametro+10
        else:
            y = ubicacion['y']+(nroRegistros*10)+15

        self.text(
            x=text['x'],
            y=y,
            text=text['text'],
        )

    def graficoCircular(self):
        config = self.config
        self.set_line_width(config['set_line_width'])
        for item in config['data']:
            self.graficoCircularColor(item)
            self.graficoCircularSector(item)
        self.graficoCircularCentral()

    def graficoCircularColor(self, item):
        self.set_fill_color(
            r=item['color']['r'],
            g=item['color']['g'],
            b=item['color']['b']
        )

    def graficoCircularSector(self, item):
        config=self.config
        solid_arc=item['graficoCircularSector']['solid_arc']
        self.solid_arc(
            x= config['ubicacion']['x'],
            y= config['ubicacion']['y'],
            a= solid_arc['a'],
            b= solid_arc['b'],
            start_angle= solid_arc['start_angle'],
            end_angle  = solid_arc['end_angle'],
            style      = solid_arc['style']
        )

    def graficoCircularCentral(self):
        config = self.config
        circleX = self.circleX
        circleY = self.circleY
        circleR = self.circleR
        set_fill_color = config['graficoMarco']['set_fill_color']
        self.set_line_width(config['set_line_width'])
        self.set_draw_color(0)
        self.set_fill_color(
            r=set_fill_color['r'],
            g=set_fill_color['g'],
            b=set_fill_color['b']
        )
        self.circle(
            x=(circleX), 
            y=(circleY), 
            r=(circleR), 
            style="FD"
        )

    def graficoLeyenda(self):
        self.leyendaMarquito()
        self.leyendaCuadritos()
        self.leyendaTexto()

    def leyendaMarquito(self):
        config = self.config
        diametro = int(config['diametro'])
        ubicacion = config['ubicacion']
        set_fill_color = config['leyendaMarquito']['set_fill_color']
        rect = config['leyendaMarquito']['rect']
        nroRegistros = len(self.data)
        self.set_fill_color(
            r=set_fill_color['r'],
            g=set_fill_color['g'],
            b=set_fill_color['b']
        )
        self.rect(
            x=int(ubicacion['x'])+diametro+5,
            y=int(ubicacion['y']),
            w=config['leyendaMarquito']['rect']['w'],
            h=(nroRegistros*10)+5,
            style=rect['style'],
        )

    def leyendaCuadritos(self):
        circleR = self.circleR
        ubicacion = self.ubicacion
        diametro = self.config['diametro']
        data = self.data
        i=5
        for item in data:
            color = item['color']
            self.set_fill_color(
                r=color['r'],
                g=color['g'],
                b=color['b']
            )
            self.rect(
                x=int(ubicacion['x']+diametro+10), 
                y=int(ubicacion['y'])+i, 
                w=5,
                h=5,
                style="FD"
            )
            i+=10   

    def leyendaTexto(self):
        data = self.data
        circleX = self.circleX
        circleR = self.circleR
        diametro = self.config['diametro']
        ubicacion = self.config['ubicacion']
        self.set_font('Times','B', 12)
        self.set_text_color(0,0,0)
        i=8.5
        for item in data:
            text = item['text']
            self.text(
                x=int(ubicacion['x'])+diametro+20,
                y=int(ubicacion['y'])+i,
                text=text
            )
            i+=10
