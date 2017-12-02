# CREATE TABLE Users(
#     id INT NOT NULL AUTO_INCREMENT,
#     email VARCHAR(255) NOT NULL UNIQUE,
#     username VARCHAR(255) NOT NULL,
#     hashed_password VARCHAR(255) NOT NULL,
#     PRIMARY KEY(id)
# );

from models.clcrypto import password_hash, generate_salt, check_password

class Users:
    __id = None
    username = None
    __hashed_password = None
    email = None

    def __init__(self):
        self.__id = -1
        self.username = ''
        self.__hashed_password = ''
        self.email = ''

    @property
    def id(self):
        return self.__id

    @property
    def hashed_password(self):
        return self.__hashed_password

    def set_password(self, password, salt):
        self.__hashed_password = password_hash(password, salt)

    def save_to_db(self, my_cursor):
        if self.__id == -1:
            sql = """INSERT INTO Users(username, email, hashed_password)
                     VALUES(%s, %s, %s)"""
            values = (self.username, self.email, self.hashed_password)
            my_cursor.execute(sql, values)
            self.__id = my_cursor.lastrowid
            return True
        else:
            sql = """UPDATE Users SET username=%s, email=%s, hashed_password=%s 
                     WHERE id=%s"""
            values = (self.username, self.email, self.hashed_password, self.id)
            my_cursor.execute(sql, values)
        return False

    def delete(self, my_cursor):
        sql = "DELETE FROM Users WHERE id={}".format(self.id)
        print(sql, self.id)
        my_cursor.execute(sql)
        self.__id = -1
        return True

    @staticmethod
    def load_user_by_id(my_cursor, id):
        sql = "SELECT * FROM Users WHERE id='%s'"
        my_cursor.execute(sql, (id,))
        data = my_cursor.fetchone()

        if data is not None:
            loaded_user = Users()
            loaded_user.__id = data[0]
            loaded_user.username = data[2]
            loaded_user.email = data[1]
            loaded_user.__hashed_password = data[3]
            return loaded_user
        else:
            return None

    @staticmethod
    def load_all_users(my_cursor):
        sql = "SELECT * FROM Users"
        ret = []
        my_cursor.execute(sql)
        for row in my_cursor:
            loaded_user = Users()
            loaded_user.__id = row[0]
            loaded_user.username = row[2]
            loaded_user.email= row[1]
            loaded_user.__hashed_password = row[3]
            ret.append(loaded_user)
        return ret