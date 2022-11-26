import pymysql

class sqlconect:
    def __init__(self):

        self.ip = ''

    def Open(self):
        connection = pymysql.connect( host='localhost',
                                      user='root',
                                      password='Jeronimo108',
                                      database='prueba'
                                    )
        return connection

    def insertValuesInterface(self, ip):

        cone = self.Open()
        cursor = cone.cursor()
        sql = "insert into Interface(ip) values(%s)"
        cursor.execute(sql, ip)
        cone.commit()
        cone.close()

    def insertValues(self, hostname, ip):
        pass

    def get_ip(self):

        cone = self.Open()
        cursor = cone.cursor()
        sql = 'select ip from Interface where id_deice = 1'
        cursor.execute(sql)
        data = cursor.fetchall()
        cone.close()
        print(data)

