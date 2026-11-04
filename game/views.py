from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align: center">术士之战</h1>'
    line4 = '<a href="/play/">进入游戏页面</a>'
    line3 = '<hr>'
    line2 = '<img src="https://ts1.tc.mm.bing.net/th/id/R-C.632752e756bdfc963a0d7e401be10889?rik=JO1r3dCjvwc3lg&riu=http%3a%2f%2fi2.hdslb.com%2fbfs%2farchive%2f76e5df2984c8880a1aae8fb67c9b3a42b3d2665e.png&ehk=vpG4%2bt5%2fFqfOqU5tm2%2fYcxDjucZTmNMm0hP83HYit0o%3d&risl=&pid=ImgRaw&r=0">'
    return HttpResponse(line1 + line4 + line3 + line2)

def play(request):
    line1 = '<h1 style = "text-align: center">游戏界面</h1>'
    line3 = '<a href="/">返回主页面</a>'
    line2 = '<img src="https://tse2-mm.cn.bing.net/th/id/OIP-C.GCmI2yl0wNLdBHAsY1FqiwHaFm?w=216&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3" width=2000>'
    return HttpResponse(line1 + line3 + line2)
