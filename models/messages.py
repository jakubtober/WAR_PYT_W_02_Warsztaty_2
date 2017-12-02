# CREATE TABLE Messages(
#     id INT NOT NULL AUTO_INCREMENT,
#     from_user INT NOT NULL,
#     to_user INT NOT NULL,
#     text TEXT,
#     creation_date DATE,
#     PRIMARY KEY (id),
#     FOREIGN KEY (to_user) REFERENCES Users(id)
# );

from datetime import datetime

class Messages:
    __id = None
    from_user = None
    to_user = None
    text = None
    date = None

    def __init__(self):
        self.__id = -1
        self.from_user = 0
        self.to_user = 0
        self.text = ''
        self.date = ''

    @property
    def id(self):
        return self.__id

    @staticmethod
    def load_message_by_id(my_cursor, id):
        sql = "SELECT * FROM Messages WHERE id='%s'"
        my_cursor.execute(sql, (id,))
        data = my_cursor.fetchone()
        print(str(data))

        if data is not None:
            message = Messages()
            message.__id = data[0]
            message.from_user = data[1]
            message.to_user = data[2]
            message.text = data[3]
            message.date = data[4]
            return message
        else:
            return None

    @staticmethod
    def load_all_messages_for_user(my_cursor, to_user):
        sql = "SELECT * FROM Messages WHERE to_user='%s'"
        all_messages = []
        my_cursor.execute(sql, (to_user,))

        for message in my_cursor:
            new_message = Messages()
            new_message.__id = message[0]
            new_message.from_user = message[1]
            new_message.to_user = message[2]
            new_message.text = message[3]
            new_message.date = message[4]
            all_messages.append(new_message)
        return all_messages

    def save_to_db(self, my_cursor):
        if self.__id == -1:
            sql = "INSERT INTO Messages(from_user, to_user, text, creation_date) VALUES(%s, %s, %s, %s)"
            values = (self.from_user, self.to_user, self.text, self.date)
            my_cursor.execute(sql, values)






