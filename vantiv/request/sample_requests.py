from __future__ import absolute_import
from . import (credit, check, services, model)
from .enums import (OrderSourceEnum, CardTypeEnum, CountryEnum)


def sampleCreditAuthorization():
        authorizationRequest = credit.Authorization()

        credentials = model.Credentials()

        credentials.AcceptorID = 1147003
        authorizationRequest.Credentials = credentials

        reports = model.Report()

        reports.ReportGroup = "1243"
        authorizationRequest.Reports = reports

        transaction = model.Transaction()

        transaction.ReferenceNumber = 1
        transaction.TransactionAmount = "10.00"
        transaction.OrderSource = OrderSourceEnum.ECOMMERCE
        authorizationRequest.Transaction = transaction

        card = model.Card()

        card.CardNumber = 4457010000000009
        card.ExpirationMonth = "01"
        card.ExpirationYear = 16
        card.CVV = 349
        card.Type = CardTypeEnum.VI
        authorizationRequest.Card = card

        application = model.Application()

        application.ApplicationID = 1234
        authorizationRequest.Application = application

        return authorizationRequest


def sampleCreditReversal(transactionID):
        reversalRequest = credit.Reversal()

        credentials = model.Credentials()

        credentials.AcceptorID = "1147003"
        reversalRequest.Credentials = credentials

        reports = model.Report()

        reports.ReportGroup = "1243"
        reversalRequest.Reports = reports

        transaction = model.Transaction()

        transaction.TransactionID = transactionID
        reversalRequest.Transaction = transaction

        application = model.Application()

        application.ApplicationID = "1234"
        reversalRequest.Application = application

        return reversalRequest


def sampleCreditAuthorizationCompletion(transactionID):
        authorizationCompletionRequest = credit.AuthorizationCompletion()

        credentials = model.Credentials()

        credentials.AcceptorID = "1147003"
        authorizationCompletionRequest.Credentials = credentials

        reports = model.Report()

        reports.ReportGroup = "1243"
        authorizationCompletionRequest.Reports = reports

        transaction = model.Transaction()

        transaction.TransactionID = transactionID
        authorizationCompletionRequest.Transaction = transaction

        application = model.Application()

        application.ApplicationID = "1234"
        authorizationCompletionRequest.Application = application

        return authorizationCompletionRequest


def sampleCreditCaptureGivenAuth():
        captureGivenAuthRequest = credit.CaptureGivenAuth()

        credentials = model.Credentials()

        credentials.AcceptorID = "1147003"
        captureGivenAuthRequest.Credentials = credentials

        reports = model.Report()

        reports.ReportGroup = "1243"
        captureGivenAuthRequest.Reports = reports

        transaction = model.Transaction()

        transaction.ReferenceNumber = "1"
        transaction.TransactionAmount = "100.10"
        transaction.AuthorizationDate = "1111-11-11"
        transaction.ApprovalNumber = "1234"
        transaction.OrderSource = OrderSourceEnum.ECOMMERCE
        captureGivenAuthRequest.Transaction = transaction

        card = model.Card()

        card.CardNumber = "4457010000000009"
        card.ExpirationMonth = "01"
        card.ExpirationYear = "16"
        card.CVV = "349"
        card.Type = CardTypeEnum.VI
        captureGivenAuthRequest.Card = card

        application = model.Application()

        application.ApplicationID = "1234"
        captureGivenAuthRequest.Application = application

        return captureGivenAuthRequest


def sampleCreditCredit(transactionID):
        creditRequest = credit.Credit()

        credentials = model.Credentials()

        credentials.AcceptorID = "1147003"
        creditRequest.Credentials = credentials

        reports = model.Report()

        reports.ReportGroup = "1243"
        creditRequest.Reports = reports

        transaction = model.Transaction()

        transaction.TransactionID = transactionID
        creditRequest.Transaction = transaction

        application = model.Application()

        application.ApplicationID = "1234"
        creditRequest.Application = application

        return creditRequest


def sampleCreditForce():
        forceRequest = credit.Force()

        credentials = model.Credentials()

        credentials.AcceptorID = "1147003"
        forceRequest.Credentials = credentials

        reports = model.Report()

        reports.ReportGroup = "1243"
        forceRequest.Reports = reports

        transaction = model.Transaction()

        transaction.ReferenceNumber = "1"
        transaction.TransactionAmount = "100.10"
        transaction.OrderSource = OrderSourceEnum.ECOMMERCE
        forceRequest.Transaction = transaction

        card = model.Card()

        card.CardNumber = "4457010000000009"
        card.ExpirationMonth = "01"
        card.ExpirationYear = "16"
        card.CVV = "349"
        card.Type = CardTypeEnum.VI
        forceRequest.Card = card

        application = model.Application()

        application.ApplicationID = "1234"
        forceRequest.Application = application

        return forceRequest


def sampleCreditReturn():
        returnRequest = credit.Return()

        credentials = model.Credentials()

        credentials.AcceptorID = "1147003"
        returnRequest.Credentials = credentials

        reports = model.Report()

        reports.ReportGroup = "1243"
        returnRequest.Reports = reports

        transaction = model.Transaction()

        transaction.ReferenceNumber = "123"
        transaction.TransactionAmount = "10.00"
        transaction.OrderSource = OrderSourceEnum.ECOMMERCE
        returnRequest.Transaction = transaction

        card = model.Card()

        card.CardNumber = "4457010000000009"
        card.ExpirationMonth = "01"
        card.ExpirationYear = "16"
        card.CVV = "349"
        card.Type = CardTypeEnum.VI
        returnRequest.Card = card

        application = model.Application()

        application.ApplicationID = "1234"
        returnRequest.Application = application

        return returnRequest


def sampleCreditSale():
        saleRequest = credit.Sale()

        credentials = model.Credentials()

        credentials.AcceptorID = "1147003"
        saleRequest.Credentials = credentials

        reports = model.Report()

        reports.ReportGroup = "1243"
        saleRequest.Reports = reports

        transaction = model.Transaction()

        transaction.ReferenceNumber = "1"
        transaction.TransactionAmount = "100.10"
        transaction.OrderSource = OrderSourceEnum.ECOMMERCE
        saleRequest.Transaction = transaction

        card = model.Card()

        card.CardNumber = "4457010000000009"
        card.ExpirationMonth = "01"
        card.ExpirationYear = "16"
        card.CVV = "349"
        card.Type = CardTypeEnum.VI
        saleRequest.Card = card

        application = model.Application()

        application.ApplicationID = "1234"
        saleRequest.Application = application

        return saleRequest


def sampleCreditVoid(transactionID):
        voidRequest = credit.Void()

        credentials = model.Credentials()

        credentials.AcceptorID = "1147003"
        voidRequest.Credentials = credentials

        reports = model.Report()

        reports.ReportGroup = "1243"
        voidRequest.Reports = reports

        transaction = model.Transaction()

        transaction.TransactionID = transactionID
        voidRequest.Transaction = transaction

        application = model.Application()

        application.ApplicationID = "1234"
        voidRequest.Application = application

        return voidRequest


def sampleCheckCredit(transactionID):
        creditRequest = check.Credit()

        credentials = model.Credentials()

        credentials.AcceptorID = "1147003"
        creditRequest.Credentials = credentials

        transaction = model.Transaction()

        transaction.TransactionID = transactionID
        creditRequest.Transaction = transaction

        reports = model.Report()

        reports.ReportGroup = "1243"
        creditRequest.Reports = reports

        application = model.Application()

        application.ApplicationID = "1234"
        creditRequest.Application = application

        return creditRequest


def sampleCheckReturn():
        returnRequest = check.Return()

        credentials = model.Credentials()

        credentials.AcceptorID = "1147003"
        returnRequest.Credentials = credentials

        transaction = model.Transaction()

        transaction.ReferenceNumber = "708388073320126000"
        transaction.TransactionAmount = "12.56"
        transaction.OrderSource = OrderSourceEnum.ECOMMERCE
        returnRequest.Transaction = transaction

        demandDepositAccount = model.DemandDepositAccount()

        demandDepositAccount.DDAAccountType = "checking"
        demandDepositAccount.AccountNumber = "234"
        demandDepositAccount.RoutingNumber = "123234345"
        demandDepositAccount.CheckNumber = "456"
        demandDepositAccount.CCDPaymentInformation = "567"
        returnRequest.DemandDepositAccount = demandDepositAccount

        address = model.Address()

        address.BillingName = "John Smith"
        address.BillingAddress1 = "1 Main St."
        address.BillingCity = "Burlington"
        address.BillingState = "MA"
        address.BillingZipcode = "01803-3747"
        address.BillingEmail = "jdoe@litle.com"
        address.BillingPhone = "978-551-0040"
        address.BillingCountry = CountryEnum.USA
        returnRequest.Address = address

        reports = model.Report()

        reports.ReportGroup = "1243"
        returnRequest.Reports = reports

        application = model.Application()

        application.ApplicationID = "1234"
        returnRequest.Application = application

        return returnRequest


def sampleCheckSale():
        saleRequest = check.Sale()

        credentials = model.Credentials()

        credentials.AcceptorID = "1147003"
        saleRequest.Credentials = credentials

        transaction = model.Transaction()

        transaction.ReferenceNumber = "1"
        transaction.TransactionAmount = "100.10"
        transaction.OrderSource = OrderSourceEnum.ECOMMERCE
        saleRequest.Transaction = transaction

        address = model.Address()

        address.BillingName = "John Smith"
        address.BillingAddress1 = "1 Main St."
        address.BillingCity = "Burlington"
        address.BillingState = "MA"
        address.BillingZipcode = "01803-3747"
        address.BillingEmail = "jdoe@litle.com"
        address.BillingPhone = "978-551-0040"
        address.BillingCountry = CountryEnum.USA
        saleRequest.Address = address

        demandDepositAccount = model.DemandDepositAccount()

        demandDepositAccount.RoutingNumber = "123234345"
        demandDepositAccount.DDAAccountType = "checking"
        demandDepositAccount.CheckNumber = "456"
        saleRequest.DemandDepositAccount = demandDepositAccount

        paymentAccount = model.PaymentAccount()

        paymentAccount.PaymentAccountID = "1232343454565"
        saleRequest.PaymentAccount = paymentAccount

        reports = model.Report()

        reports.ReportGroup = "1243"
        saleRequest.Reports = reports

        application = model.Application()

        application.ApplicationID = "1234"
        saleRequest.Application = application

        return saleRequest


def sampleCheckVerification():
        verificationRequest = check.Verification()

        credentials = model.Credentials()

        credentials.AcceptorID = "1147003"
        verificationRequest.Credentials = credentials

        transaction = model.Transaction()

        transaction.ReferenceNumber = "1"
        transaction.TransactionAmount = "100.10"
        transaction.OrderSource = OrderSourceEnum.ECOMMERCE
        verificationRequest.Transaction = transaction

        address = model.Address()

        address.BillingName = "John Smith"
        address.BillingAddress1 = "1 Main St."
        address.BillingCity = "Burlington"
        address.BillingState = "MA"
        address.BillingZipcode = "01803-3747"
        address.BillingEmail = "jdoe@litle.com"
        address.BillingPhone = "978-551-0040"
        address.BillingCountry = CountryEnum.USA
        verificationRequest.Address = address

        demandDepositAccount = model.DemandDepositAccount()

        demandDepositAccount.DDAAccountType = "checking"
        demandDepositAccount.AccountNumber = "234"
        demandDepositAccount.RoutingNumber = "123234345"
        demandDepositAccount.CheckNumber = "456"
        demandDepositAccount.CCDPaymentInformation = "567"
        verificationRequest.DemandDepositAccount = demandDepositAccount

        reports = model.Report()

        reports.ReportGroup = "1243"
        verificationRequest.Reports = reports

        application = model.Application()

        application.ApplicationID = "1234"
        verificationRequest.Application = application

        return verificationRequest


def sampleCheckVoid(transactionID):
        voidRequest = check.Void()

        credentials = model.Credentials()

        credentials.AcceptorID = "1147003"
        voidRequest.Credentials = credentials

        transaction = model.Transaction()

        transaction.TransactionID = transactionID
        voidRequest.Transaction = transaction

        reports = model.Report()

        reports.ReportGroup = "1243"
        voidRequest.Reports = reports

        application = model.Application()

        application.ApplicationID = "1234"
        voidRequest.Application = application

        return voidRequest


def sampleServicesCreatePlan():
        createPlanRequest = services.CreatePlan()

        credentials = model.Credentials()

        credentials.AcceptorID = "1147003"
        createPlanRequest.Credentials = credentials

        scheduledTask = model.ScheduledTask()

        scheduledTask.Active = "true"
        scheduledTask.ScheduledTaskID = "12"
        scheduledTask.Name = "NewPlan"
        scheduledTask.Description = "Created New Plan"
        scheduledTask.RunFrequency = "WEEKLY"
        scheduledTask.Amount = "12.00"
        scheduledTask.RunCycles = "5"
        scheduledTask.TrialRunCycles = "7"
        scheduledTask.TrialRunFrequency = "DAY"
        createPlanRequest.ScheduledTask = scheduledTask

        return createPlanRequest


def sampleServicesFraudCheck():
        fraudcheckRequest = services.FraudCheck()

        credentials = model.Credentials()

        credentials.AcceptorID = "1147003"
        fraudcheckRequest.Credentials = credentials

        reports = model.Report()

        reports.ReportGroup = "1243"
        fraudcheckRequest.Reports = reports

        advancedFraudChecks = model.AdvancedFraudChecks()

        advancedFraudChecks.ThreatMetrixSessionID = "123"
        fraudcheckRequest.AdvancedFraudChecks = advancedFraudChecks

        application = model.Application()

        application.ApplicationID = "1234"
        fraudcheckRequest.Application = application

        return fraudcheckRequest


def sampleServicesPaymentAccountCreate():
        paymentAccountCreateRequest = services.PaymentAccountCreate()

        credentials = model.Credentials()

        credentials.AcceptorID = "1147003"
        paymentAccountCreateRequest.Credentials = credentials

        reports = model.Report()

        reports.ReportGroup = "1243"
        paymentAccountCreateRequest.Reports = reports

        card = model.Card()

        card.AccountNumber = "5454545454545454"
        paymentAccountCreateRequest.Card = card

        application = model.Application()

        application.ApplicationID = "1234"
        paymentAccountCreateRequest.Application = application

        return paymentAccountCreateRequest


def sampleServicesScheduledTaskDelete():
        scheduledTaskDeleteRequest = services.ScheduledTaskDelete()

        credentials = model.Credentials()

        credentials.AcceptorID = "1147003"
        scheduledTaskDeleteRequest.Credentials = credentials

        scheduledTask = model.ScheduledTask()

        scheduledTask.SubscriptionID = "12432463563564"
        scheduledTaskDeleteRequest.ScheduledTask = scheduledTask

        return scheduledTaskDeleteRequest


def sampleServicesScheduledTaskUpdate():
        scheduledTaskUpdateRequest = services.ScheduledTaskUpdate()

        credentials = model.Credentials()

        credentials.AcceptorID = "1147003"
        scheduledTaskUpdateRequest.Credentials = credentials

        scheduledTask = model.ScheduledTask()

        scheduledTask.SubscriptionID = "12432463563564"
        scheduledTask.BillingDate = "2019-10-21"
        scheduledTaskUpdateRequest.ScheduledTask = scheduledTask

        return scheduledTaskUpdateRequest


def sampleServicesPaymentAccountUpdate():
        paymentAccountUpdateRequest = services.PaymentAccountUpdate()

        credentials = model.Credentials()

        credentials.AcceptorID = "1147003"
        paymentAccountUpdateRequest.Credentials = credentials

        reports = model.Report()

        reports.ReportGroup = "1243"
        paymentAccountUpdateRequest.Reports = reports

        card = model.Card()

        card.CVV = "123"
        paymentAccountUpdateRequest.Card = card

        application = model.Application()

        application.ApplicationID = "1234"
        paymentAccountUpdateRequest.Application = application

        paymentAccount = model.PaymentAccount()

        paymentAccount.PaymentAccountID = "1112000188575454"
        paymentAccountUpdateRequest.PaymentAccount = paymentAccount

        return paymentAccountUpdateRequest


def sampleServicesUpdatePlan():
        updatePlanRequest = services.UpdatePlan()

        credentials = model.Credentials()

        credentials.AcceptorID = "1147003"
        updatePlanRequest.Credentials = credentials

        scheduledTask = model.ScheduledTask()

        scheduledTask.Active = "false"
        scheduledTask.ScheduledTaskID = "12"
        updatePlanRequest.ScheduledTask = scheduledTask

        return updatePlanRequest
