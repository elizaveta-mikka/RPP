import cherrypy
from models import *

id_com = [x for x in Comments.select()]
s_max_com = 'max="' + str(len(id_com)) + '"'
id_post = [x for x in Posts.select()]
s_max_post = 'max="' + str(len(id_post)) + '"'
id_comment = []
def tables(n_tab):
    s = ""
    if n_tab == 1:
        for x in Posts.select():
            s += "<tr>"
            s += "<td>" + str(x.id) + "</td>"
            s += "<td>" + str(x.n_post) + "</td>"
            s += "<td>" + str(x.n_comm) + "</td>"
            s += "</tr>"
    else:
        for x in Comments.select():
            s += "<tr>"
            s += "<td>" + str(x.id) + "</td>"
            s += "<td>" + str(x.id_chng) + "</td>"
            s += "<td>" + str(x.date) + "</td>"
            s += "<td>" + str(x.time) + "</td>"
            s += "<td>" + str(x.text) + "</td>"
            s += "<td>" + str(x.likes) + "</td>"
            s += "</tr>"
    return s


class DB_Tables(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head><p align="center"><b><font size="6">Комментарии к посту<b></p></head>
          <p></p></font>
          <body>
            <div> 
                <p></p>
                <form action="view_tab">
                    <button type="submit"><font size="4">Просмотр</font></button>
                </form>
                <p></p>
            </div>
            <div> 
                <p></p>
                <form action="change_tab">
                    <button type="submit"><font size="4">Изменение</font></button>
                </form>
                <p></p>
            </div>
            <div> 
                <p></p>
                <form action="add_tab">
                    <button type="submit"><font size="4">Добавление</font></button>
                </form>
                <p></p>
            </div>
          </body>
        </html>"""

    @cherrypy.expose
    def add_tab(self):
        return """<html>
            <head><p align="center"><b><font size="6">Добавление записи в таблицу описание комментариев<b></p></head>
            <p></p></font>
            <body>
            <form  method="get" action="save_new">
                <table border = "2" align="center">
                    <tr>
                        <td align="center">ID изменения</td>
                        <td align="center">Дата</td>
                        <td align="center">Время</td>
                        <td align="center">Текст</td>
                        <td align="center">Количество лайков</td>
                    </tr>
                    <tr>
                        <td><input type="number" value="1" name="id_ch" min="1" """ + s_max_post + """"/></td>
                        <td><input type="number" value="01" name="day" min="1" max="31"/>-
                        <input type="number" value="01" name="mon" min="1" max="12"/>-
                        <input type="number" value="2000" name="year" min="2000" max="2030"/></td>
                        <td><input type="number" value="00" name="hour" min="0" max="23"/>:
                        <input type="number" value="00" name="minu" min="0" max="60"/></td>
                        <td><input type="text" value="Комментарий" name="text"/></td>
                        <td><input type="number" value="0" name="likes" min="0"/></td>
                    </tr> 
                </table>
                <p align="center"><button type="submit"><font size="4">Создать запись</font></button></p>
            </form>
            </body>
            </html>"""

    @cherrypy.expose
    def save_new(self, id_ch, day, mon, year, hour, minu, text, likes):
        s_date = day + '.' + mon + '.' + year
        s_time = hour + ':' + minu
        comment = Comments.create(id_chng = id_ch, date = s_date, time = s_time, text = text, likes = likes)
        return """<html>
                <head><p align="center"><b><font size="6">Запись сохранена<b></p></head>
                <p></p></font>
                <body>
                <form action="index">
                    <p align="center"><button type="submit"><font size="4">Вернуться на главную страницу</font></button></p>
                </form>
                </body>
                </html>"""

    @cherrypy.expose
    def view_tab(self):
        return """<html>
            <head><p align="center"><b><font size="6">Просмотр таблиц<b></p></head>
            <p></p></font>
            <body>
            <table>
                <tr>
                    <td>
                        <p><font size="4">Посты и комментарии к ним</font></p>
                        <table border = "2">
                            <tr>
                                <td>ID изменения</td>
                                <td>№ поста</td>
                                <td>№ комментария под постом</td>
                            </tr>
                            """ + tables(1) + """ 
                        </table>
                    </td>
                    <td width = "100">
                    </td>
                    <td>
                        <p><font size="4">Описание комментариев</font></p>
                        <table border = "2">
                        <tr>
                            <td>ID комментария</td>
                            <td>ID изменения</td>
                            <td>Дата</td>
                            <td>Время</td>
                            <td>Текст</td>
                            <td>Количество лайков</td>
                        </tr>
                        """ + tables(2) + """ 
                        </table>
                    </td>
                </tr>
            </table>
            </body>
            </html>"""

    @cherrypy.expose
    def change_tab(self):
        return """<html>
            <head><p align="center"><b><font size="6">Изменение таблицы описания комментария<b></p></head>
            <p></p></font>
            <body>
            <form  method="get" action="change">
                <p><font size="4">Выведите ID комментария, который хотите изменить</font></p>
                <input type="number" value="1" name="id" min="1" """ + s_max_com + """"/>
                <p></p>
                <button type="submit"><font size="4">Изменить запись</font></button>
            </form>
            </body>
            </html>"""

    @cherrypy.expose
    def change(self, id=1):
        id_comment.append(id)
        comment = Comments.select().where(Comments.id == id).get()
        return """<html>
        <head><p align="center"><b><font size="6">Изменение записи с ID """ + str(id) +"""<b></p></head>
        <p></p></font>
        <body>
        <form  method="get" action="update">
            <table border = "2" align="center">
                <tr>
                    <td align="center">ID изменения</td>
                    <td align="center">Дата</td>
                    <td align="center">Время</td>
                    <td align="center">Текст</td>
                    <td align="center">Количество лайков</td>
                </tr>
                <tr>
                    <td><input type="number" value='""" + str(comment.id_chng) + """' name="id_ch" min="1" """ + s_max_post + """"/></td>
                    <td><input type="number" value="" name="day" min="1" max="31"/>-
                    <input type="number" value="" name="mon" min="1" max="12"/>-
                    <input type="number" value="" name="year" min="2000" max="2030"/></td>
                    <td><input type="number" value="" name="hour" min="0" max="23"/>:
                    <input type="number" value="" name="minu" min="0" max="60"/></td>
                    <td><input type="text" value="" name="text"/></td>
                    <td><input type="number" value="" name="likes" min="0"/></td>
                </tr> 
            </table>
            <p align="center"><button type="submit"><font size="4">Сохранить изменения</font></button></p>
        </form>
        </body>
        </html>"""

    @cherrypy.expose
    def update(self, id_ch, day, mon, year, hour, minu, text, likes):
        comment = Comments.select().where(Comments.id == id_comment[-1]).get()
        comment.id_chng = id_ch
        if day != "" and mon != "" and year != "":
            comment.date = day + '.' + mon + '.' + year
        if hour != "" and minu != "":
            comment.time = hour + ':' + minu
        if text != "":
            comment.text = text
        if likes != "":
            comment.likes = likes
        comment.save()
        return """<html>
        <head><p align="center"><b><font size="6">Изменение внесено<b></p></head>
        <p></p></font>
        <body>
        <form action="index">
            <p align="center"><button type="submit"><font size="4">Вернуться на главную страницу</font></button></p>
        </form>
        </body>
        </html>"""
        

if __name__ == '__main__':
    cherrypy.quickstart(DB_Tables())