# spirentaion_rest_client

SpirentAion is python ReST client for Spirent AION Service ReST API Supports HTTP-Verbs GET,POST,PUT and DELETE. 

This ReST client supports python2.7+ and python3+

https://github.com/waripoornima/spirent_aion_rest_client

# Installation and Updating
Use the package manager pip to install SpirentAion like below.
Rerun this command to check for and install updates.

	pip install py_spirentaion_rest_client # python2

	python3 -m pip install py_spirentaion_rest_client # python3


## Usage
Features:
Command Syntax/Example :

   spirentaion_object = SpirentAion(aion_server, username, Password)

* Get the Build version

			end_point = '/lic/version'
			spirentaion_object.get(end_point)


* List Users
			
			end_point = '/iam/users'
			spirentaion_object.get(end_point)


* Get application Id

			end_point = '/inv/products'
			spirentaion_object.get(end_point)

* License Checkout

			end_point = '/lic/checkouts'
			user_params = {
  			'view'='current',
			'orgnization_id' = 'org id provided by spirent',
			'application_id' = 'your application id ex: stc',
  			'user_iid' = 'your aion user id'
			}
			spirentaion_object.get(end_point,params=user_params)
                
#### Demo of some of the features:
'''
python /examples/sample_spirentaion_rest_client_example.py

	This is sample script to print version, org_id application_id 
	and current user checkouts

Note : update following variables in script for your environment:

	username = 'your username',
	password = 'your password',
	organization_id = 'org_id' <- This is optional, if not provided, rest_client will get the default spirent id 

'''

You can get default organization id 
Python code:

	url = 'https://spirent.spirentaion.com/api/iam/organizations/default'
	session = requests.Session()
	response = session.get(url)


## Contact
feel free to contact for any issue while using the spirentaion_rest_client

	poornima.wari@spirent.com
	
	temeva-support@spirent.com

## License
[MIT]
