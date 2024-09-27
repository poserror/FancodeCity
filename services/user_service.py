from services.base_service import get

#Fetch all users
def get_users():
    return get('users')

#check if the users are from Fancode city based on the lat/long criteria
def is_fancode_city(user):
    latitude = float(user['address']['geo']['lat'])
    longitude = float(user['address']['geo']['lng'])
    return -40 <= latitude <= 5 and 5 <= longitude <= 100

#Filter users belonging to fancode city
def get_fancode_users(users):
    return [user for user in users if is_fancode_city(user)]