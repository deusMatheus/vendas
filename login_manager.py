from db_manager import db_manager as db

class Login_manager:

    def check(self, username, password):
        if(db().cursor.execute(f'SELECT username, password FROM funcionarios WHERE username = "{username}" AND password = "{password}"').fetchall()):
            return True
        else:
            return False
