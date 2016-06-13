# Python_DevHub

It is the fork of original samples, reworked into SDK format. Using Marshmallow and urllib with adaptation to Python 3.5.

Original doucmentation and etc:

* Documentation: https://apideveloper.vantiv.com/docs/devhub-developer
* Forum: https://apideveloper.vantiv.com/forum
* FAQ: https://apideveloper.vantiv.com/faqs

##Overview

This repository provide simple SDK to sending transactions to Vantiv DevHub.


##Prerequisites

* DevHub Account (https://apideveloper.vantiv.com)
* License from DevHub Account
* AcceptorID (merchantid)

## All steps and information about setup accounts and requests headers you can find in official documentations.


##Folder Contents
```
> vantiv
        > Test.py : Used as a starting point to try out the API using the Sample Code.
        > request (folder)
               > config.py: Used to set the base endpoint URL, license, and optional proxy settings should your company have a proxy.
               > request.py: Contains examples of sending a tranaction, serializing an object to JSON, and getting the Json String response.
               > sample_requests.py: The following data generator examples provide test values that can be set per each transaction type.
               > utilities.py: Useful example of code like extracting values from a string response.
               > Boarding (folder): Transaction types definitions commonly used by payment facilitator partners.
               > Check (folder): Transaction type definitions
               > Credit (folder): Transaction type definitions
               > Model (folder): Data definition of the API.
               > Services (folder): Transaction type definitions for items used across Check and Credit.
```


####Copyright (c) 2016 Vantiv, Inc. - All Rights Reserved.

Sample Code is for reference only and is solely intended to be used for educational purposes and is provided ?AS IS? and ?AS AVAILABLE? and without warranty. It is the responsibility of the developer to  develop and write its own code before successfully certifying their solution.

This sample may not, in whole or in part, be copied, photocopied, reproduced, translated, or reduced to any electronic medium or machine-readable form without prior consent, in writing, from Vantiv, Inc.

Use, duplication or disclosure by the U.S. Government is subject to restrictions set forth in an executed license agreement and in subparagraph (c)(1) of the Commercial Computer Software-Restricted Rights Clause at FAR 52.227-19; subparagraph (c)(1)(ii) of the Rights in Technical Data and Computer Software clause at DFARS 252.227-7013, subparagraph (d) of the Commercial Computer Software--Licensing clause at NASA FAR supplement 16-52.227-86; or their equivalent.

Information in this sample code is subject to change without notice and does not represent a commitment on the part of Vantiv, Inc.  In addition to the foregoing, the Sample Code is subject to the terms and conditions set forth in the Vantiv Terms and Conditions of Use (http://www.apideveloper.vantiv.com) and the Vantiv Privacy Notice (http://www.vantiv.com/Privacy-Notice).
