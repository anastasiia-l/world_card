import requests
from random import randint


test_case = str(randint(0, 255))
url = 'http://127.0.0.1:8000/api/'
email = 'test' + str(randint(0, 255)) + 'c' + test_case + "@test.ua"
password = 'testword11'
full_name = 'test' + test_case
DOB = '1991-01-01'



def cusromer_reg_module():
    customer_registration_url = url + 'customers/registration/'
    payload = { 'username' : email, 'password': password, 'full_name' : full_name, 'DOB': DOB }
    res = requests.post(customer_registration_url, json=payload)
    print('* Customer registration' + "\n" +
      "    status code:      " + str(res.status_code) + "\n" +
      "    response content: " + res.text + "\n")

    response = eval(res.text)
    token = response["detail"]

    user_login = url + 'login/'
    payload = { 'username' : email, 'password': password}
    res = requests.post(user_login, json=payload)
    print('* Customer registration' + "\n" +
      "    status code:      " + str(res.status_code) + "\n" +
      "    response content: " + res.text + "\n")

    list_customers = url + 'customers/'
    headers = {'Authorization': 'Token ' + token}
    res = requests.get(list_customers, headers=headers)
    print('* User login' + "\n" +
      "    status code:      " + str(res.status_code) + "\n" +
      "    response content: " + res.text + "\n")


    detail_customer = url + 'customers/5/'
    res = requests.get(detail_customer, headers=headers)
    print('* Detail customer' + "\n" +
      "    status code:      " + str(res.status_code) + "\n" +
      "    response content: " + res.text + "\n")


    change_password = url + 'change_password/'
    payload = { 'username': email, 'password': password,'new_password': 'newtestword11'}
    res = requests.post(user_login, json=payload)
    print('* User change_password' + "\n" +
      "    status code:      " + str(res.status_code) + "\n" +
      "    response content: " + res.text + "\n")


    logout = url + 'logout/'
    res = requests.get(logout, headers=headers)
    print('* User logout' + "\n" +
      "    status code:      " + str(res.status_code) + "\n" +
      "    response content: " + res.text + "\n")

def institution_create_module():
    user_login = url + 'login/'
    payload = { 'username' : 'admin', 'password': 'admin'}
    res = requests.post(user_login, json=payload)
    print('* Customer registration' + "\n" +
      "    status code:      " + str(res.status_code) + "\n" +
      "    response content: " + res.text + "\n")

    response = eval(res.text)
    headers = {'Authorization': 'Token ' + response["token"]}

    list_customers = url + 'institutions/'
    payload = { 'email' : 'dsdsf@hjh.ua', 'coordinates': '(65.345, 65.3456)', 'name':'test'}
    res = requests.post(list_customers, headers=headers, json=payload)
    print('* User login' + "\n" +
      "    status code:      " + str(res.status_code) + "\n" +
      "    response content: " + res.text + "\n")

def medic_registrarion():
    registration_medic_url = url + 'medics/registration/'

    payload = {'username': email, 'password': password, 'full_name': full_name, 'inst_id': 2, 'specialty': 'Офтальмолог	'}
    res = requests.post(registration_medic_url, json=payload)
    print('* Medic registration' + "\n" +
          "    status code:      " + str(res.status_code) + "\n" +
          "    response content: " + res.text + "\n")

    response = eval(res.text)
    token = response["detail"]

    user_login = url + 'login/'
    payload = {'username': email, 'password': password}
    res = requests.post(user_login, json=payload)
    print('* Customer registration' + "\n" +
          "    status code:      " + str(res.status_code) + "\n" +
          "    response content: " + res.text + "\n")

    headers = {'Authorization': 'Token ' + token}
    logout = url + 'logout/'
    res = requests.get(logout, headers=headers)
    print('* User logout' + "\n" +
          "    status code:      " + str(res.status_code) + "\n" +
          "    response content: " + res.text + "\n")



'''
user_login = url + 'coordinates/'
payload = {'address': "ул Бучмы 20 Харьков"}
res = requests.post(user_login, json=payload)
print('* Coordinates' + "\n" +
          "    status code:      " + str(res.status_code) + "\n" +
          "    response content: " + res.text + "\n")
          
'''

"""
'
find_medic_url = url + 'medics/notification/'
find_medic_url = url + 'medics/createcall/'
find_medic_url = url + 'iot/createcall/'
find_medic_url = url + 'coordinates/'
"""

def medic_find():
    user_login = url + 'login/'
    payload = {'username': 'admin', 'password': 'admin'}
    res = requests.post(user_login, json=payload)
    print('* Login' + "\n" +
          "    status code:      " + str(res.status_code) + "\n" +
          "    response content: " + res.text + "\n")
    response = eval(res.text)
    token = response["token"]

    headers = {'Authorization': 'Token ' + token}

    find_medic_url = url + 'medics/find/'

    payload = {'call_id': 1}
    res = requests.post(find_medic_url, json=payload)
    print('* Find medic' + "\n" +
          "    status code:      " + str(res.status_code) + "\n" +
          "    response content: " + res.text + "\n")
cusromer_reg_module()
medic_find()
