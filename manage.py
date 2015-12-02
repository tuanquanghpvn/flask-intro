import sys
from apps import manager, db
from apps.users.models import User

if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('createsuperuser', nargs='+')
    # if len(sys.argv) == 1:
    #     parser.print_help()
    #     sys.exit(1)
    # args = parser.parse_args()

    CRUSER = 'createsuperuser'
    if CRUSER in sys.argv:
        # Get information
        username = raw_input('Username: ')
        if not username:
            print('Username is require!')
            sys.exit(False)
        email = raw_input('Email: ')
        if not email:
            print('Email is require!')
            sys.exit(False)
        password = raw_input('Password: ')
        if not password:
            print('Password is require!')
            sys.exit(False)
        re_password = raw_input('Re password: ')
        if password != re_password:
            print('Re Password is not equal password!')
            sys.exit(False)

        # Save information to database
        try:
            user = User(username=username, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
        except Exception as error:
            print('Create superuser error!', error)
            sys.exit(False)

        print('Create superuser success!')
        sys.exit(True)
    manager.run()
