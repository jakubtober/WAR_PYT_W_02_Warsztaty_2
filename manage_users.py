
import argparse
from flask import Flask, request
from mysql.connector import connect

from models.users import Users
from models.clcrypto import password_hash, generate_salt, check_password

cnx = connect(user='root', password='coderslab', host='127.0.0.1', database='workshop_2')
cursor = cnx.cursor()


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def show_objects():

    help = """<h2>Help</h2>use <strong>-u --username -p --password</strong> to create new user or check if it exists in the database</br>
    use <strong>-u --username -p --password -e --edit</strong> to set new password</br>
    use <strong>-u --username -p --password -d --delete</strong> to delete user</br>
    use <strong>-l --list</strong> to list all users
    """

    # args: -u --username + -p --password
    # check if such username exists in database, if not -> create username and password, else raise error
    # by default username = email
    if app.config.options.username and app.config.options.password and not app.config.options.edit and not app.config.options.delete:
        users = Users.load_all_users(cursor)
        for user in users:
            if app.config.options.username == user.username and check_password(app.config.options.password, user.hashed_password):
                return 'I found this user in the database'

        new_user = Users()
        new_user.set_password(app.config.options.password, None)
        new_user.username = app.config.options.username
        new_user.email = app.config.options.username
        print(new_user.username)
        print(new_user.email)
        new_user.save_to_db(cursor)
        cnx.commit()

        return 'I have created new user'

    # args: -u --username + -p --password + -e --edit + -n --new-pass
    # check if password is correct, if it is correct save new password (from -p argument)
    if app.config.options.username and app.config.options.password and app.config.options.edit and app.config.options.newpass:
        users = Users.load_all_users(cursor)
        for user in users:
            if app.config.options.username == user.username and check_password(app.config.options.password, user.hashed_password):
                user.set_password(app.config.options.newpass, None)
                user.save_to_db(cursor)
                cnx.commit()
                return 'Password has been changed.'

        return "<strong>Smth went wrong</strong></br>-u --username: {}</br> -p --password: {}</br> -e --edit: {}".format(app.config.options.username,
                                                                                    app.config.options.password, app.config.options.edit)
    # args: -u --username + -p --password + -d --delete
    # check if password is correct, if it is then delete user from the database
    if app.config.options.username and app.config.options.password and app.config.options.delete:
        users = Users.load_all_users(cursor)
        for user in users:
            if app.config.options.username == user.username and check_password(app.config.options.password, user.hashed_password)\
                    and app.config.options.delete == user.email:
                user.delete(cursor)
                cnx.commit()
                return 'User deleted.'

        return "Smth went wrong, maybe wrong username and/or password?"

    # display list of the users
    if app.config.options.list:
        if app.config.options.list:
            all_users = ''
            users = Users.load_all_users(cursor)
            for user in users:
                all_users += '<p><strong>Username:</strong> {}</br> <strong>Email:</strong> {}</br></p>'.format(user.username, user.email)
        return all_users

    return help



def set_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username",
                        action="store", dest="username", default=False,
                        help="test")
    parser.add_argument("-p", "--password",
                        action="store", dest="password", default=False,
                        help="test")
    parser.add_argument("-n", "--newpass",
                        action="store", dest="newpass", default=False,
                        help="test")
    parser.add_argument("-l", "--list",
                        action="store_true", dest="list", default=False,
                        help="test")
    parser.add_argument("-d", "--delete",
                        action="store", dest="delete", default=False,
                        help="test")
    parser.add_argument("-e", "--edit",
                        action="store", dest="edit", default=False,
                        help="test")

    options = parser.parse_args()
    return options


def solution(options):
    app.config.options = options
    app.run(debug=True)


if __name__ == "__main__":
    solution(set_options())

