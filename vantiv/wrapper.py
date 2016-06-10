from request import (Credit, Check, Services)


def credit_authorization(**kwargs):
    authorizationRequest, errors = Credit.Authorization. \
                                    __schema__().load(kwargs)

    return authorizationRequest, errors


def credit_reversal(**kwargs):
    reversalRequest, errors = Credit.Reversal.__schema__().load(kwargs)

    return reversalRequest, errors


def credit_authorization_completion(**kwargs):
    authorizationCompletionRequest, errors = Credit.AuthorizationCompletion.\
                                                __schema__().load(kwargs)

    return authorizationCompletionRequest, errors


def credit_capture_given_auth(**kwargs):
    captureGivenAuthRequest, errors = Credit.CaptureGivenAuth.\
                                     __schema__().load(kwargs)

    return captureGivenAuthRequest, errors


def credit_credit(**kwargs):
    creditRequest, errors = Credit.Credit.__schema__().load(kwargs)

    return creditRequest, errors


def credit_force(**kwargs):
    forceRequest, errors = Credit.Force.__schema__().load(kwargs)

    return forceRequest, errors


def credit_return(**kwargs):
    returnRequest, errors = Credit.Return.__schema__().load(kwargs)

    return returnRequest, errors


def credit_sale(**kwargs):
    saleRequest, errors = Credit.Sale.__schema__().load(kwargs)

    return saleRequest, errors


def credit_void(**kwargs):
    voidRequest, errors = Credit.Void.__schema__().load(kwargs)

    return voidRequest, errors


def check_credit(**kwargs):
    creditRequest, errors = Check.Credit.__schema__().load(kwargs)

    return creditRequest, errors


def check_return(**kwargs):
    returnRequest, errors = Check.Return.__schema__().load(kwargs)

    return returnRequest, errors


def check_sale(**kwargs):
    saleRequest, errors = Check.Sale.__schema__().load(kwargs)

    return saleRequest, errors


def check_verification(kwargs):
    verificationRequest, errors = Check.Verification.__schema__().load(kwargs)

    return verificationRequest, errors


def check_void(**kwargs):
    voidRequest, errors = Check.Void.__schema__().load(kwargs)

    return voidRequest, errors


def services_create_plan(**kwargs):
    createPlanRequest, errors = Services.CreatePlan.__schema__().load(kwargs)

    return createPlanRequest, errors


def services_fraud_check(**kwargs):
    fraudCheckRequest, errors = Services.FraudCheck.__schema__().load(kwargs)

    return fraudCheckRequest, errors


def services_payment_account_create(**kwargs):
    paymentAccountCreateRequest, errors = Services.PaymentAccountCreate.\
                                            __schema__().load(kwargs)

    return paymentAccountCreateRequest, errors


def services_scheduled_task_delete(**kwargs):
    scheduledTaskDeleteRequest, errors = Services.ScheduledTaskDelete.\
                                            __schema__().load(kwargs)

    return scheduledTaskDeleteRequest, errors


def services_scheduled_task_update(**kwargs):
    scheduledTaskUpdateRequest, errors = Services.ScheduledTaskUpdate.\
                                            __schema__().load(kwargs)

    return scheduledTaskUpdateRequest, errors


def services_payment_account_update(**kwargs):
    paymentAccountUpdateRequest, errors = Services.PaymentAccountUpdate.\
                                            __schema__().load(kwargs)

    return paymentAccountUpdateRequest, errors


def services_update_plan(**kwargs):
        updatePlanRequest, errors = Services.UpdatePlan.\
                                        __schema__().load(kwargs)

        return updatePlanRequest, errors
