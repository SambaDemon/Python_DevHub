from __future__ import absolute_import
from .sample_tests import *
from .request.config import Config

###-----------------------CONFIGURE THE API------------------------###

# Config.license = "" # !!! REQUIRED !!!

#   - The rest are all optional...

# Config.baseEndpoint = "apis.cert.vantiv.com" #this is the default
# Config.version = 1 #this is the default value

#   - If your company has a proxy, set the proxy object and if it uses authentication, base64 encode your username and password
# Config.proxy = {'https': 'https://User:Password@example.example.com:8080/'} #sample proxy setting

#   - For debugging
# Config.printRequest = False
# Config.printResponse = False
# Config.doNotSend = False # if set to True, request.send() will return the request and will not send the transaction
# ^^^^^^^^^^^^^^^^^^^^^^^^CONFIGURE THE API^^^^^^^^^^^^^^^^^^^^^^^^#

#   Uncomment the #sample transaction below that you would like to test


#  CREDIT
def test_credits():
    sampleCreditAuthorization()
    sampleCreditAuthorizationCompletion()
    sampleCreditCaptureGivenAuth()
    sampleCreditCredit()
    sampleCreditForce()
    sampleCreditReturn()
    sampleCreditReversal()
    sampleCreditSale()
    sampleCreditVoid()


#  CHECK
def test_checks():
    sampleCheckCredit()
    sampleCheckReturn()
    sampleCheckSale()
    sampleCheckVerification()
    sampleCheckVoid()


# SERVICES
def test_services():
    sampleCreatePlan()
    sampleFraudCheck()
    samplePaymentAccountCreate()
    sampleScheduledTaskDelete()
    sampleScheduledTaskUpdate()
    samplePaymentAccountUpdate()
    sampleUpdatePlan()
