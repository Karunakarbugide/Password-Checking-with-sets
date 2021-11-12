class password_validation:

    def validate_password(self, input_password):
        password = input_password.lower()
        # reading existing password set from text file
        with open('passwordset.txt') as f:
            pwd_list = f.readlines()
            pwd_list = [x.replace('\n', "") for x in pwd_list]
            print(pwd_list)

        if len(password) < 4:
            return 'bad'
        elif password in pwd_list:
            return 'bad'
        elif "".join(filter(lambda x: not x.isdigit(), password)) in pwd_list:
            return 'bad'
        elif "".join(reversed(password)) in pwd_list:
            return 'bad'
        else:
            return 'good'




