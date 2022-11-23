import pymysql

class sqlconect:
    def Open(self):
        connection = pymysql.connect( host='localhost',
                                      user='root',
                                      password='Jeronimo108',
                                      database='Movie_proyect'
                                    )
        return connection
