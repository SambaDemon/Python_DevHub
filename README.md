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


##The MIT License (MIT)

####Copyright (c) 2016 Aleksander Sukharev, https://github.com/SambaDemon, alexander.sukharev1@gmail.com

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
