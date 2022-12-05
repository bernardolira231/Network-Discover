import pymysql

class sqlconect:
    def Open(self):
        connection = pymysql.connect( host='localhost',
                                      user='root',
                                      password='Jeronimo108',
                                      database='prueba'
                                    )
        return connection

    def insertValuesInterface(self, l):

        cone = self.Open()
        cursor = cone.cursor()
        for i in l:
            sql = "insert into Interface(ip, hostname) values(%s, %s)"
            cursor.execute(sql, i)
            cone.commit()
        cone.close()

    def insertValues(self, dev):
        cone = self.Open()
        cursor = cone.cursor()
        for i in dev:
            sql = "insert into Device(type, hostname) values(%s, %s)"
            cursor.execute(sql, dev)
        cone.commit()
        cone.close()


    def get_ip(self):

        cone = self.Open()
        cursor = cone.cursor()
        sql = 'select ip from Interface where id_deice = 1'
        cursor.execute(sql)
        data = cursor.fetchall()
        cone.close()
        print(data)

