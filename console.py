#!/usr/bin/python3
"""Module for console for controlling"""

from cmd import Cmd
from models import storage
from models.user import User
from models.location import Location
from datetime import datetime, timedelta



classes = {'User': User, 'Location': Location}

class Console(Cmd):
    """Console class"""
    prompt = 'Weather$ '
    intro = 'Welcome to the Weather console app!'



    def do_EOF(self, line):
        """Exit the console"""
        return True

    def do_quit(self, line):
        """Exit the console"""
        print('ByeBye')
        return True

    def emptyline(self):
        """Do nothing"""
        pass

    def do_create_expired(self, line):
        """create user with attributes for testing"""
        if not line:
            print('** class name missing **')
            return
        if line != 'User':
            print('enter User')
            return
        new = User()
        new.last_active = datetime.now() - timedelta(days=15)
        new.save()
        print(new.id)
    def do_exdelete(self, line):
        """Do delete method on users who are not active for 14 days"""
        storage.delete_expired_users()
        print('Expired sessions deleted successfully')

    def do_delete_session(self, line):
        """Delete a session"""
        storage.get(User, line).delete()

if __name__ == '__main__':
    storage.reload()
    console = Console()
    console.cmdloop()
