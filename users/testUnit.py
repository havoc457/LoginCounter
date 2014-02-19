from django.test import TestCase
from UsersModel import UsersModel
from users.models import User
# Create your tests here.



class testUnit(TestCase):
	Err_Num = -1 
	Good_Num = 1

	def setUp(self):
		newOne = User(user = 'abcd', password = 'abcd' )
		newOne.save()

	def testLogin(self):   ### good one 
		dataUser = UsersModel()
		self.assertEqual(dataUser.login('abcd', 'abcd'), (UsersModel.SUCCESS, self.Good_Num ))  ### count = 2

	def testAdd(self):    ### good one 
		dataUser = UsersModel()
		self.assertEqual(dataUser.add('123', '123'), (UsersModel.SUCCESS, self.Good_Num))
		
	def testLoginWrongPassWord(self): #### Error
		dataUser = UsersModel()
		self.assertEqual(dataUser.login('123', '456'), (UsersModel.ERR_BAD_CREDENTIALS, self.Err_Num))

	def testNullNull(self): #### Error
		dataUser = UsersModel()
		self.assertEqual(dataUser.login('', ''), (UsersModel.ERR_BAD_USERNAME, self.Err_Num))

	def testAddNullUserName(self):  ### Error 
		dataUser = UsersModel()
		self.assertEqual(dataUser.add('', '456'), (UsersModel.ERR_BAD_USERNAME, self.Err_Num))
	
	def testAddNullPassWord(self):  ### good one
		dataUser = UsersModel()
		self.assertEqual(dataUser.add('abc', ''), (UsersModel.SUCCESS, self.Good_Num))

	def testAddLongUserName(self):  ## Error 
		user = '1' * 130
		dataUser = UsersModel()
		self.assertEqual(dataUser.add(user, '1234'), (UsersModel.ERR_BAD_USERNAME, self.Err_Num))

	def testAddDuplicateUserName(self):### Error 
		dataUser = UsersModel()
		self.assertEqual(dataUser.add('abcd', '456'), (UsersModel.ERR_USER_EXISTS, self.Err_Num))
		
	def testAddLongPassWord(self): ## Error 
		password = '1' * 200
		dataUser = UsersModel()
		self.assertEqual(dataUser.add('kkkk', password), (UsersModel.ERR_BAD_PASSWORD, self.Err_Num))
		

	def testRestartFixture(self):
		dataUser = UsersModel()
		self.assertEqual(dataUser.TESTAPI_resetFixture(), UsersModel.SUCCESS)
		try:
			getUser = User.objects.get(user = '123')
			self.assertEqual(True, False)
		except:
			self.assertEqual(True, True)

