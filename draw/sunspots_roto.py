from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from reportlab.lib import colors
from urllib import urlopen
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label

URL = "http://services.swpc.noaa.gov/text/predicted-sunspot-radio-flux.txt"
COMMENT_CHARS = "#:"

drawing = Drawing(400, 200)
data = []
for line in urlopen(URL).readlines():
    if not line.isspace() and line[0] not in COMMENT_CHARS:
        data.append([float(n) for n in line.split()])

print data

pred = [row[2] for row in data]
high = [row[3] for row in data]
low = [row[4] for row in data]
times = [row[0] + row[1]/12.0 for row in data]

lp = LinePlot()
lp.x = 50
lp.y = 50
lp.width = 300
lp.height = 125
lp.data = [zip(times, pred), zip(times, high), zip(times, low)]
lp.lines[0].strokeColor = colors.blue
lp.lines[1].strokeColor = colors.red
lp.lines[2].strokeColor = colors.green

drawing.add(lp)
drawing.add(String(250, 150, "sunSpots", fontSize=14, fillColor=colors.red))
renderPDF.drawToFile(drawing, "report.pdf", "sunSpots")




