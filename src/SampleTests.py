
from request import SampleRequests  
from request import Utilities


def sampleCreditAuthorization() :
    authorization = SampleRequests.sampleCreditAuthorization()
    response = authorization.send()
    return response


def sampleCreditAuthorizationCompletion() :
    authorization = SampleRequests.sampleCreditAuthorization()
    response = authorization.send()
    transactionID = Utilities.getTransactionID(response)
    transaction = Utilities.getValueFromKey(response, 'TransactionID')
    
    if(transactionID) :
        authorizationCompletion = SampleRequests.sampleCreditAuthorizationCompletion(transactionID)
        response = authorizationCompletion.send()
        return response
    
    print("Authorization failed. Cannot perform Authorization Completion transaction")
    return None


def sampleCreditCaptureGivenAuth() :
    captureGivenAuth = SampleRequests.sampleCreditCaptureGivenAuth()
    response = captureGivenAuth.send()
    return response


def sampleCreditCredit() :
    sale = SampleRequests.sampleCreditSale()
    response = sale.send()
    transactionID = Utilities.getTransactionID(response)
    
    if(transactionID) :
        credit = SampleRequests.sampleCreditCredit(transactionID)
        response = credit.send()
        return response
    
    print("Sale failed. Cannot perform Credit transaction")
    return None


def sampleCreditForce() :
    force = SampleRequests.sampleCreditForce()
    response = force.send()
    return response


def sampleCreditReturn() :
    return_ = SampleRequests.sampleCreditReturn()
    response = return_.send()
    return response


def sampleCreditReversal() :
    authorization = SampleRequests.sampleCreditAuthorization()
    response = authorization.send()
    transactionID = Utilities.getTransactionID(response)
    
    if(transactionID) :
        reversal = SampleRequests.sampleCreditReversal(transactionID)
        response = reversal.send()
        return response
    
    print("Authorization failed. Cannot perform Reversal transaction")
    return None


def sampleCreditSale() :
    sale = SampleRequests.sampleCreditSale()
    response = sale.send()
    return response


def sampleCreditVoid() :
    sale = SampleRequests.sampleCreditSale()
    response = sale.send()
    transactionID = Utilities.getTransactionID(response)
    
    if(transactionID) :
        void_ = SampleRequests.sampleCreditVoid(transactionID)
        response = void_.send()
        return response
    
    print("Sale failed. Cannot perform Void transaction")
    return None



def sampleCheckCredit() :
    sale = SampleRequests.sampleCheckSale()
    response = sale.send()
    transactionID = Utilities.getTransactionID(response)
    
    if(transactionID) :
        credit = SampleRequests.sampleCheckCredit(transactionID)
        response = credit.send()
        return response
    
    print("Sale failed. Cannot perform Credit transaction")
    return None


def sampleCheckReturn() :
    return_ = SampleRequests.sampleCheckReturn()
    response = return_.send()
    return response


def sampleCheckSale() :
    sale = SampleRequests.sampleCheckSale()
    response = sale.send()
    return response


def sampleCheckVerification() :
    verification = SampleRequests.sampleCheckVerification()
    response = verification.send()
    return response


def sampleCheckVoid() :
    sale = SampleRequests.sampleCheckSale()
    response = sale.send()
    transactionID = Utilities.getTransactionID(response)
    
    if(transactionID) :
        void_ = SampleRequests.sampleCheckVoid(transactionID)
        response = void_.send()
        return response
    
    print("Sale failed. Cannot perform Void transaction")
    return None



def sampleCreatePlan() :
    createPlan = SampleRequests.sampleServicesCreatePlan()
    response = createPlan.send()
    return response


def sampleFraudCheck() :
    fraudCheck = SampleRequests.sampleServicesFraudCheck()
    response = fraudCheck.send()
    return response


def samplePaymentAccountCreate() :
    paymentAccountCreate = SampleRequests.sampleServicesPaymentAccountCreate()
    response = paymentAccountCreate.send()
    return response


def sampleScheduledTaskDelete() :
    scheduledTaskDelete = SampleRequests.sampleServicesScheduledTaskDelete()
    response = scheduledTaskDelete.send()
    return response


def sampleScheduledTaskUpdate() :
    scheduledTaskUpdate = SampleRequests.sampleServicesScheduledTaskUpdate()
    response = scheduledTaskUpdate.send()
    return response


def samplePaymentAccountUpdate() :
    paymentAccountUpdate = SampleRequests.sampleServicesPaymentAccountUpdate()
    response = paymentAccountUpdate.send()
    return response


def sampleUpdatePlan() :
    updatePlan = SampleRequests.sampleServicesUpdatePlan()
    response = updatePlan.send()
    return response
