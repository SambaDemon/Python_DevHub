from __future__ import absolute_import

from .request import sample_requests
from .request import utils


def sampleCreditAuthorization():
    authorization = sample_requests.sampleCreditAuthorization()
    response = authorization.send()
    return response


def sampleCreditAuthorizationCompletion():
    authorization = sample_requests.sampleCreditAuthorization()
    response = authorization.send()
    transactionID = utils.get_transaction_id(response)
    transaction = utils.get_value_from_key(response, 'TransactionID')

    if (transactionID):
        authorizationCompletion = sample_requests \
            .sampleCreditAuthorizationCompletion(transactionID)
        response = authorizationCompletion.send()
        return response

    print("Authorization failed. \
          Cannot perform Authorization Completion transaction")
    return None


def sampleCreditCaptureGivenAuth():
    captureGivenAuth = sample_requests.sampleCreditCaptureGivenAuth()
    response = captureGivenAuth.send()
    return response


def sampleCreditCredit():
    sale = sample_requests.sampleCreditSale()
    response = sale.send()
    transactionID = utils.get_transaction_id(response)

    if (transactionID):
        credit = sample_requests.sampleCreditCredit(transactionID)
        response = credit.send()
        return response

    print("Sale failed. Cannot perform Credit transaction")
    return None


def sampleCreditForce():
    force = sample_requests.sampleCreditForce()
    response = force.send()
    return response


def sampleCreditReturn():
    return_ = sample_requests.sampleCreditReturn()
    response = return_.send()
    return response


def sampleCreditReversal():
    authorization = sample_requests.sampleCreditAuthorization()
    response = authorization.send()
    transactionID = utils.get_transaction_id(response)

    if (transactionID):
        reversal = sample_requests.sampleCreditReversal(transactionID)
        response = reversal.send()
        return response

    print("Authorization failed. Cannot perform Reversal transaction")
    return None


def sampleCreditSale():
    sale = sample_requests.sampleCreditSale()
    response = sale.send()
    return response


def sampleCreditVoid():
    sale = sample_requests.sampleCreditSale()
    response = sale.send()
    transactionID = utils.get_transaction_id(response)

    if (transactionID):
        void_ = sample_requests.sampleCreditVoid(transactionID)
        response = void_.send()
        return response

    print("Sale failed. Cannot perform Void transaction")
    return None


def sampleCheckCredit():
    sale = sample_requests.sampleCheckSale()
    response = sale.send()
    transactionID = utils.get_transaction_id(response)

    if (transactionID):
        credit = sample_requests.sampleCheckCredit(transactionID)
        response = credit.send()
        return response

    print("Sale failed. Cannot perform Credit transaction")
    return None


def sampleCheckReturn():
    return_ = sample_requests.sampleCheckReturn()
    response = return_.send()
    return response


def sampleCheckSale():
    sale = sample_requests.sampleCheckSale()
    response = sale.send()
    return response


def sampleCheckVerification():
    verification = sample_requests.sampleCheckVerification()
    response = verification.send()
    return response


def sampleCheckVoid():
    sale = sample_requests.sampleCheckSale()
    response = sale.send()
    transactionID = utils.get_transaction_id(response)

    if (transactionID):
        void_ = sample_requests.sampleCheckVoid(transactionID)
        response = void_.send()
        return response

    print("Sale failed. Cannot perform Void transaction")
    return None


def sampleCreatePlan():
    createPlan = sample_requests.sampleServicesCreatePlan()
    response = createPlan.send()
    return response


def sampleFraudCheck():
    fraudCheck = sample_requests.sampleServicesFraudCheck()
    response = fraudCheck.send()
    return response


def samplePaymentAccountCreate():
    paymentAccountCreate = sample_requests.sampleServicesPaymentAccountCreate()
    response = paymentAccountCreate.send()
    return response


def sampleScheduledTaskDelete():
    scheduledTaskDelete = sample_requests.sampleServicesScheduledTaskDelete()
    response = scheduledTaskDelete.send()
    return response


def sampleScheduledTaskUpdate():
    scheduledTaskUpdate = sample_requests.sampleServicesScheduledTaskUpdate()
    response = scheduledTaskUpdate.send()
    return response


def samplePaymentAccountUpdate():
    paymentAccountUpdate = sample_requests.sampleServicesPaymentAccountUpdate()
    response = paymentAccountUpdate.send()
    return response


def sampleUpdatePlan():
    updatePlan = sample_requests.sampleServicesUpdatePlan()
    response = updatePlan.send()
    return response
