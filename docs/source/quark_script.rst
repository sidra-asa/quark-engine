++++++++++++++++++++++++++++++++++++++++++++++++++
Quark Script
++++++++++++++++++++++++++++++++++++++++++++++++++

Ecosystem for Mobile Security Tools
------------------------------------

Innovative & Interactive
=========================

The goal of Quark Script aims to provide an innovative way for mobile security researchers to analyze or **pentest**  the targets.

Based on Quark, we integrate decent tools as Quark Script APIs and make them exchange valuable intelligence to each other. This enables security researchers to **interact**  with staged results and perform **creative**  analysis with Quark Script.

Dynamic & Static Analysis
==========================

In Quark script, we integrate not only static analysis tools (e.g. Quark itself) but also dynamic analysis tools (e.g. `objection <https://github.com/sensepost/objection>`_).  

Re-Usable & Sharable
====================

Once the user creates a Quark script for specific analysis scenario. The script can be used in another targets. Also, the script can be shared to other security researchers. This enables the exchange of knowledges. 

More APIs to come
==================
Quark Script is now in a beta version. We'll keep releasing practical APIs and analysis scenarios.  


Quickstart 
-----------

| In this tutorial, we will learn how to install and run Quark Script with a very easy example.
| We show how to detect CWE-798 in ovaa.apk.

Step 1: Environments Requirements
==================================
- Quark Script requires Python 3.8 or above.

Step 2: Install Quark Engine
=============================

You can install Quark Engine by running:

::

    $ pip3 install quark-engine


Step 3: Prepare Quark Script, Detection Rule and the Sample File
================================================================

1. Get the CWE-798 Quark Script and the detection rule `here <https://quark-engine.readthedocs.io/en/latest/quark_script.html#detect-cwe-798-in-android-application-ovaa-apk>`_.
2. Get the sampe file (ovaa.apk) `here <https://github.com/dark-warlord14/ovaa/releases/tag/1.0>`_.
3. Put the script, detection rule, and sample file in the same directory.
4. Edit accordingly to the file names:

.. code-block:: python

    SAMPLE_PATH = "ovaa.apk"
    RULE_PATH = "findSecretKeySpec.json"


Now you are ready to run the script!

Step 4: Run the script
======================

::

    $ python3 CWE-798.py


You should now see the detection result in the terminal.

::

    Found hard-coded AES key 49u5gh249gh24985ghf429gh4ch8f23f


Introduce of Quark Script APIs
------------------------------

findMethodInAPK(samplePath, targetMethod)
=========================================

- **Description**: Find the target method in APK
- **params**: 
    1. samplePath: Target file
    2. targetMethod: A python list contains class name, method name, and descriptor of target method
- **return**: Python list contains caller method instance of target method

Rule(rule.json)
===============

- **Description**: Making detection rule a rule instance
- **params**: Path of a single Quark rule
- **return**: Quark rule instance

runQuarkAnalysis(SAMPLE_PATH, ruleInstance)
===========================================

- **Description**: Given detection rule and target sample, this instance runs the basic Quark analysis.
- **params**: 
    1. SAMPLE_PATH: Target file 
    2. ruleInstance: Quark rule object
- **return**: quarkResult instance

quarkResultInstance.behaviorOccurList
=====================================

- **Description**: List that stores instances of detected behavior in different part of the target file.
- **params**: none
- **return**: detected behavior instance

quarkResultInstance.getAllStrings(none)
=======================================

- **Description**: Get all strings inside the target APK file.
- **params**: none
- **return**: python list containing all strings inside the target APK file.

quarkResultInstance.isHardcoded(argument)
==========================================

- **Description**: Check if the argument is hardcoded into the APK.
- **params**: 
    1. argument: string value that is passed in when a method is invoked
- **return**: True/False

quarkResultInstance.findMethodInCaller(callerMethod, targetMethod)
==================================================================
- **Description**: Find target method in caller method.
- **params**: 
    1. callerMethod: python list contains class name, method name and descriptor of caller method.
    2. targetMethod: python list contains class name, method name and descriptor of target method.
- **return**: python list contains target method instances.

behaviorInstance.firstAPI.fullName
==================================

- **Description**: Show the name of the first key API called in this behavior.
- **params**: none
- **return**: API name

behaviorInstance.secondAPI.fullName
===================================

- **Description**: Show the name of the second key API called in this behavior.
- **params**: none
- **return**: API name

behaviorInstance.hasString(pattern, isRegex)
============================================

- **Description**: Check if the arguments of the two APIs contain the string.
- **params**: 
    1. pattern: string that may appear in the arguments
    2. isRegex: consider the string as a regular expression if True, defaults to False
- **return**: the matched string

behaviorInstance.hasUrl(none)
=============================

-  **Description**: Check if the behavior contains urls.
-  **params**: none
-  **return**: python list containing all detected urls.

behaviorInstance.methodCaller
=============================

- **Description**: Find method who calls this behavior (API1 & API2).
- **params**: none
- **return**: method instance 

behaviorInstance.getParamValues(none)
=====================================

- **Description**: Get parameter values that API1 sends to API2 in the behavior.
- **params**: none
- **return**: python list containing parameter values.

behaviorInstance.isArgFromMethod(targetMethod)
==============================================

- **Description**: Check if there are any arguments from the target method.
- **params**: 
    1. targetMethod: python list contains class name, method name, and descriptor of target method
- **return**: True/False

behaviorInstance.getMethodsInArgs(none)
==============================================

- **Description**: Get the methods which the arguments in API2 has passed through.
- **params**: none
- **return**: python list containing method instances

methodInstance.getXrefFrom(none)
================================

- **Description**: Find out who call this method.
- **params**: none
- **return**: python list containing caller methods.

methodInstance.getXrefTo(none)
==============================

- **Description**: Find out who this method called.
- **params**: none
- **return**: python list containing tuples (callee methods, index).

methodInstance.getArguments(none)
==============================

- **Description**: Get arguments from method.
- **params**: none
- **return**: python list containing arguments.
  
methodInstance.findSuperclassHierarchy(none)
=============================================

- **Description**: Find all superclasses of this method object.
- **params**: none
- **return**: Python list contains all superclass names of this method. 

Objection(host)
===============

- **Description**: Create an instance for Objection (dynamic analysis tool). 
- **params**: Monitoring IP:port
- **return**: objection instance

objInstance.hookMethod(method, watchArgs, watchBacktrace, watchRet)
=====================================================================

- **Description**: Hook the target method with Objection.
- **params**: 
    1. method: the tagrget API. (type: str or method instance) 
    2. watchArgs: Return Args information if True. (type: boolean) 
    3. watchBacktrace: Return backtrace information if True. (type: boolean) 
    4. watchRet: Return the return information of the target API if True. (type: boolean)
- **return**: none

runFridaHook(apkPackageName, targetMethod, methodParamTypes, secondToWait)
============================================================================

- **Description**: Track calls to the specified method for given seconds.
- **params**:
    1. apkPackageName: the package name of the target APP
    2. targetMethod: the target API
    3. methodParamTypes: string that holds the parameters used by the target API
    4. secondToWait: seconds to wait for method calls, defaults to 10
- **return**: FridaResult instance

checkClearText(inputString)
============================

- **Description**: Check the decrypted value of the input string.
- **params**:
    1. inputString: string to be checked
- **return**: the decrypted value

getActivities(samplePath)
==========================
- **Description**: Get activities from the manifest of target sample.
- **params**: 
    1. samplePath: the file path of target sample
- **return**: python list containing activities

activityInstance.hasIntentFilter(none)
======================================
- **Description**: Check if the activity has an intent-filter.
- **params**: none
- **return**: True/False

activityInstance.isExported(none)
==================================
- **Description**: Check if the activity set ``android:exported=true``.
- **params**: none
- **return**: True/False

getReceivers(samplePath)
==========================
- **Description**: Get receivers from a target sample.
- **params**:
    1. samplePath: target sample
- **return**: python list containing receivers

receiverInstance.hasIntentFilter(none)
======================================
- **Description**: Check if the receiver has an intent-filter.
- **params**: none
- **return**: True/False

receiverInstance.isExported(none)
==================================
- **Description**: Check if the receiver is exported.
- **params**: none
- **return**: True/False

getApplication(samplePath)
==========================
- **Description**: Get the application element from the manifest file of the target sample.
- **params**: 
    1. samplePath: the file path of the target sample
- **return**: the application element of the target sample

applicationInstance.isDebuggable(none)
======================================
- **Description**: Check if the application element sets ``android:debuggable=true``.
- **params**: none
- **return**:  True/False

Analyzing real case (InstaStealer) using Quark Script
------------------------------------------------------

Quark Script that dynamic hooks the method containing urls 
===========================================================

The scenario is simple! We'd like to dynamic hooking the methods in the malware that contains urls. We can use APIs above to write Quark Script.

.. code-block:: python

    from quark.script import runQuarkAnalysis, Rule
    from quark.script.objection import Objection

    SAMPLE_PATH = "6f032.apk"
    RULE_PATH = "00211.json"

    ruleInstance = Rule(RULE_PATH)
    quarkResult = runQuarkAnalysis(SAMPLE_PATH, ruleInstance)

    for behaviorInstance in quarkResult.behaviorOccurList:
        detectedUrl = behaviorInstance.hasUrl()
        
        if detectedUrl:
            print(f"\nDetected Behavior -> {ruleInstance.crime}")
            print(f"\nDetected Url -> {detectedUrl}")
            
            method = behaviorInstance.methodCaller
            print(f"\nThe detected behavior was called by -> {method.fullName}")

            print("\nAttempt to hook the method:")
            obj = Objection("127.0.0.1:8888")
            
            obj.hookMethod(method, 
                        watchArgs=True, 
                        watchBacktrace=True, 
                        watchRet=True)
            print(f"\tHook -> {method.fullName}")
            
            for methodCaller in method.getXrefFrom():
                obj.hookMethod(methodCaller, 
                            watchArgs=True, 
                            watchBacktrace=True, 
                            watchRet=True)
                print(f"\tHook -> {methodCaller.fullName}")
                
            for methodCallee, _ in method.getXrefTo():
                obj.hookMethod(methodCallee, 
                            watchArgs=True, 
                            watchBacktrace=True, 
                            watchRet=True)
                print(f"\tHook -> {methodCallee.fullName}")
                
    print("\nSee the hook results in Objection's terminal.")

.. note::
    Please make sure you have the dynamic analysis environment ready before executing the script.

    1. Objection installed and running. Check the guideline `here <https://github.com/sensepost/objection/wiki/Installation>`_.
    2. Android Virtual Machine with frida installed. Check the guideline `here <https://frida.re/docs/android/>`_.
    3. Or a rooted Android Device (Google Pixel 6) with frida installed. Check the root guideline `here <https://forum.xda-developers.com/t/guide-root-pixel-6-with-magisk-android-12-1.4388733/>`_, frida install guideline is the `same <https://frida.re/docs/android/>`_ with Android Virtual Machine.

Quark Script Result
===================

.. image:: https://i.imgur.com/elztZdC.png

Logs on the Objection terminal (hooking)
========================================

.. image:: https://i.imgur.com/XrtfgjY.jpg

Method (callComponentMethod) with urls is detected triggered!
=============================================================

.. image:: https://i.imgur.com/ryV3f57.jpg


Detect CWE-798 in Android Application (ovaa.apk)
------------------------------------------------

This scenario seeks to find hard-coded credentials in the APK file. See `CWE-798 <https://cwe.mitre.org/data/definitions/798.html>`_ for more details.

Let's use this `APK <https://github.com/oversecured/ovaa>`_ and the above APIs to show how Quark script find this vulnerability.

First, we design a detection rule ``findSecretKeySpec.json`` to spot on behavior uses method SecretKeySpec. Then, we get all the parameter values that input to this method. From the returned parameter values, we identify it's a AES key and parse the key out of the values. Finally, we dump all strings in the APK file and check if the AES key is in the strings. If the answer is YES, BINGO!!! We find hard-coded credentials in the APK file. 

Quark Scipt: CWE-798.py
========================

.. code-block:: python

    import re
    from quark.script import runQuarkAnalysis, Rule

    SAMPLE_PATH = "ovaa.apk"
    RULE_PATH = "findSecretKeySpec.json"

    ruleInstance = Rule(RULE_PATH)
    quarkResult = runQuarkAnalysis(SAMPLE_PATH, ruleInstance)

    for secretKeySpec in quarkResult.behaviorOccurList:
        
        allStrings = quarkResult.getAllStrings()
        
        firstParam = secretKeySpec.getParamValues()[1]
        secondParam = secretKeySpec.getParamValues()[2]
        
        if secondParam == "AES":
            AESKey = re.findall(r'\((.*?)\)', firstParam)[1]
            
        if AESKey in allStrings:
            print(f"Found hard-coded {secondParam} key {AESKey}")


Quark Rule: findSecretKeySpec.json
==================================

.. code-block:: json

    {
        "crime": "Detect APK using SecretKeySpec.",
        "permission": [],
        "api": [
            {
                "descriptor": "()[B",
                "class": "Ljava/lang/String;",
                "method": "getBytes"
            },
            {
                "descriptor": "([BLjava/lang/String;)V",
                "class": "Ljavax/crypto/spec/SecretKeySpec;",
                "method": "<init>"
            }
        ],
        "score": 1,
        "label": []
    }


Quark Script Result
=====================

.. code-block:: TEXT

    $ python3 findSecretKeySpec.py 

    Found hard-coded AES key 49u5gh249gh24985ghf429gh4ch8f23f


Hard-Coded AES key in the APK file
===================================

.. code-block:: TEXT

    const-string v2, "49u5gh249gh24985ghf429gh4ch8f23f"

    invoke-virtual {v2}, Ljava/lang/String;->getBytes()[B

    move-result-object v2

    invoke-direct {v1, v2, v0}, Ljavax/crypto/spec/SecretKeySpec;-><init>([BLjava/lang/String;)V


Detect CWE-94 in Android Application (ovaa.apk)
-----------------------------------------------

This scenario seeks to find code injection in the APK file. See `CWE-94 <https://cwe.mitre.org/data/definitions/94.html>`_ for more details.

Let's use this `APK <https://github.com/oversecured/ovaa>`_ and the above APIs to show how Quark script find this vulnerability.

First, we design a detection rule ``loadExternalCode.json`` to spot on behavior uses method createPackageContext. Then, we find the caller method who calls the createPackageContext. Finally, we check if  method checkSignatures is called in the caller method for verification.


Quark Scipt: CWE-94.py
========================

.. code-block:: python

    from quark.script import runQuarkAnalysis, Rule
                                                                                                        
    SAMPLE_PATH = "ovaa.apk"
    RULE_PATH = "loadExternalCode.json"
                                                                                                        
    targetMethod = [
            "Landroid/content/pm/PackageManager;",
            "checkSignatures",
            "(Ljava/lang/String;Ljava/lang/String;)I"
            ]
                                                                                                        
    ruleInstance = Rule(RULE_PATH)
    quarkResult = runQuarkAnalysis(SAMPLE_PATH, ruleInstance)
                                                                                                        
    for ldExternalCode in quarkResult.behaviorOccurList:
                                                            
        callerMethod = [
                ldExternalCode.methodCaller.className,
                ldExternalCode.methodCaller.methodName,
                ldExternalCode.methodCaller.descriptor
                ]
                                                                                                        
        if not quarkResult.findMethodInCaller(callerMethod, targetMethod):
            print(f"\nMethod: {targetMethod[1]} not found!")
            print(f"CWE-94 is detected in {SAMPLE_PATH}")

Quark Rule: loadExternalCode.json
==================================

.. code-block:: json
        
    {
        "crime": "Load external code from other APK.",
        "permission": [],
        "api": [
            {
                "descriptor": "(Ljava/lang/String;I)Landroid/content/Context;",
                "class": "",
                "method": "createPackageContext"
            },
            {
                "descriptor": "(Ljava/lang/String;)Ljava/lang/Class;",
                "class": "Ljava/lang/ClassLoader;",
                "method": "loadClass"
            }
        ],
        "score": 1,
        "label": []
    }


Quark Script Result
===================

.. code-block:: TEXT

    $ python3 CWE-94.py

    Method: checkSignatures not found!
    CWE-94 is detected in ovaa.apk


Detect CWE-921 in Android Application (ovaa.apk)
------------------------------------------------

This scenario seeks to find unsecure storage mechanism of data in the APK file. See `CWE-921 <https://cwe.mitre.org/data/definitions/921.html>`_ for more details.

Let's use this `APK <https://github.com/oversecured/ovaa>`_ and the above APIs to show how Quark script find this vulnerability.

First, we design a detection rule ``checkFileExistence.json`` to spot on behavior that checks if a file exist on given storage mechanism. Then, we use API ``getParamValues()`` to get the file path. Finally, CWE-921 is found if the file path contains keyword ``sdcard``.

Quark Script CWE-921.py
========================

.. code-block:: python

    from quark.script import runQuarkAnalysis, Rule

    SAMPLE_PATH = "ovaa.apk"
    RULE_PATH = "checkFileExistence.json"

    ruleInstance = Rule(RULE_PATH)
    quarkResult = runQuarkAnalysis(SAMPLE_PATH, ruleInstance)

    for existingFile in quarkResult.behaviorOccurList:
        filePath = existingFile.getParamValues()[0]
        if "sdcard" in filePath:
            print(f"This file is stored inside the SDcard\n")
            print(f"CWE-921 is detected in {SAMPLE_PATH}.")

Quark Rule: checkFileExistence.json
===================================

.. code-block:: json

    {
        "crime": "Check file existence",
        "permission": [],
        "api": [
            {
                "descriptor": "(Ljava/lang/String;)V",
                "class": "Ljava/io/File;",
                "method": "<init>"
            },
            {
                "descriptor": "()Z",
                "class": "Ljava/io/File;",
                "method": "exists"
            }
        ],
        "score": 1,
        "label": []
    }

Quark Script Result
====================

.. code-block:: TEXT

    $ python3 CWE-921.py 
    This file is stored inside the SDcard

    CWE-921 is detected in ovaa.apk.


Detect CWE-312 in Android Application (ovaa.apk)
------------------------------------------------

This scenario seeks to find cleartext storage of sensitive data in the APK file. See `CWE-312 <https://cwe.mitre.org/data/definitions/312.html>`_ for more details.

Let's use this `APK <https://github.com/oversecured/ovaa>`_ and the above APIs to show how Quark script find this vulnerability.

First, we designed a `Frida <https://frida.re>`_ script ``agent.js`` to hook the target method and get the arguments when the target method is called. Then we hook the method ``putString`` to catch its arguments. Finally, we use `Ciphey <https://github.com/Ciphey/Ciphey>`_ to check if the arguments are encrypted.

Quark Script CWE-312.py
========================

.. code-block:: python

    from quark.script.frida import runFridaHook
    from quark.script.ciphey import checkClearText

    APP_PACKAGE_NAME = "oversecured.ovaa"

    TARGET_METHOD = "android.app." \
                    "SharedPreferencesImpl$EditorImpl." \
                    "putString"

    METHOD_PARAM_TYPE = "java.lang.String," \
                        "java.lang.String"

    fridaResult = runFridaHook(APP_PACKAGE_NAME,
                                TARGET_METHOD,
                                METHOD_PARAM_TYPE,
                            secondToWait = 10)

    for putString in fridaResult.behaviorOccurList:

        firstParam, secondParam = putString.getParamValues()

        if firstParam in ["email", "password"] and \
            secondParam == checkClearText(secondParam):
            
            print(f'The CWE-312 vulnerability is found. The cleartext is "{secondParam}"')

Frida Script: agent.js
=======================

.. code-block:: javascript

    // -*- coding: utf-8 -*-
    // This file is part of Quark-Engine - https://github.com/quark-engine/quark-engine
    // See the file 'LICENSE' for copying permission.

    /*global Java, send, rpc*/
    function replaceMethodImplementation(targetMethod, classAndMethodName, methodParamTypes, returnType) {
        targetMethod.implementation = function () {
            let callEvent = {
                "type": "CallCaptured",
                "identifier": [classAndMethodName, methodParamTypes, returnType],
                "paramValues": []
            };

            for (const arg of arguments) {
                callEvent["paramValues"].push((arg || "(none)").toString());
            }

            send(JSON.stringify(callEvent));
            return targetMethod.apply(this, arguments);
        };
    }

    function watchMethodCall(classAndMethodName, methodParamTypes) {
        if (classAndMethodName == null || methodParamTypes == null) {
            return;
        }

        const indexOfLastSeparator = classAndMethodName.lastIndexOf(".");
        const classNamePattern = classAndMethodName.substring(0, indexOfLastSeparator);
        const methodNamePattern = classAndMethodName.substring(indexOfLastSeparator + 1);

        Java.perform(() => {
            const classOfTargetMethod = Java.use(classNamePattern);
            const possibleMethods = classOfTargetMethod[`${methodNamePattern}`];

            if (typeof possibleMethods === "undefined") {
                const failedToWatchEvent = {
                    "type": "FailedToWatch",
                    "identifier": [classAndMethodName, methodParamTypes]
                };

                send(JSON.stringify(failedToWatchEvent));
                return;
            }

            possibleMethods.overloads.filter((possibleMethod) => {
                const paramTypesOfPossibleMethod = possibleMethod.argumentTypes.map((argument) => argument.className);
                return paramTypesOfPossibleMethod.join(",") === methodParamTypes;
            }).forEach((matchedMethod) => {
                const retType = matchedMethod.returnType.name;
                replaceMethodImplementation(matchedMethod, classAndMethodName, methodParamTypes, retType);
            }
            );

        });
    }

    rpc.exports["watchMethodCall"] = (classAndMethodName, methodParamTypes) => watchMethodCall(classAndMethodName, methodParamTypes);

Quark Script Result
====================

.. code-block:: TEXT

    $ python3 CWE-312.py
    The CWE-312 vulnerability is found. The cleartext is "test@email.com"
    The CWE-312 vulnerability is found. The cleartext is "password"

Detect CWE-89 in Android Application (AndroGoat.apk)
----------------------------------------------------

This scenario seeks to find SQL injection in the APK file. See `CWE-89 <https://cwe.mitre.org/data/definitions/89.html>`_ for more details.

Let's use this `APK <https://github.com/satishpatnayak/AndroGoat>`_ and the above APIs to show how Quark script find this vulnerability.

First, we design a detection rule ``executeSQLCommand.json`` to spot on behavior using SQL command Execution. Then, we use API ``isArgFromMethod`` to check if ``append`` use the value of ``getText`` as the argument. If yes, we confirmed that the SQL command string is built from user input, which will cause CWE-89 vulnerability.

Quark Script CWE-89.py
======================

.. code-block:: python

    from quark.script import runQuarkAnalysis, Rule

    SAMPLE_PATH = "AndroGoat.apk"
    RULE_PATH = "executeSQLCommand.json"

    targetMethod = [
        "Landroid/widget/EditText;", # class name 
        "getText",                   # method name
        "()Landroid/text/Editable;", # descriptor
    ]

    ruleInstance = Rule(RULE_PATH)
    quarkResult = runQuarkAnalysis(SAMPLE_PATH, ruleInstance)

    for sqlCommandExecution in quarkResult.behaviorOccurList:
        if sqlCommandExecution.isArgFromMethod(
            targetMethod
        ):
            print(f"CWE-89 is detected in {SAMPLE_PATH}")

Quark Rule: executeSQLCommand.json
==================================

.. code-block:: json

    {
        "crime": "Execute SQL Command",
        "permission": [],
        "api": [
            {
                "class": "Ljava/lang/StringBuilder;",
                "method": "append",
                "descriptor": "(Ljava/lang/String;)Ljava/lang/StringBuilder;"
            },
            {
                "class": "Landroid/database/sqlite/SQLiteDatabase;",
                "method": "rawQuery",
                "descriptor": "(Ljava/lang/String; [Ljava/lang/String;)Landroid/database/Cursor;"
            }
        ],
        "score": 1,
        "label": []
    }

Quark Script Result
====================

.. code-block:: TEXT

    $ python3 CWE-89.py

    CWE-89 is detected in AndroGoat.apk


Detect CWE-926 in Android Application (dvba.apk)
----------------------------------------------------

This scenario seeks to find **improper export of Android application components** in the APK file. See `CWE-926 <https://cwe.mitre.org/data/definitions/926.html>`_ for more details.

Let's use this `APK <https://github.com/rewanthtammana/Damn-Vulnerable-Bank>`_ and the above APIs to show how Quark script find this vulnerability.

First, we use Quark API ``getActivities`` to get all activity data in the manifest. Then we use ``activityInstance.hasIntentFilter`` to check if the activities have ``intent-filter``. Also, we use ``activityInstance.isExported`` to check if the activities set the attribute ``android:exported=true``. If both are **true**, then the APK exports the component for use by other applications. That may cause CWE-926 vulnerabilities.

Quark Script CWE-926.py
=======================

.. code-block:: python

    from quark.script import *

    SAMPLE_PATH = "dvba.apk"

    for activityInstance in getActivities(SAMPLE_PATH):
        
        if activityInstance.hasIntentFilter() and activityInstance.isExported():
            print(f"CWE-926 is detected in the activity, {activityInstance}")

Quark Script Result
====================

.. code-block:: TEXT

    $ python3 CWE-926.py

    CWE-926 is found in the activity, com.app.damnvulnerablebank.CurrencyRates
    CWE-926 is found in the activity, com.app.damnvulnerablebank.SplashScreen

Detect CWE-749 in Android Application (MSTG-Android-Java.apk)
-------------------------------------------------------------

This scenario seeks to find **exposed methods or functions** in the APK file. See `CWE-749 <https://cwe.mitre.org/data/definitions/749.html>`_ for more details.

Let's use this `APK <https://github.com/OWASP/MASTG-Hacking-Playground>`_ and the above APIs to show how Quark script find this vulnerability.

First, we design a detection rule ``configureJsExecution.json`` to spot on behavior using method ``setJavascriptEnabled``. Then, we use API ``methodInstance.getArguments`` to check if it enables JavaScript execution on websites. Finally, we look for calls to method ``addJavaScriptInterface`` in the caller method. If **yes**, the APK exposes methods or functions to websites. That causes CWE-749 vulnerability.

Quark Script CWE-749.py
=======================

.. code-block:: python

    from quark.script import runQuarkAnalysis, Rule

    SAMPLE_PATH = "MSTG-Android-Java.apk"
    RULE_PATH = "configureJsExecution.json"

    targetMethod = [
        "Landroid/webkit/WebView;",
        "addJavascriptInterface",
        "(Ljava/lang/Object; Ljava/lang/String;)V"
    ]

    ruleInstance = Rule(RULE_PATH)
    quarkResult = runQuarkAnalysis(SAMPLE_PATH, ruleInstance)

    for configureJsExecution in quarkResult.behaviorOccurList:

        caller = configureJsExecution.methodCaller
        secondAPI = configureJsExecution.secondAPI

        enableJS = secondAPI.getArguments()[1]
        exposeAPI = quarkResult.findMethodInCaller(caller, targetMethod)

        if enableJS and exposeAPI:
            print(f"CWE-749 is detected in method, {caller.fullName}"

Quark Rule: configureJsExecution.json
=====================================

.. code-block:: json

    {
        "crime": "Configure JavaScript execution on websites",
        "permission": [],
        "api": [
            {
                "class": "Landroid/webkit/WebView;",
                "method": "getSettings",
                "descriptor": "()Landroid/webkit/WebSettings;"
            },
            {
                "class": "Landroid/webkit/WebSettings;",
                "method": "setJavaScriptEnabled",
                "descriptor": "(Z)V"
            }
        ],
        "score": 1,
        "label": []
    }

Quark Script Result
====================

.. code-block:: TEXT

    $ python3 CWE-749.py

    CWE-749 is detected in method, Lsg/vp/owasp_mobile/OMTG_Android/OMTG_ENV_005_WebView_Remote; onCreate (Landroid/os/Bundle;)V
    CWE-749 is detected in method, Lsg/vp/owasp_mobile/OMTG_Android/OMTG_ENV_005_WebView_Local; onCreate (Landroid/os/Bundle;)V


Detect CWE-532 in Android Application (dvba.apk)
-------------------------------------------------------------

This scenario seeks to find **insertion of sensitive information into Log file**. See `CWE-532 <https://cwe.mitre.org/data/definitions/532.html>`_ for more details.

Let’s use this `APK <https://github.com/rewanthtammana/Damn-Vulnerable-Bank>`_ and the above APIs to show how the Quark script finds this vulnerability.

First, we use API ``findMethodInAPK`` to locate ``log.d`` method. Then we use API ``methodInstance.getArguments`` to get the argument that input to ``log.d``. Finally, we use some keywords such as "token", "password", and "decrypt" to check if arguments include sensitive data. If the answer is YES, that may cause sensitive data leakage into log file.

You can use your own keywords in the keywords list to detect sensitive data.

Quark Script CWE-532.py
=======================

.. code-block:: python

    from quark.script import findMethodInAPK

    SAMPLE_PATH = "dvba.apk"
    TARGET_METHOD = [
        "Landroid/util/Log;",                       # class name
        "d",                                        # method name
        "(Ljava/lang/String; Ljava/lang/String;)I"  # descriptor
    ]
    CREDENTIAL_KEYWORDS = [
        "token",
        "decrypt",
        "password"
    ]

    methodsFound = findMethodInAPK(SAMPLE_PATH, TARGET_METHOD)

    for debugLogger in methodsFound:
        arguments = debugLogger.getArguments()

        for keyword in CREDENTIAL_KEYWORDS:
            if keyword in arguments[1]:
                print(f"CWE-532 is detected in method, {debugLogger.fullName}") 


Quark Script Result
====================

.. code-block:: TEXT

    $ python CWE-532.py 
    CWE-532 is detected in method, Lcom/google/firebase/auth/FirebaseAuth; d (Lc/c/b/h/o;)V


Detect CWE-780 in Android Application (MSTG-Android-Java.apk)
-------------------------------------------------------------

This scenario seeks to find **the use of the RSA algorithm without Optimal Asymmetric Encryption Padding (OAEP)**. See `CWE-780 <https://cwe.mitre.org/data/definitions/780.html>`_ for more details.

Let's use this `APK <https://github.com/OWASP/MASTG-Hacking-Playground>`_ and the above APIs to show how the Quark script find this vulnerability.

We first design a detection rule ``useOfCryptographicAlgo.json`` to spot on behavior using the cryptographic algorithm. Then, we use API `behaviorInstance.hasString(pattern, isRegex)` to filter behaviors using the RSA algorithm. Finally, we use the same API to check if the algorithm runs without the OAEP scheme. If the answer is YES, the plaintext is predictable.

Quark Script CWE-780.py
=======================

.. code-block:: python

    from quark.script import Rule, runQuarkAnalysis

    SAMPLE_PATH = "MSTG-Android-Java.apk"
    RULE_PATH = "useOfCryptographicAlgo.json"

    ruleInstance = Rule(RULE_PATH)
    quarkResult = runQuarkAnalysis(SAMPLE_PATH, ruleInstance)

    for useCryptographicAlgo in quarkResult.behaviorOccurList:

        methodCaller = useCryptographicAlgo.methodCaller

        if useCryptographicAlgor.hasString("RSA") and \
            not useCryptographicAlgo.hasString("OAEP"):
            print(f"CWE-780 is detected in method, {methodCaller.fullName}")

Quark Rule: useOfCryptographicAlgo.json
=======================================

.. code-block:: json

    {
        "crime": "Use of cryptographic algorithm",
        "permission": [],
        "api": [
            {
                "class": "Ljavax/crypto/Cipher;",
                "method": "getInstance",
                "descriptor": "(Ljava/lang/String; Ljava/lang/String;)Ljavax/crypto/Cipher"
            },
            {
                "class": "Ljavax/crypto/Cipher;",
                "method": "init",
                "descriptor": "(I Ljava/security/Key;)V"
            }
        ],
        "score": 1,
        "label": []
    }

Quark Script Result
====================

.. code-block:: TEXT

    $ python3 CWE-780.py
    CWE-780 is detected in method, Lsg/vp/owasp_mobile/OMTG_Android/OMTG_DATAST_001_KeyStore; encryptString (Ljava/lang/String;)V

Detect CWE-319 in Android Application (ovaa.apk)
-------------------------------------------------------------

This scenario seeks to find **the Cleartext Transmission of Sensitive Information**. See `CWE-319 <https://cwe.mitre.org/data/definitions/319.html>`_ for more details.

Let's use this `APK <https://github.com/oversecured/ovaa>`_ and the above APIs to show how the Quark script finds this vulnerability. This sample uses the package Retrofit to request Web APIs, but the APIs use cleartext protocols. 

We first design a detection rule ``setRetrofitBaseUrl.json`` to spot on behavior that sets the base URL of the Retrofit instance. Then, we loop through a custom list of cleartext protocol schemes and use API `behaviorInstance.hasString` to filter arguments that are URL strings with cleartext protocol.

Quark Script CWE-319.py
=======================

.. code-block:: python 
    
    from quark.script import runQuarkAnalysis, Rule

    SAMPLE_PATH = "./ovaa.apk"
    RULE_PATH = "setRetrofitBaseUrl.json"

    PROTOCOL_KEYWORDS = [
        "http",
        "smtp",
        "ftp"
    ]


    ruleInstance = Rule(RULE_PATH)
    quarkResult = runQuarkAnalysis(SAMPLE_PATH, ruleInstance)

    for setRetrofitBaseUrl in quarkResult.behaviorOccurList: 
        for protocol in PROTOCOL_KEYWORDS:
        
            regexRule = f"{protocol}://[0-9A-Za-z./-]+"
            cleartextProtocolUrl = setRetrofitBaseUrl.hasString(regexRule, True)
        
            if cleartextProtocolUrl:
                print(f"CWE-319 detected!")
                print(f"Here are the found URLs with cleartext protocol:")
                print("\n".join(cleartextProtocolUrl))



Quark Rule: setRetrofitBaseUrl.json
=======================================

.. code-block:: json
    
    {
        "crime": "Set Retrofit Base Url",
        "permission": [],
        "api": 
        [
            {
                "descriptor": "()V",
                "class": "Lretrofit2/Retrofit$Builder;",
                "method": "<init>"
            },
            {
                "descriptor": "(Ljava/lang/String;)Lretrofit2/Retrofit$Builder;",
                "class": "Lretrofit2/Retrofit$Builder;",
                "method": "baseUrl"
            }
        ],
        "score": 1,
        "label": []
    }

Quark Script Result
====================

.. code-block:: TEXT
   
    $ python3 CWE-319.py
    CWE-319 detected!
    Here are the found URLs with cleartext protocol:
    http://example.com./api/v1/


Detect CWE-327 in Android Application (InjuredAndroid.apk)
-------------------------------------------------------------

This scenario seeks to find **the use of a Broken or Risky Cryptographic Algorithm**. See `CWE-327 <https://cwe.mitre.org/data/definitions/327.html>`_ for more details.

Let's use this `APK <https://github.com/B3nac/InjuredAndroid>`_ and the above APIs to show how the Quark script finds this vulnerability.

We first design a detection rule ``useOfCryptographicAlgo.json`` to spot on behavior using cryptographic algorithms. Then, we use API ``behaviorInstance.hasString(pattern, isRegex)`` with a list to check if the algorithm is risky. If YES, that may cause the exposure of sensitive data.

Quark Script CWE-327.py
=======================

.. code-block:: python 

    from quark.script import runQuarkAnalysis, Rule

    SAMPLE_PATH = "InjuredAndroid.apk"
    RULE_PATH = "useOfCryptographicAlgo.json"

    WEAK_ALGORITHMS = ["DES", "ARC4", "BLOWFISH"]

    ruleInstance = Rule(RULE_PATH)
    quarkResult = runQuarkAnalysis(SAMPLE_PATH, ruleInstance)

    for useCryptoAlgo in quarkResult.behaviorOccurList:

        caller = useCryptoAlgo.methodCaller

        for algo in WEAK_ALGORITHMS:
            if useCryptoAlgo.hasString(algo):
                print(f"CWE-327 is detected in method, {caller.fullName}")
 
Quark Rule: useOfCryptographicAlgo.json
=======================================

.. code-block:: json
    
    {
        "crime": "Use of cryptographic algorithm",
        "permission": [],
        "api": [
            {
                "class": "Ljavax/crypto/Cipher;",
                "method": "getInstance",
                "descriptor": "(Ljava/lang/String;)Ljavax/crypto/Cipher"
            },
            {
                "class": "Ljavax/crypto/Cipher;",
                "method": "init",
                "descriptor": "(I Ljava/security/Key;)V"
            }
        ],
        "score": 1,
        "label": []
    }

Quark Script Result
===================

.. code-block:: TEXT

    $ python3 CWE-327.py
    CWE-327 is detected in method, Lb3nac/injuredandroid/k; b (Ljava/lang/String;)Ljava/lang/String;
    CWE-327 is detected in method, Lb3nac/injuredandroid/k; a (Ljava/lang/String;)Ljava/lang/String;


Detect CWE-20 in Android Application (diva.apk)
-----------------------------------------------

This scenario seeks to find **Improper Input Validation**. See `CWE-20 <https://cwe.mitre.org/data/definitions/20.html>`_ for more details.

Let’s use this `APK <https://github.com/payatu/diva-android>`_ and the above APIs to show how the Quark script finds this vulnerability.

First, we design a detection rule ``openUrlThatUserInput.json`` to spot the behavior of opening the URL that the user input. Then we use API ``behaviorInstance.getMethodsInArgs`` to get a list of methods which the URL in ``loadUrl`` has passed through. Finally, we check if any validation method is in the list. If **No**, the APK does not validate user input. 
That causes CWE-20 vulnerability.




Quark Script CWE-20.py
======================

.. code-block:: python

    from quark.script import runQuarkAnalysis, Rule

    SAMPLE_PATH = "diva.apk"
    RULE_PATH = "openUrlThatUserInput.json"

    rule = Rule(RULE_PATH)
    result = runQuarkAnalysis(SAMPLE_PATH, rule)

    VALIDATE_METHODS = ["contains", "indexOf", "matches", "replaceAll"]

    for openUrl in result.behaviorOccurList:
        calledMethods = openUrl.getMethodsInArgs()

        if not any(method.methodName in VALIDATE_METHODS
                for method in calledMethods):
            print("CWE-20 is detected in method,"
                f"{openUrl.methodCaller.fullName}")



Quark Rule: inputWebUrl.json
====================================

.. code-block:: json
    
    {
        "crime": "Open the Url that user input",
        "permission": [],
        "api": [
            {
                "class": "Landroid/widget/EditText;",
                "method": "getText",
                "descriptor": "()Landroid/text/Editable;"
            },
            {
                "class": "Landroid/webkit/WebView;",
                "method": "loadUrl",
                "descriptor": "(Ljava/lang/String;)V"
            }
        ],
        "score": 1,
        "label": []
    }

Quark Script Result
===================

.. code-block:: TEXT

   $ python CWE-20.py 
   CWE-20 is detected in method, Ljakhar/aseem/diva/InputValidation2URISchemeActivity; get (Landroid/view/View;)V



Detect CWE-79 in Android Application (Vuldroid.apk)
------------------------------------------------------

This scenario seeks to find **Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting').** See `CWE-79 <https://cwe.mitre.org/data/definitions/79.html>`_ for more details.

Let’s use this `APK <https://github.com/jaiswalakshansh/Vuldroid>`_ and the above APIs to show how the Quark script finds this vulnerability. 

First, we design a detection rule ``loadUrlFromIntent.json`` to spot on behavior loading URL from intent data to the WebView instance.

Next, we use API ``quarkResultInstance.findMethodInCaller(callerMethod, targetMethod)`` and ``methodInstance.getArguments()``  to check if the Javascript execution is enabled in the WebView. Finally, we check if there are any famous XSS filters. If **NO**, that may cause CWE-79 vulnerability.


Quark Script CWE-79.py
========================

.. code-block:: python
     
    from quark.script import runQuarkAnalysis, Rule

    SAMPLE_PATH = "Vuldroid.apk"
    RULE_PATH = "loadUrlFromIntent.json"

    XSS_FILTERS = [
        [
            "Lorg/owasp/esapi/Validator;", "getValidSafeHTML",
            "(Ljava/lang/String; Ljava/lang/String; I Z)Ljava/lang/String;",
        ],
        [
            "Lorg/owasp/esapi/Encoder;", "encodeForHTML",
            "(Ljava/lang/String;)Ljava/lang/String;",
        ],
        [
            "Lorg/owasp/esapi/Encoder;", "encodeForJavaScript",
            "(Ljava/lang/String;)Ljava/lang/String;",
        ],
        [
            "Lorg/owasp/html/PolicyFactory;", "sanitize",
            "(Ljava/lang/String;)Ljava/lang/String;",
        ],
    ]

    targetMethod = [
        "Landroid/webkit/WebSettings;", "setJavaScriptEnabled",
        "(Z)V"
    ]

    ruleInstance = Rule(RULE_PATH)
    quarkResult = runQuarkAnalysis(SAMPLE_PATH, ruleInstance)

    for loadUrl in quarkResult.behaviorOccurList:
        caller = loadUrl.methodCaller
        setJS = quarkResult.findMethodInCaller(caller, targetMethod)
        enableJS = []

        if setJS:
            enableJS = setJS[0].getArguments()[1]

        if enableJS:
            XSSFiltersInCaller = [
                filterAPI for filterAPI in XSS_FILTERS if quarkResult.findMethodInCaller(caller, filterAPI)
            ]

            if not XSSFiltersInCaller:
                print(f"CWE-79 is detected in method, {caller.fullName}")


Quark Rule: loadUrlFromIntent.json
====================================

.. code-block:: json
    
    {
        "crime": "Load URL from intent to WebView",
        "permission": [],
        "api": [
            {
                "descriptor": "()Landroid/net/Uri;",
                "class": "Landroid/content/Intent;",
                "method": "getData"
            },
            {
                "descriptor": "(Ljava/lang/String;)V",
                "class": "Landroid/webkit/WebView;",
                "method": "loadUrl"
            }
        ],
        "score": 1,
        "label": []
    }


Quark Script Result
===================

.. code-block:: TEXT

    $ python CWE-79.py  
    CWE-79 is detected in method, Lcom/vuldroid/application/ForgetPassword; onCreate (Landroid/os/Bundle;)V



Detect CWE-328 in Android Application (allsafe.apk)
------------------------------------------------------

This scenario seeks to find **the use of weak Hash**. See `CWE-328 <https://cwe.mitre.org/data/definitions/328.html>`_ for more details.

Let’s use  `allsafe.apk <https://github.com/t0thkr1s/allsafe>`_, `ovaa.apk <https://github.com/oversecured/ovaa>`_, `AndroGoat.apk <https://github.com/satishpatnayak/AndroGoat>`_, `MSTG-Android-Java.apk <https://github.com/OWASP/MASTG-Hacking-Playground>`_, and the above APIs to show how the Quark script finds this vulnerability.

First, we use API ``findMethodInAPK(samplePath, targetMethod)`` to find the method ``MessageDigest.getInstance()`` or ``SecretKeyFactory.getInstance()``. Next, we use API ``methodInstance.getArguments()`` with a list to check if the method uses `weak hashing algorithms <https://en.wikipedia.org/wiki/Hash_function_security_summary>`_. If **YES**, that causes CWE-328 vulnerability.

Quark Script CWE-328.py
========================

.. code-block:: python
     
    from quark.script import findMethodInAPK

    SAMPLE_PATHS = [
            "./allsafe.apk",   "./ovaa.apk",
            "./AndroGoat.apk", "./MSTG-Android-Java.apk"
    ]

    TARGET_METHODS = [
        [
            "Ljava/security/MessageDigest;", "getInstance",
            "(Ljava/lang/String;)Ljava/security/MessageDigest;"
        ],
        [
            "Ljavax/crypto/SecretKeyFactory;", "getInstance",
            "(Ljava/lang/String;)Ljavax/crypto/SecretKeyFactory;"
        ]
    ]

    HASH_KEYWORDS = [
        "MD2",  "MD4",  "MD5",      "PANAMA",
        "SHA0", "SHA1", "HAVAL128", "RIPEMD128"
    ]

    for samplePath in SAMPLE_PATHS:

        methodsFound = []
        for target in TARGET_METHODS:
            methodsFound += findMethodInAPK(samplePath, target)

        for setHashAlgo in methodsFound:
            algoName = setHashAlgo.getArguments()[0].replace("-", "")

            if any(keyword in algoName for keyword in HASH_KEYWORDS):
                print(f"CWE-328 is detected in {samplePath},\n\t"
                      f"and it occurs in method, {setHashAlgo.fullName}")


Quark Script Result
===================

.. code-block:: TEXT

    $ python CWE-328.py
    CWE-328 is detected in ./allsafe.apk,
            and it occurs in method, Linfosecadventures/allsafe/challenges/SQLInjection; md5 (Ljava/lang/String;)Ljava/lang/String;
    CWE-328 is detected in ./allsafe.apk,
            and it occurs in method, Lcom/google/firebase/database/core/utilities/Utilities; sha1HexDigest (Ljava/lang/String;)Ljava/lang/String;
    CWE-328 is detected in ./allsafe.apk,
            and it occurs in method, Linfosecadventures/allsafe/challenges/WeakCryptography; md5Hash (Ljava/lang/String;)Ljava/lang/String;
    CWE-328 is detected in ./ovaa.apk,
            and it occurs in method, Lorg/apache/commons/io/input/MessageDigestCalculatingInputStream; <init> (Ljava/io/InputStream;)V
    CWE-328 is detected in ./AndroGoat.apk,
            and it occurs in method, Lowasp/sat/agoat/AccessControlIssue1Activity; hashPIN (Ljava/lang/String;)Ljava/lang/String;
    CWE-328 is detected in ./MSTG-Android-Java.apk,
        and it occurs in method, Lcom/tozny/crypto/android/AesCbcWithIntegrity; generateKeyFromPassword (Ljava/lang/String; [B)Lcom/tozny/crypto/android/AesCbcWithIntegrity$SecretKeys;

Detect CWE-295 in Android Application (InsecureShop.apk)
----------------------------------------------------------

This scenario seeks to find **Improper Certificate Validation**. See
`CWE-295 <https://cwe.mitre.org/data/definitions/295.html>`__ for more
details.

Let’s use this `APK <https://github.com/hax0rgb/InsecureShop>`__ and the
above APIs to show how the Quark script finds this vulnerability.

We use the API ``findMethodInAPK`` to locate all
``SslErrorHandler.proceed`` methods. Then we need to identify whether if
the method ``WebViewClient.onReceivedSslError`` is overrode by its
subclass.

First, we check and make sure that the ``MethodInstance.name`` is
``onReceivedSslError``, and the ``MethodInstance.descriptor`` is
``(Landroid/webkit/WebView; Landroid/webkit/SslErrorHandler; Landroid/net/http/SslError;)V``.

Then we use the API 
``MethodInstance.findSuperclassHierarchy`` to get the superclass list of
the method’s caller class.

Finally, we check the ``Landroid/webkit/WebViewClient;`` is on the
superclass list. If **YES**, that may cause CWE-295 vulnerability.

Quark Script CWE-295.py
========================

.. code-block:: python
     
    from quark.script import findMethodInAPK

    SAMPLE_PATH = "insecureShop.apk"
    TARGET_METHOD = [
        "Landroid/webkit/SslErrorHandler;",  # class name
        "proceed",                           # method name
        "()V"                                # descriptor
    ]
    OVERRIDE_METHOD = [
        "Landroid/webkit/WebViewClient;",    # class name
        "onReceivedSslError",                # method name
        "(Landroid/webkit/WebView;"+" Landroid/webkit/SslErrorHandler;" + \
        " Landroid/net/http/SslError;)V"     # descriptor
    ]

    for sslProceedCaller in findMethodInAPK(SAMPLE_PATH, TARGET_METHOD):
        if (sslProceedCaller.name == OVERRIDE_METHOD[1] and
        sslProceedCaller.descriptor == OVERRIDE_METHOD[2] and
        OVERRIDE_METHOD[0] in sslProceedCaller.findSuperclassHierarchy()):
            print(f"CWE-295 is detected in method, {sslProceedCaller.fullName}")

Quark Script Result
===================

.. code-block:: TEXT

   $　python3 CWE-295.py
   Requested API level 29 is larger than maximum we have, returning API level 28 instead.
   CWE-295 is detected in method, Lcom/insecureshop/util/CustomWebViewClient; onReceivedSslError (Landroid/webkit/WebView; Landroid/webkit/SslErrorHandler; Landroid/net/http/SslError;)V


Detect CWE-489 in Android Application (allsafe.apk, AndroGoat.apk, pivaa.apk)
-------------------------------------------------------------------------------

This scenario seeks to find **active debug code** in the APK file. See `CWE-489 <https://cwe.mitre.org/data/definitions/489.html>`_ for more details.

Let's use `allsafe.apk <https://github.com/t0thkr1s/allsafe>`_, `AndroGoat.apk <https://github.com/satishpatnayak/AndroGoat>`_, `pivaa.apk <https://github.com/HTBridge/pivaa>`_, and the above APIs to show how the Quark script finds this vulnerability.

First, we use Quark API ``getApplication`` to get the application element in the manifest file. Then we use ``applicationInstance.isDebuggable`` to check if the application element sets the attribute ``android:debuggable`` to true. If **Yes**, that causes CWE-489 vulnerabilities.

Quark Script CWE-489.py
===========================

The Quark Script below uses allsafe.apk to demonstrate. You can change the ``SAMPLE_PATH`` to the sample you want to detect. For example, ``SAMPLE_PATH = AndroGoat.apk`` or ``SAMPLE_PATH = pivaa.apk``.

.. code-block:: python

    from quark.script import getApplication

    SAMPLE_PATH = "allsafe.apk"

    if getApplication(SAMPLE_PATH).isDebuggable():
        print(f"CWE-489 is detected in {SAMPLE_PATH}.")    

Quark Script Result
======================
- **allsafe.apk**

.. code-block:: TEXT
    
    $ python3 CWE-489.py
    CWE-489 is detected in allsafe.apk

- **AndroGoat.apk**

.. code-block:: TEXT
    
    $ python3 CWE-489.py
    CWE-489 is detected in AndroGoat.apk

- **pivaa.apk**

.. code-block:: TEXT
    
    $ python3 CWE-489.py
    CWE-489 is detected in pivaa.apk

Detect CWE-22 in Android Application (ovaa.apk and InsecureBankv2.apk )
-----------------------------------------------------------------------
This scenario seeks to find **the improper limitation of a pathname to a restricted directory ('Path Traversal')**. See `CWE-22 <https://cwe.mitre.org/data/definitions/22.html>`_ for more details.

Let’s use `ovaa.apk <https://github.com/oversecured/ovaa>`_, `InsecureBankv2.apk <https://github.com/dineshshetty/Android-InsecureBankv2/releases>`_, and the above APIs to show how the Quark script finds this vulnerability.

First, we design a detection rule ``accessFileInExternalDir.json`` to spot behavior accessing a file in an external directory.

Next, we use API ``methodInstance.getArguments()`` to get the argument for the file path and use `quarkResultInstance.isHardcoded(argument)` to check if the argument is hardcoded into the APK. If No, the argument is from external input.

Finally, we use Quark API ``quarkResultInstance.findMethodInCaller(callerMethod, targetMethod)`` to check if there are any APIs in the caller method for string matching. If **NO**, the APK does not neutralize special elements within the argument, which may cause CWE-22 vulnerability.

Quark Script CWE-22.py
=======================

The Quark Script below uses ovaa.apk to demonstrate. You can change the ``SAMPLE_PATH`` to the sample you want to detect. For example, ``SAMPLE_PATH = InsecureBankv2.apk``.

.. code-block:: python

    from quark.script import runQuarkAnalysis, Rule

    SAMPLE_PATH = "ovaa.apk"
    RULE_PATH = "accessFileInExternalDir.json"


    STRING_MATCHING_API = [
        ["Ljava/lang/String;", "contains", "(Ljava/lang/CharSequence)Z"],
        ["Ljava/lang/String;", "indexOf", "(I)I"],
        ["Ljava/lang/String;", "indexOf", "(Ljava/lang/String;)I"],
        ["Ljava/lang/String;", "matches", "(Ljava/lang/String;)Z"],
    ]


    ruleInstance = Rule(RULE_PATH)
    quarkResult = runQuarkAnalysis(SAMPLE_PATH, ruleInstance)

    for accessExternalDir in quarkResult.behaviorOccurList:

        filePath = accessExternalDir.secondAPI.getArguments()[2]

        if quarkResult.isHardcoded(filePath):
            continue

        caller = accessExternalDir.methodCaller
        strMatchingAPIs = [
                api for api in STRING_MATCHING_API if quarkResult.findMethodInCaller(
                    caller, api)
        ]

        if not strMatchingAPIs:
            print(f"CWE-22 is detected in method, {caller.fullName}")

Quark Rule: accessFileInExternalDir.json
=========================================

.. code-block:: json

    {
        "crime": "Access a file in an external directory",
        "permission": [],
        "api": [
            {
                "class": "Landroid/os/Environment;",
                "method": "getExternalStorageDirectory",
                "descriptor": "()Ljava/io/File;"
            },
            {
                "class": "Ljava/io/File;",
                "method": "<init>",
                "descriptor": "(Ljava/io/File;Ljava/lang/String;)V"
            }
        ],
        "score": 1,
        "label": []
    }


Quark Script Result
======================
- **ovaa.apk**

.. code-block:: TEXT
    
    $ python3 CWE-22.py
    CWE-22 is detected in method, Loversecured/ovaa/providers/TheftOverwriteProvider; openFile (Landroid/net/Uri; Ljava/lang/String;)Landroid/os/ParcelFileDescriptor;

- **InsecureBankv2.apk**

.. code-block:: TEXT
    
    $ python3 CWE-22.py
    CWE-22 is detected in method, Lcom/android/insecurebankv2/ViewStatement; onCreate (Landroid/os/Bundle;)V

Detect CWE-23 in Android Application (ovaa.apk and InsecureBankv2.apk )
-----------------------------------------------------------------------
This scenario aims to demonstrate the detection of the **Relative Path Traversal** vulnerability using `ovaa.apk <https://github.com/oversecured/ovaa>`_ and `InsecureBankv2.apk <https://github.com/dineshshetty/Android-InsecureBankv2/releases>`_. See `CWE-23 <https://cwe.mitre.org/data/definitions/23.html>`_ for more details.

To begin with, we will create a detection rule named ``accessFileInExternalDir.json`` to identify behavior that accesses a file in an external directory.

Next, we will use ``methodInstance.getArguments()`` to retrieve the file path argument and check whether it belongs to the APK or not. If it does not belong to the APK, the argument is likely from external input.

Finally, we will use the Quark API ``quarkResultInstance.findMethodInCaller(callerMethod, targetMethod)`` to search for any APIs in the caller method that match the string. If no matching API is found, the APK does not neutralize special elements within the argument, which may result in the CWE-23 vulnerability. If a matching API is found, we will verify whether it neutralizes the Relative Path string or not. If it does not neutralize it, the APK may still be vulnerable to CWE-23.

Quark Script CWE-23.py
=======================

The Quark Script below uses ovaa.apk to demonstrate. You can change the ``SAMPLE_PATH`` to the sample you want to detect. For example,  ``SAMPLE_PATH = "InsecureBankv2.apk"``.

.. code-block:: python

    from quark.script import runQuarkAnalysis, Rule

    SAMPLE_PATH = "ovaa.apk"
    RULE_PATH = "accessFileInExternalDir.json"


    STRING_MATCHING_API = [
        ["Ljava/lang/String;", "contains", "(Ljava/lang/CharSequence)Z"],
        ["Ljava/lang/String;", "indexOf", "(I)I"],
        ["Ljava/lang/String;", "indexOf", "(Ljava/lang/String;)I"],
        ["Ljava/lang/String;", "matches", "(Ljava/lang/String;)Z"],
        ["Ljava/lang/String;", "replaceAll",
            "(Ljava/lang/String; Ljava/lang/String;)Ljava/lang/String;"],
    ]

    ruleInstance = Rule(RULE_PATH)
    quarkResult = runQuarkAnalysis(SAMPLE_PATH, ruleInstance)

    for accessExternalDir in quarkResult.behaviorOccurList:

        filePath = accessExternalDir.secondAPI.getArguments()[2]

        if quarkResult.isHardcoded(filePath):
            continue

        caller = accessExternalDir.methodCaller
        strMatchingAPIs = [
            api for api in STRING_MATCHING_API if quarkResult.findMethodInCaller(
                caller, api)
        ]

        if not strMatchingAPIs:
            print(f"CWE-23 is detected in method, {caller.fullName}")
        elif strMatchingAPIs.find("..") == -1:
            print(f"CWE-23 is detected in method, {caller.fullName}")

                
Quark Rule: accessFileInExternalDir.json
=========================================

.. code-block:: json

    {
        "crime": "Access a file in an external directory",
        "permission": [],
        "api": [
            {
                "class": "Landroid/os/Environment;",
                "method": "getExternalStorageDirectory",
                "descriptor": "()Ljava/io/File;"
            },
            {
                "class": "Ljava/io/File;",
                "method": "<init>",
                "descriptor": "(Ljava/io/File;Ljava/lang/String;)V"
            }
        ],
        "score": 1,
        "label": []
    }


Quark Script Result
======================
- **ovaa.apk**

.. code-block:: TEXT
    
    $ python3 CWE-23.py
    CWE-23 is detected in method, Loversecured/ovaa/providers/TheftOverwriteProvider; openFile (Landroid/net/Uri; Ljava/lang/String;)Landroid/os/ParcelFileDescriptor;

- **InsecureBankv2.apk**

.. code-block:: TEXT
    
    $ python3 CWE-23.py
    CWE-23 is detected in method, Lcom/android/insecurebankv2/ViewStatement; onCreate (Landroid/os/Bundle;)V

Detect CWE-338 in Android Application (pivva.apk)
------------------------------------------------------

This scenario aims to detect the **Use of Cryptographically Weak Pseudo-Random Number Generator (PRNG).** See `CWE-338 <https://cwe.mitre.org/data/definitions/338.html>`_ for more details.

To demonstrate how the Quark script finds this vulnerability, we will use the `pivaa <https://github.com/HTBridge/pivaa>`_ APK file and the above APIs.

First, we design a detection rule useMethodOfPRNG.json to spot on behavior that uses Pseudo Random Number Generator (PRNG). Then, we use API ``getXrefFrom()`` to get the caller method of PRNG. Finally, we use some keywords such as “token”, “password”, and “encrypt” to check if the PRNG is for credential usage.

Quark Script CWE-338.py
========================
.. code-block:: python
     
    from quark.script import runQuarkAnalysis, Rule

    SAMPLE_PATH = "pivaa.apk"
    RULE_PATH = "useMethodOfPRNG.json"

    CREDENTIAL_KEYWORDS = [
        "token", "password", "account", "encrypt",
        "authentication", "authorization", "id", "key"
    ]

    ruleInstance = Rule(RULE_PATH)
    quarkResult = runQuarkAnalysis(SAMPLE_PATH, ruleInstance)

    for usePRNGMethod in quarkResult.behaviorOccurList:
        for prngCaller in usePRNGMethod.methodCaller.getXrefFrom():
            if any(keyword in prngCaller.fullName
                for keyword in CREDENTIAL_KEYWORDS):
                print("CWE-338 is detected in %s" % prngCaller.fullName)

useMethodOfPRNG.json
========================
.. code-block:: json
    
    {
        "crime": "Use method of PRNG",
        "permission": [],
        "api": [
            {
                "class": "Ljava/util/Random;",
                "method": "<init>",
                "descriptor": "()V"
            },
            {
                "class": "Ljava/util/Random;",
                "method": "nextInt",
                "descriptor": "(I)I"
            }
        ],
        "score": 1,
        "label": []
    }

Quark Script Result
===================

.. code-block:: TEXT

    $ python CWE-338.py  
    CWE-338 is detected in Lcom/htbridge/pivaa/EncryptionActivity$2; onClick (Landroid/view/View;)V
    


Detect CWE-88 in Android Application (Vuldroid.apk)
------------------------------------------------------

This scenario seeks to find **Improper Neutralization of Argument Delimiters in a Command**. See `CWE-88 <https://cwe.mitre.org/data/definitions/88.html>`_ for more details.

Let‘s use this `APK <https://github.com/jaiswalakshansh/Vuldroid>`_ and the above APIs to show how the Quark script finds this vulnerability.

First, we design a detection rule ``ExternalStringsCommands.json`` to spot on behavior using external strings as commands.

Next, we use Quark API ``quarkResultInstance.findMethodInCaller(callerMethod, targetMethod)`` to check if any APIs in the caller method for string matching. 

If NO, the APK does not neutralize special elements within the argument, which may cause CWE-88 vulnerability. 

If YES, check if there are any delimiters used in string matching for a filter. If NO, the APK does not neutralize special elements within the argument, which may cause CWE-88 vulnerability. 


Quark Script CWE-88.py
=======================

The Quark Script below uses Vuldroid.apk to demonstrate.

.. code-block:: python

    from quark.script import runQuarkAnalysis, Rule

    SAMPLE_PATH = "Vuldroid.apk"
    RULE_PATH = "ExternalStringCommand.json"


    STRING_MATCHING_API = [
        ["Ljava/lang/String;", "contains", "(Ljava/lang/CharSequence)Z"],
        ["Ljava/lang/String;", "indexOf", "(I)I"],
        ["Ljava/lang/String;", "indexOf", "(Ljava/lang/String;)I"],
        ["Ljava/lang/String;", "matches", "(Ljava/lang/String;)Z"],
        ["Ljava/lang/String;", "replaceAll",
            "(Ljava/lang/String; Ljava/lang/String;)Ljava/lang/String;"],
    ]

    delimiters = [' ', ';', '||', '|', ',', '>', '>>', '`']

    ruleInstance = Rule(RULE_PATH)
    quarkResult = runQuarkAnalysis(SAMPLE_PATH, ruleInstance)

    for ExternalStringCommand in quarkResult.behaviorOccurList:

        caller = ExternalStringCommand.methodCaller

        strMatchingAPIs = [
            api for api in STRING_MATCHING_API if
            quarkResult.findMethodInCaller(caller, api)
        ]

        if not strMatchingAPIs or \
                any(dlm not in strMatchingAPIs for dlm in delimiters):
            print(f"CWE-88 is detected in method, {caller.fullName}")

                
Quark Rule: ExternalStringCommand.json
=========================================

.. code-block:: json

    {
        "crime": "Using external strings as commands",
        "permission": [],
        "api": [
            {
                "class": "Landroid/content/Intent;",
                "method": "getStringExtra",
                "descriptor": "(Ljava/lang/String;)Ljava/lang/String"
            },
            {
                "class": "Ljava/lang/Runtime;",
                "method": "exec",
                "descriptor": "(Ljava/lang/String;)Ljava/lang/Process"
            }
        ],
        "score": 1,
        "label": []
    }


Quark Script Result
======================
- **Vuldroid.apk**

.. code-block:: TEXT

    $ python3 CWE-88.py
    CWE-88 is detected in method, Lcom/vuldroid/application/RootDetection; onCreate (Landroid/os/Bundle;)V

Detect CWE-925 in Android Application (InsecureBankv2, AndroGoat)
------------------------------------------------------------------

This scenario seeks to find **Improper Verification of Intent by
Broadcast Receiver**. See
`CWE-925 <https://cwe.mitre.org/data/definitions/925.html>`__ for more
details.

Let’s use both two of apks
(`InsecureBankv2 <https://github.com/dineshshetty/Android-InsecureBankv2>`__
and `AndroGoat <https://github.com/satishpatnayak/AndroGoat>`__) to show
how the Quark script finds this vulnerability.

In the first step, we use the ``getReceivers`` API to find all
``Receiver`` components defined in the Android application. Then, we
exclude any receivers that are not exported.

In the second step, our goal is to verify the **intentAction** is
properly validated in each receiver which is identified in the previous
step. To do this, we use the ``checkMethodCalls`` function.

Finally, if any receiver’s **onReceive** method exhibits improper
verification on **intentAction**, it could indicate a potential CWE-925
vulnerability.

Quark Script CWE-925.py
=======================

.. code:: python

   from quark.script import checkMethodCalls, getReceivers

   SAMPLE_PATHS = ["AndroGoat.apk", "InsecureBankv2.apk"]

   TARGET_METHOD = [
       '',
       'onReceive',
       '(Landroid/content/Context; Landroid/content/Intent;)V'
   ]

   CHECK_METHODS = [
       ['Landroid/content/Intent;', 'getAction', '()Ljava/lang/String;']
   ]

   for filepath in SAMPLE_PATHS:
       receivers = getReceivers(filepath)
       for receiver in receivers:
           if receiver.isExported():
               className = "L"+str(receiver).replace('.', '/')+';'
               TARGET_METHOD[0] = className
               if not checkMethodCalls(filepath, TARGET_METHOD, CHECK_METHODS):
                   print(f"CWE-925 is detected in method, {className}")

Quark Script Result
===================

.. code-block:: TEXT

   $ python CWE-925.py
   CWE-925 is detected in method, Lowasp/sat/agoat/ShowDataReceiver;
   CWE-925 is detected in method, Lcom/android/insecurebankv2/MyBroadCastReceiver;

Detect  CWE-73 in Android Application (ovaa.apk)
---------------------------------------------------

This scenario seeks to find **External Control of File Name or Path**. See
`CWE-73 <https://cwe.mitre.org/data/definitions/73.html>`__ for more
details.

First, we design a detection rule ``accessFileInExternalDir.json`` to spot behavior accessing a file in an external directory.

Second, we use API ``methodInstance.getArguments()`` to get the argument for the file path and use ``quarkResultInstance.isHardcoded(argument)`` to check if the argument is hardcoded into the APK. If **No**, the argument is from external input.

Finally, we use Quark API ``quarkResultInstance.findMethodInCaller(callerMethod, targetMethod)``  to check if any APIs in the caller method for opening files. If **YES**, the APK performs file operations using external input as a path, which may cause CWE-73 vulnerability.

Quark Script CWE-73.py
=======================

.. code:: python

    from quark.script import runQuarkAnalysis, Rule

    SAMPLE_PATH = "ovaa.apk"
    RULE_PATH = "accessFileInExternalDir.json"

    OPEN_FILE_API = [
        "Landroid/os/ParcelFileDescriptor;",                   # Class name
        "open",                                                # Method name   
        "(Ljava/io/File; I)Landroid/os/ParcelFileDescriptor;"  # Descriptor
    ]

    ruleInstance = Rule(RULE_PATH)
    quarkResult = runQuarkAnalysis(SAMPLE_PATH, ruleInstance)

    for accessExternalDir in quarkResult.behaviorOccurList:
        filePath = accessExternalDir.secondAPI.getArguments()[2]
    
        if quarkResult.isHardcoded(filePath):
            continue

        caller = accessExternalDir.methodCaller
        result = quarkResult.findMethodInCaller(caller, OPEN_FILE_API)

        if result:
            print("CWE-73 is detected in method, ", caller.fullName)
         
Quark Rule: accessFileInExternalDir.json
=========================================

.. code-block:: json

    {
        "crime": "Access a file in an external directory",
        "permission": [],
        "api": [
            {
                "class": "Landroid/os/Environment;",
                "method": "getExternalStorageDirectory",
                "descriptor": "()Ljava/io/File;"
            },
            {
                "class": "Ljava/io/File;",
                "method": "<init>",
                "descriptor": "(Ljava/io/File;Ljava/lang/String;)V"
            }
        ],
        "score": 1,
        "label": []
    }

Quark Script Result
=====================

.. code-block:: TEXT

   $ python CWE-73.py
   CWE-73 is detected in method, Loversecured/ovaa/providers/TheftOverwriteProvider; openFile (Landroid/net/Uri; Ljava/lang/String;)Landroid/os/ParcelFileDescriptor;
