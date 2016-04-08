import Boarding
import Credit
import Check
import Services
import Model

def sampleCreditAuthorization() :
        authorizationRequest = Credit.Authorization()

        credentials = Model.Credentials();
        
        credentials.AcceptorID = "1147003"
        authorizationRequest.Credentials = credentials

        reports = Model.Reports();
        
        reports.ReportGroup = "1243"
        authorizationRequest.Reports = reports

        transaction = Model.Transaction();
        
        transaction.ReferenceNumber = "1"
        transaction.TransactionAmount = "10.00"
        transaction.OrderSource = (Model.Transaction.OrderSourceEnum.ECOMMERCE)
        authorizationRequest.Transaction = transaction

        card = Model.Card();
        
        card.CardNumber = "4457010000000009"
        card.ExpirationMonth = "01"
        card.ExpirationYear = "16"
        card.CVV = "349"
        card.Type = (Model.Card.TypeEnum.VI)
        authorizationRequest.Card = card

        application = Model.Application();
        
        application.ApplicationID = "1234"
        authorizationRequest.Application = application

        return authorizationRequest

def sampleCreditReversal(transactionID) :
        reversalRequest = Credit.Reversal()

        credentials = Model.Credentials();
        
        credentials.AcceptorID = "1147003"
        reversalRequest.Credentials = credentials

        reports = Model.Reports();
        
        reports.ReportGroup = "1243"
        reversalRequest.Reports = reports

        transaction = Model.Transaction();
        
        transaction.TransactionID = transactionID
        reversalRequest.Transaction = transaction

        application = Model.Application();
        
        application.ApplicationID = "1234"
        reversalRequest.Application = application

        return reversalRequest

def sampleCreditAuthorizationCompletion(transactionID) :
        authorizationCompletionRequest = Credit.AuthorizationCompletion()

        credentials = Model.Credentials();
        
        credentials.AcceptorID = "1147003"
        authorizationCompletionRequest.Credentials = credentials

        reports = Model.Reports();
        
        reports.ReportGroup = "1243"
        authorizationCompletionRequest.Reports = reports

        transaction = Model.Transaction();
        
        transaction.TransactionID = transactionID
        authorizationCompletionRequest.Transaction = transaction

        application = Model.Application();
        
        application.ApplicationID = "1234"
        authorizationCompletionRequest.Application = application

        return authorizationCompletionRequest

def sampleCreditCaptureGivenAuth() :
        captureGivenAuthRequest = Credit.CaptureGivenAuth()

        credentials = Model.Credentials();
        
        credentials.AcceptorID = "1147003"
        captureGivenAuthRequest.Credentials = credentials

        reports = Model.Reports();
        
        reports.ReportGroup = "1243"
        captureGivenAuthRequest.Reports = reports

        transaction = Model.Transaction();
        
        transaction.ReferenceNumber = "1"
        transaction.TransactionAmount = "100.10"
        transaction.AuthorizationDate = "1111-11-11"
        transaction.ApprovalNumber = "1234"
        transaction.OrderSource = (Model.Transaction.OrderSourceEnum.ECOMMERCE)
        captureGivenAuthRequest.Transaction = transaction

        card = Model.Card();
        
        card.CardNumber = "4457010000000009"
        card.ExpirationMonth = "01"
        card.ExpirationYear = "16"
        card.CVV = "349"
        card.Type = (Model.Card.TypeEnum.VI)
        captureGivenAuthRequest.Card = card

        application = Model.Application();
        
        application.ApplicationID = "1234"
        captureGivenAuthRequest.Application = application

        return captureGivenAuthRequest

def sampleCreditCredit(transactionID) :
        creditRequest = Credit.Credit()

        credentials = Model.Credentials();
        
        credentials.AcceptorID = "1147003"
        creditRequest.Credentials = credentials

        reports = Model.Reports();
        
        reports.ReportGroup = "1243"
        creditRequest.Reports = reports

        transaction = Model.Transaction();
        
        transaction.TransactionID = transactionID
        creditRequest.Transaction = transaction

        application = Model.Application();
        
        application.ApplicationID = "1234"
        creditRequest.Application = application

        return creditRequest

def sampleCreditForce() :
        forceRequest = Credit.Force()

        credentials = Model.Credentials();
        
        credentials.AcceptorID = "1147003"
        forceRequest.Credentials = credentials

        reports = Model.Reports();
        
        reports.ReportGroup = "1243"
        forceRequest.Reports = reports

        transaction = Model.Transaction();
        
        transaction.ReferenceNumber = "1"
        transaction.TransactionAmount = "100.10"
        transaction.OrderSource = (Model.Transaction.OrderSourceEnum.ECOMMERCE)
        forceRequest.Transaction = transaction

        card = Model.Card();
        
        card.CardNumber = "4457010000000009"
        card.ExpirationMonth = "01"
        card.ExpirationYear = "16"
        card.CVV = "349"
        card.Type = (Model.Card.TypeEnum.VI)
        forceRequest.Card = card

        application = Model.Application();
        
        application.ApplicationID = "1234"
        forceRequest.Application = application

        return forceRequest

def sampleCreditReturn() :
        returnRequest = Credit.Return()

        credentials = Model.Credentials();
        
        credentials.AcceptorID = "1147003"
        returnRequest.Credentials = credentials

        reports = Model.Reports();
        
        reports.ReportGroup = "1243"
        returnRequest.Reports = reports

        transaction = Model.Transaction();
        
        transaction.ReferenceNumber = "123"
        transaction.TransactionAmount = "10.00"
        transaction.OrderSource = (Model.Transaction.OrderSourceEnum.ECOMMERCE)
        returnRequest.Transaction = transaction

        card = Model.Card();
        
        card.CardNumber = "4457010000000009"
        card.ExpirationMonth = "01"
        card.ExpirationYear = "16"
        card.CVV = "349"
        card.Type = (Model.Card.TypeEnum.VI)
        returnRequest.Card = card

        application = Model.Application();
        
        application.ApplicationID = "1234"
        returnRequest.Application = application

        return returnRequest

def sampleCreditSale() :
        saleRequest = Credit.Sale()

        credentials = Model.Credentials();
        
        credentials.AcceptorID = "1147003"
        saleRequest.Credentials = credentials

        reports = Model.Reports();
        
        reports.ReportGroup = "1243"
        saleRequest.Reports = reports

        transaction = Model.Transaction();
        
        transaction.ReferenceNumber = "1"
        transaction.TransactionAmount = "100.10"
        transaction.OrderSource = (Model.Transaction.OrderSourceEnum.ECOMMERCE)
        saleRequest.Transaction = transaction

        card = Model.Card();
        
        card.CardNumber = "4457010000000009"
        card.ExpirationMonth = "01"
        card.ExpirationYear = "16"
        card.CVV = "349"
        card.Type = (Model.Card.TypeEnum.VI)
        saleRequest.Card = card

        application = Model.Application();
        
        application.ApplicationID = "1234"
        saleRequest.Application = application

        return saleRequest

def sampleCreditVoid(transactionID) :
        voidRequest = Credit.Void()

        credentials = Model.Credentials();
        
        credentials.AcceptorID = "1147003"
        voidRequest.Credentials = credentials

        reports = Model.Reports();
        
        reports.ReportGroup = "1243"
        voidRequest.Reports = reports

        transaction = Model.Transaction();
        
        transaction.TransactionID = transactionID
        voidRequest.Transaction = transaction

        application = Model.Application();
        
        application.ApplicationID = "1234"
        voidRequest.Application = application

        return voidRequest


def sampleCheckCredit(transactionID) :
        creditRequest = Check.Credit()

        credentials = Model.Credentials();
        
        credentials.AcceptorID = "1147003"
        creditRequest.Credentials = credentials

        transaction = Model.Transaction();
        
        transaction.TransactionID = transactionID
        creditRequest.Transaction = transaction

        reports = Model.Reports();
        
        reports.ReportGroup = "1243"
        creditRequest.Reports = reports

        application = Model.Application();
        
        application.ApplicationID = "1234"
        creditRequest.Application = application

        return creditRequest

def sampleCheckReturn() :
        returnRequest = Check.Return()

        credentials = Model.Credentials();
        
        credentials.AcceptorID = "1147003"
        returnRequest.Credentials = credentials

        transaction = Model.Transaction();
        
        transaction.ReferenceNumber = "708388073320126000"
        transaction.TransactionAmount = "12.56"
        transaction.OrderSource = (Model.Transaction.OrderSourceEnum.ECOMMERCE)
        returnRequest.Transaction = transaction

        demandDepositAccount = Model.DemandDepositAccount();
        
        demandDepositAccount.DDAAccountType = "Checking"
        demandDepositAccount.AccountNumber = "234"
        demandDepositAccount.RoutingNumber = "123234345"
        demandDepositAccount.CheckNumber = "456"
        demandDepositAccount.CCDPaymentInformation = "567"
        returnRequest.DemandDepositAccount = demandDepositAccount

        address = Model.Address();
        
        address.BillingName = "John Smith"
        address.BillingAddress1 = "1 Main St."
        address.BillingCity = "Burlington"
        address.BillingState = "MA"
        address.BillingZipcode = "01803-3747"
        address.BillingEmail = "jdoe@litle.com"
        address.BillingPhone = "978-551-0040"
        address.BillingCountry = (Model.Address.BillingCountryEnum.USA)
        returnRequest.Address = address

        reports = Model.Reports();
        
        reports.ReportGroup = "1243"
        returnRequest.Reports = reports

        application = Model.Application();
        
        application.ApplicationID = "1234"
        returnRequest.Application = application

        return returnRequest

def sampleCheckSale() :
        saleRequest = Check.Sale()

        credentials = Model.Credentials();
        
        credentials.AcceptorID = "1147003"
        saleRequest.Credentials = credentials

        transaction = Model.Transaction();
        
        transaction.ReferenceNumber = "1"
        transaction.TransactionAmount = "100.10"
        transaction.OrderSource = (Model.Transaction.OrderSourceEnum.ECOMMERCE)
        saleRequest.Transaction = transaction

        address = Model.Address();
        
        address.BillingName = "John Smith"
        address.BillingAddress1 = "1 Main St."
        address.BillingCity = "Burlington"
        address.BillingState = "MA"
        address.BillingZipcode = "01803-3747"
        address.BillingEmail = "jdoe@litle.com"
        address.BillingPhone = "978-551-0040"
        address.BillingCountry = (Model.Address.BillingCountryEnum.USA)
        saleRequest.Address = address

        demandDepositAccount = Model.DemandDepositAccount();
        
        demandDepositAccount.RoutingNumber = "123234345"
        demandDepositAccount.DDAAccountType = "Checking"
        demandDepositAccount.CheckNumber = "456"
        saleRequest.DemandDepositAccount = demandDepositAccount

        paymentAccount = Model.PaymentAccount();
        
        paymentAccount.PaymentAccountID = "1232343454565"
        saleRequest.PaymentAccount = paymentAccount

        reports = Model.Reports();
        
        reports.ReportGroup = "1243"
        saleRequest.Reports = reports

        application = Model.Application();
        
        application.ApplicationID = "1234"
        saleRequest.Application = application

        return saleRequest

def sampleCheckVerification() :
        verificationRequest = Check.Verification()

        credentials = Model.Credentials();
        
        credentials.AcceptorID = "1147003"
        verificationRequest.Credentials = credentials

        transaction = Model.Transaction();
        
        transaction.ReferenceNumber = "1"
        transaction.TransactionAmount = "100.10"
        transaction.OrderSource = (Model.Transaction.OrderSourceEnum.ECOMMERCE)
        verificationRequest.Transaction = transaction

        address = Model.Address();
        
        address.BillingName = "John Smith"
        address.BillingAddress1 = "1 Main St."
        address.BillingCity = "Burlington"
        address.BillingState = "MA"
        address.BillingZipcode = "01803-3747"
        address.BillingEmail = "jdoe@litle.com"
        address.BillingPhone = "978-551-0040"
        address.BillingCountry = (Model.Address.BillingCountryEnum.USA)
        verificationRequest.Address = address

        demandDepositAccount = Model.DemandDepositAccount();
        
        demandDepositAccount.DDAAccountType = "Checking"
        demandDepositAccount.AccountNumber = "234"
        demandDepositAccount.RoutingNumber = "123234345"
        demandDepositAccount.CheckNumber = "456"
        demandDepositAccount.CCDPaymentInformation = "567"
        verificationRequest.DemandDepositAccount = demandDepositAccount

        reports = Model.Reports();
        
        reports.ReportGroup = "1243"
        verificationRequest.Reports = reports

        application = Model.Application();
        
        application.ApplicationID = "1234"
        verificationRequest.Application = application

        return verificationRequest

def sampleCheckVoid(transactionID) :
        voidRequest = Check.Void()

        credentials = Model.Credentials();
        
        credentials.AcceptorID = "1147003"
        voidRequest.Credentials = credentials

        transaction = Model.Transaction();
        
        transaction.TransactionID = transactionID
        voidRequest.Transaction = transaction

        reports = Model.Reports();
        
        reports.ReportGroup = "1243"
        voidRequest.Reports = reports

        application = Model.Application();
        
        application.ApplicationID = "1234"
        voidRequest.Application = application

        return voidRequest


def sampleServicesCreatePlan() :
        createPlanRequest = Services.CreatePlan()

        credentials = Model.Credentials();
        
        credentials.AcceptorID = "1147003"
        createPlanRequest.Credentials = credentials

        scheduledTask = Model.ScheduledTask();
        
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

def sampleServicesFraudCheck() :
        fraudCheckRequest = Services.FraudCheck()

        credentials = Model.Credentials();
        
        credentials.AcceptorID = "1147003"
        fraudCheckRequest.Credentials = credentials

        reports = Model.Reports();
        
        reports.ReportGroup = "1243"
        fraudCheckRequest.Reports = reports

        advancedFraudChecks = Model.AdvancedFraudChecks();
        
        advancedFraudChecks.ThreatMetrixSessionID = "123"
        fraudCheckRequest.AdvancedFraudChecks = advancedFraudChecks

        application = Model.Application();
        
        application.ApplicationID = "1234"
        fraudCheckRequest.Application = application

        return fraudCheckRequest

def sampleServicesPaymentAccountCreate() :
        paymentAccountCreateRequest = Services.PaymentAccountCreate()

        credentials = Model.Credentials();
        
        credentials.AcceptorID = "1147003"
        paymentAccountCreateRequest.Credentials = credentials

        reports = Model.Reports();
        
        reports.ReportGroup = "1243"
        paymentAccountCreateRequest.Reports = reports

        card = Model.Card();
        
        card.AccountNumber = "5454545454545454"
        paymentAccountCreateRequest.Card = card

        application = Model.Application();
        
        application.ApplicationID = "1234"
        paymentAccountCreateRequest.Application = application

        return paymentAccountCreateRequest

def sampleServicesScheduledTaskDelete() :
        scheduledTaskDeleteRequest = Services.ScheduledTaskDelete()

        credentials = Model.Credentials();
        
        credentials.AcceptorID = "1147003"
        scheduledTaskDeleteRequest.Credentials = credentials

        scheduledTask = Model.ScheduledTask();
        
        scheduledTask.SubscriptionID = "12432463563564"
        scheduledTaskDeleteRequest.ScheduledTask = scheduledTask

        return scheduledTaskDeleteRequest

def sampleServicesScheduledTaskUpdate() :
        scheduledTaskUpdateRequest = Services.ScheduledTaskUpdate()

        credentials = Model.Credentials();
        
        credentials.AcceptorID = "1147003"
        scheduledTaskUpdateRequest.Credentials = credentials

        scheduledTask = Model.ScheduledTask();
        
        scheduledTask.SubscriptionID = "12432463563564"
        scheduledTask.BillingDate = "2019-10-21"
        scheduledTaskUpdateRequest.ScheduledTask = scheduledTask

        return scheduledTaskUpdateRequest

def sampleServicesPaymentAccountUpdate() :
        paymentAccountUpdateRequest = Services.PaymentAccountUpdate()

        credentials = Model.Credentials();
        
        credentials.AcceptorID = "1147003"
        paymentAccountUpdateRequest.Credentials = credentials

        reports = Model.Reports();
        
        reports.ReportGroup = "1243"
        paymentAccountUpdateRequest.Reports = reports

        card = Model.Card();
        
        card.CVV = "123"
        paymentAccountUpdateRequest.Card = card

        application = Model.Application();
        
        application.ApplicationID = "1234"
        paymentAccountUpdateRequest.Application = application

        paymentAccount = Model.PaymentAccount();
        
        paymentAccount.PaymentAccountID = "1112000188575454"
        paymentAccountUpdateRequest.PaymentAccount = paymentAccount

        return paymentAccountUpdateRequest

def sampleServicesUpdatePlan() :
        updatePlanRequest = Services.UpdatePlan()

        credentials = Model.Credentials();
        
        credentials.AcceptorID = "1147003"
        updatePlanRequest.Credentials = credentials

        scheduledTask = Model.ScheduledTask();
        
        scheduledTask.Active = "false"
        scheduledTask.ScheduledTaskID = "12"
        updatePlanRequest.ScheduledTask = scheduledTask

        return updatePlanRequest