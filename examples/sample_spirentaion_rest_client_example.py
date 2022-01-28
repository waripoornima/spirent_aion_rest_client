"""
    This is sample example for Spirent Aion license checkouts
    Using SpirentAion rest client
"""

from py_spirentaion_rest_client.SpirentAion import SpirentAion
import json

<<<<<<< HEAD
# get aion credentials from file aion_credentials.json
# get Aion credentials :
# read json file
json_file = open('aion_credentials.json', 'r')

# store data in json object
json_object = json.load(json_file)

# close the original file
json_file.close()

aion_server = json_object['AION']['aion_server']
username = json_object['AION']['username']
password = json_object['AION']['password']
=======
# user credentials
aion_server = 'spirent.spirentaion.com'
user = 'poornima.wari@spirent.com'
password = '***'
>>>>>>> feaeceabec15ec3468255203bed28802195e94ba

# creating SpirentAion object
spirentaion_object = SpirentAion(aion_server, username, password)

# get the license server version
end_points = '/lic/version'

# calling get method
license_version = spirentaion_object.get(end_points)
print('License Server Version: {}'.format(license_version['build_number']))

# get the organization id
end_points = '/api/iam/organizations/default'
organization = spirentaion_object.get(end_points)
organization_id = organization['id']
print('Organization Id: {}'.format(organization_id))

# get the product id for Spirent TestCenter
end_points ='/inv/products'
product_list = spirentaion_object.get(end_points)
stc_id = ''
for product_dict in product_list:
    if product_dict['name'] == 'Spirent TestCenter':
        stc_id = product_dict['id']

print('Application Id: {}'.format(stc_id))

# get the license checkout
params = {
                    'view': 'current',
                    'organization_id': organization_id,
                    'application_id': stc_id,
                    'user_id': username
          }

end_points = '/lic/checkouts'
checkouts = spirentaion_object.get(end_points, params=params)
print('License checkout :{}'.format(checkouts))
