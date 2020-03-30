from jinja2 import Template

class Report:
    def __init__ (self, date, title, subtitle, subtitle2):
        self.date = date
        self.title = title
        self.subtitle = subtitle
        self.subtitle2 = subtitle2
    
    def outputDate(self):
        return self.date

    def outputTitle(self):
        return self.title

    def subTitle(self):
        return self.subtitle
    
    def subTitle2(self):
        return self.subtitle2


textLines =[
    '로그 세팅하기',
    'utils.py 의 TODO 구현하기',
    '로그 레벨 (DEBUG, INFO, WARNING, ERROR) 수준 이해하기',
    '핸들러 (StreamHandler, FileHandler) 추가하는 코드 작성',
    '로그 포맷 설정 하는 코드 작성',
]

code = [
    'import logging',
    'logging.basicConfig(format=''%(asctime)s - %(message)s'', level=logging.INFO)',
    'logging.info(''Admin logged in'')',
]

shell =[
    '2018-07-11 20:12:06,288 - Admin logged in',
]

textLines2 = [
    'cli.py의 TODO 구현하기',
    'Subparser 메서드 적용시키기',
    'Airflow 1.0.1 - bin/cli.py 파일 참조',
    '각 커맨드에 매칭되는 함수 적용 시키기',
]

report = Report('2020.04.16',
                '3회차 Report',
                'CLI 인터페이스 구현하기',
                'CLI 인터페이스 연동')


#Content
tt = Template("{{ rep.outputTitle() }}")
title_doc = Template("{{ rep.outputDate() }} - {{ rep.outputTitle() }}")
sub_date = Template(" 일시 : {{ rep.outputDate() }} ")
sub_title = Template(" ■ {{ rep.subTitle() }}")
sub_title2 = Template(" ■ {{ rep.subTitle2() }}")

fileName =  tt.render(rep=report)
documentTitle = title_doc.render(rep=report)
title =  tt.render(rep=report)
subTitle = sub_date.render(rep=report)
subTitle2 = sub_title.render(rep=report)
subTitle3 = sub_title2.render(rep=report)

# Create document
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

pdf = canvas.Canvas(fileName)
pdf.setTitle(documentTitle)

pdfmetrics.registerFont(
    TTFont('abc','gulim.ttf')
)
pdf.setFont('abc',36)
pdf.drawCentredString(300, 770, title)

# Sub Title
def draw_subtitle(color, size, x, y, sub):
    pdf.setFillColor(color)
    pdf.setFont("abc",size)
    pdf.drawString(x,y, sub)

# Draw a line
def draw_line(x, y, degreeline):
    pdf.line(x,degreeline,y,degreeline)


# Text object 
def draw_text(x,y,size,color,list):
    text = pdf.beginText(x,y)
    text.setFont("abc", size)
    text.setFillColor(color)
    text.textLines(list)
    pdf.drawText(text)

if __name__ == '__main__' :

    draw_subtitle(colors.gray,20,40,680,subTitle)
    draw_subtitle(colors.gray,20,40,640,subTitle2)
    draw_subtitle(colors.gray,20,40,340,subTitle3)

    draw_line(30, 550, 330)
    draw_line(30, 550, 330)



    draw_text(40,580,15,colors.gray,textLines)
    draw_text(40,480,10,colors.blue,code)
    draw_text(40,420,10,colors.green,shell)
    draw_text(40,300,15,colors.gray,textLines2)

    pdf.save()