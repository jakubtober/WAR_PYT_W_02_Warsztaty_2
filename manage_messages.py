
import argparse
from flask import Flask, request
from mysql.connector import connect
from datetime import datetime

from models.users import Users
from models.messages import Messages
from models.clcrypto import password_hash, generate_salt, check_password

cnx = connect(user='root', password='coderslab', host='127.0.0.1', database='workshop_2')
cursor = cnx.cursor()


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def show_objects():

    help = """<h2>Help</h2>use <strong>-u --username -p --password -l</strong> to show your messages</br>
    use <strong>-u --username -p --password -t -to -s --send</strong> to send new message</br>
    """

    # args: -u --username + -p --password + -l --list
    # check username and password, if correct list all messages
    if app.config.options.username and app.config.options.password and app.config.options.list:
        user_on_the_list = False
        users = Users.load_all_users(cursor)
        for user in users:
            if app.config.options.username == user.username and check_password(app.config.options.password, user.hashed_password):
                user_on_the_list = True
                list_of_messages = '<h2><strong>{} in-box</strong></h2>'.format(user.username)
                all_messages = Messages.load_all_messages_for_user(cursor, user.id)

                for message in all_messages:
                    from_user = Users.load_user_by_id(cursor, message.from_user)
                    to_user = Users.load_user_by_id(cursor, message.to_user)
                    list_of_messages +="<p>Message id: {}</br>From: {}</br>Message: {}</br>Date: {}</p>".format(
                        message.id,
                        from_user.username,
                        message.text,
                        message.date
                    )

                return list_of_messages

        if user_on_the_list == False:
            return 'Pls enter correct credentials...'

    # args: -u --username + -p --password + -s --send + -t --to
    # check username and password, if correct check receiver and save message in the database
    if app.config.options.username and app.config.options.password and app.config.options.send and app.config.options.to:
        users = Users.load_all_users(cursor)
        receiver_on_the_list = False
        user_on_the_list = False

        for user in users:
            if app.config.options.username == user.username and check_password(app.config.options.password, user.hashed_password):
                user_on_the_list = True
                for receiver in users:
                    if app.config.options.to == receiver.username:
                        receiver_on_the_list = True
                        new_message = Messages()
                        new_message.from_user = user.id
                        new_message.to_user = receiver.id
                        new_message.text = app.config.options.send
                        new_message.date = datetime.today()
                        new_message.save_to_db(cursor)
                        cnx.commit()
                        return "Your message has been sent."
                if receiver_on_the_list == False:
                    return "Sorry we don't have this receiver in the database..."

        if user_on_the_list == False:
            return 'Pls enter correct credentials...'

    return help



def set_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username",
                        action="store", dest="username", default=False,
                        help="test")
    parser.add_argument("-p", "--password",
                        action="store", dest="password", default=False,
                        help="test")
    parser.add_argument("-l", "--list",
                        action="store_true", dest="list", default=False,
                        help="test")
    parser.add_argument("-t", "--to",
                        action="store", dest="to", default=False,
                        help="test")
    parser.add_argument("-s", "--send",
                        action="store", dest="send", default=False,
                        help="test")

    options = parser.parse_args()
    return options


def solution(options):
    app.config.options = options
    app.run(debug=True)


if __name__ == "__main__":
    solution(set_options())

