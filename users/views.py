from django.views.decorators.csrf import csrf_exempt #Stops login forgery
from users.UsersModel import UsersModel
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

import json
import unittest
import users.testUnit as testUnit

@csrf_exempt
def index(request):
	return render_to_response('client.html')


@csrf_exempt
def login(request):
		infoRequest = json.loads(request.body)

		response = UsersModel().login(infoRequest['user'], infoRequest['password']) 
			
		if response[0] == UsersModel.SUCCESS: # success
			result = json.dumps({'errCode' : response[0], 'count' : response[1]})
			return HttpResponse(result, content_type = 'application/json')
		else: 
			result = json.dumps({'errCode' : response[0]})
			return HttpResponse(result, content_type = 'application/json')


@csrf_exempt
def add(request):
		infoRequest = json.loads(request.body)

		response = UsersModel().add(infoRequest['user'], infoRequest['password'])
		if response[0] == UsersModel.SUCCESS: # success
			outcome = json.dumps({'errCode' : response[0], 'count' : response[1]})
			return HttpResponse(outcome, content_type = 'application/json')
		else: 
			outcome = json.dumps({'errCode' : response[0]})
			return HttpResponse(outcome, content_type = 'application/json')

	
@csrf_exempt
def unitTests(request):
		loadModule = unittest.TestLoader().loadTestsFromModule(testUnit) # load the unit test module
		fileToWrite = open("testFile", "w") # create a file to write to
		runner = unittest.TextTestRunner(stream = fileToWrite, verbosity = 2) # set up the test runner
		result = runner.run(loadModule) # start the test runner
		sumError = len(result.errors) + len(result.failures)
		total = result.testsRun
		fileToWrite.close()
		fileToRead = open("testFile", "r") # read back from the file
		outcome = json.dumps({'nrFailed' : sumError, 'output' : fileToRead.read() ,'numTests' : total})
		fileToRead.close()
		return HttpResponse(outcome, content_type = 'application/json')

	
@csrf_exempt
def reset(request):
		response = UsersModel().TESTAPI_resetFixture()   
		if response == UsersModel.SUCCESS:
			outcome = json.dumps({'errCode' : response})
			return HttpResponse(outcome, content_type = 'application/json')
