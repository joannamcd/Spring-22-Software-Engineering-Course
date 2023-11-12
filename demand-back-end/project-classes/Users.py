import bcrypt


class Users:

    def __init__(self, first_name, last_name, email, user_name, password, phone=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.user_name = user_name

        # hashing pass with bcrypt
        hashPass = password.encode('utf-8')
        password = bcrypt.hashpw(hashPass, bcrypt.gensalt())
        self.password = password

        if phone is None:
            self.phone = -1
        else:
            self.phone = phone


class TaaSUsers(Users):

    def __init__(self, first_name, last_name, email, user_name, password, home_address, city, zipcode, state,
                 phone=None):
        super().__init__(first_name, last_name, email, user_name, password, phone)
        self.home_address = home_address
        self.city = city
        self.zipcode = zipcode
        self.state = state

    def _is_valid_firstName(self, first_name):
        if len(first_name) > 30:
            raise ValueError("First Name cannot exceed 30 characters.")
        return first_name

    def _is_valid_lastName(self, last_name):
        if len(last_name) > 30:
            raise ValueError("Last Name cannot exceed 30 characters.")
        return last_name

    def _is_valid_email(self, email):
        regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if not regex.match(regex, email):
            raise ValueError("It's not an email address.")
        return email

    def _is_valid_userName(self, user_name):
        if len(user_name) > 30:
            raise ValueError("User Name cannot exceed 30 characters.")
        return user_name

    def _is_valid_home_address(self, home_address):
        if len(home_address) > 40:
            raise ValueError("Address cannot exceed 40 characters.")
        return home_address

    def _is_valid_city(self, city):
        if len(city) > 30:
            raise ValueError("City cannot exceed 30 characters.")
        return city

    def _is_valid_zipcode(self, zipcode):
        if len(zipcode) > 30:
            raise ValueError("Zipcode cannot exceed 30 characters.")
        return zipcode

    def _is_valid_state(self, state):
        if len(state) > 30:
            raise ValueError("State cannot exceed 30 characters.")
        return state

    def _is_valid_phone(self, phone):
        if len(phone) > 10:
            raise ValueError("Phone cannot exceed 10 characters.")
        return phone


class FleetManagers(Users):

    def __init__(self, first_name, last_name, email, user_name, password, assigned_fleets=None, phone=None):
        super().__init__(first_name, last_name, email, user_name, password, phone)
        self.assigned_fleets = assigned_fleets
        if assigned_fleets is None:
            self.assigned_fleets = []
        else:
            self.assigned_fleets = assigned_fleets

    def add_fleet(self, fleet):
        if fleet not in self.assigned_fleets:
            self.assigned_fleets.append(fleet)

    def remove_fleet(self, fleet):
        if fleet in self.assigned_fleets:
            self.assigned_fleets.remove(fleet)

    def print_fleets(self):
        print('-->', self.assigned_fleets)

# Example object creation calls for all existing Projectclasses
# usr1 = User('James', 'Ross', 'ross@mail.com', 'usr1', 5645634565)
# TaaSUser1 = TaaSUser('James', 'Ross', 'ross@mail.com', 'TaaS-usr1', 5645634565, '8333 bluff', phone=1436526543)
# fltMgr1 = FleetManager('James', 'Ross', 'ross@mail.com', 'FltMgr-usr1', 5645634565)
# fltMgr1.add_fleet(66)
# fltMgr1.add_fleet(676)
# fltMgr1.remove_fleet(66)
# # print(vars(obj)) shows all attributes of given object
# print(vars(usr1))
# print(vars(TaaSUser1))
# print(vars(fltMgr1))
