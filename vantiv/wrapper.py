from request import (Credit, Check, Services)


def credit_authorization(**kwargs):
    authorizationRequest, errors = Credit.Authorization. \
                                    __schema__().load(kwargs)

    return authorizationRequest, errors


def sampleCreditReversal(**kwargs):
    reversalRequest, errors = Credit.Reversal.__schema__().load(kwargs)

    return reversalRequest, errors


def sampleCreditAuthorizationCompletion(**kwargs):
    authorizationCompletionRequest, errors = Credit.AuthorizationCompletion.\
                                                __schema__().load(kwargs)

    return authorizationCompletionRequest, errors


def sampleCreditCaptureGivenAuth(**kwargs):
    captureGivenAuthRequest, errors = Credit.CaptureGivenAuth.\
                                     __schema__().load(kwargs)

    return captureGivenAuthRequest, errors


def sampleCreditCredit(**kwargs):
    creditRequest, errors = Credit.Credit.__schema__().load(kwargs)

    return creditRequest, errors


def sampleCreditForce(**kwargs):
    forceRequest, errors = Credit.Force.__schema__().load(kwargs)

    return forceRequest, errors


def sampleCreditReturn(**kwargs):
    returnRequest, errors = Credit.Return.__schema__().load(kwargs)

    return returnRequest, errors


def sampleCreditSale(**kwargs):
    saleRequest, errors = Credit.Sale.__schema__().load(kwargs)

    return saleRequest, errors


def sampleCreditVoid(**kwargs):
    voidRequest, errors = Credit.Void.__schema__().load(kwargs)

    return voidRequest, errors


def sampleCheckCredit(**kwargs):
    creditRequest, errors = Check.Credit.__schema__().load(kwargs)

    return creditRequest, errors


def sampleCheckReturn(**kwargs):
    returnRequest, errors = Check.Return.__schema__().load(kwargs)

    return returnRequest, errors


def sampleCheckSale(**kwargs):
    saleRequest, errors = Check.Sale.__schema__().load(kwargs)

    return saleRequest, errors


def sampleCheckVerification(kwargs):
    verificationRequest, errors = Check.Verification.__schema__().load(kwargs)

    return verificationRequest, errors


def sampleCheckVoid(**kwargs):
    voidRequest, errors = Check.Void.__schema__().load(kwargs)

    return voidRequest, errors


def sampleServicesCreatePlan(**kwargs):
    createPlanRequest, errors = Services.CreatePlan.__schema__().load(kwargs)

    return createPlanRequest, errors


def sampleServicesFraudCheck(**kwargs):
    fraudCheckRequest, errors = Services.FraudCheck.__schema__().load(kwargs)

    return fraudCheckRequest, errors


def sampleServicesPaymentAccountCreate(**kwargs):
    paymentAccountCreateRequest, errors = Services.PaymentAccountCreate.\
                                            __schema__().load(kwargs)

    return paymentAccountCreateRequest, errors


def sampleServicesScheduledTaskDelete(**kwargs):
    scheduledTaskDeleteRequest, errors = Services.ScheduledTaskDelete.\
                                            __schema__().load(kwargs)

    return scheduledTaskDeleteRequest, errors


def sampleServicesScheduledTaskUpdate(**kwargs):
    scheduledTaskUpdateRequest, errors = Services.ScheduledTaskUpdate.\
                                            __schema__().load(kwargs)

    return scheduledTaskUpdateRequest, errors


def sampleServicesPaymentAccountUpdate(**kwargs):
    paymentAccountUpdateRequest, errors = Services.PaymentAccountUpdate.\
                                            __schema__().load(kwargs)

    return paymentAccountUpdateRequest, errors


def sampleServicesUpdatePlan(**kwargs):
        updatePlanRequest, errors = Services.UpdatePlan.\
                                        __schema__().load(kwargs)

        return updatePlanRequest, errors
