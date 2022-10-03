# Locust and Wiremock playground

# Locust
Locust is an easy to use, scriptable and scalable performance testing tool written in Python.

You define the behaviour of your users in regular Python code, instead of being stuck in a UI or restrictive domain specific language.

This makes Locust infinitely expandable and very developer friendly.

More info: https://locust.io/


# Wiremock
WireMock is an HTTP mock server. At its core it is web server that can be primed to serve canned responses to particular requests (stubbing) and that captures incoming requests so that they can be checked later (verification).

It also has an assortment of other useful features including record/playback of interactions with other APIs, injection of faults and delays, simulation of stateful behaviour.

It can be used as a library by any JVM application, or run as a standalone process either on the same host as the system under test or a remote server.

All of WireMock’s features are accessible via its REST (JSON) interface and its Java API. Additionally, stubs can be configured via JSON files.

More info: https://wiremock.org/

## Prerequisites
1. Pythom
2. Java 11

# Preparatiom
## Wiremock start
The package already includes the wiremock package. Navigate to wiremock folder and execute the following command:
```
java -jar wiremock-studio-2.32.0-18.jar
```

In case Java 11 is not your default version, you can use the following:
```
"/c/Program Files/Java/jdk-11.0.11/bin/java" -jar wiremock-studio-2.32.0-18.jar
```
This will fireup the wiremock localhost, and you are able now to see the available apis:
![image](https://user-images.githubusercontent.com/113723/193519838-25dfd2c4-5463-49f2-80a9-7ef317de8350.png)

Now that Wiremock is up and running you can open your browser and navigate to the Wiremock url admin panel http://localhost:9000  to see the "Services API" that works in http://localhost:8080  


## Locust
To install locust (https://docs.locust.io/en/stable/installation.html), execute the following command:

```
pip3 install locust
```
![image](https://user-images.githubusercontent.com/113723/193520366-1d4dcd1d-3287-47ba-95a2-5467f8145330.png)

To verify the installation:
```
locust -V
```
![image](https://user-images.githubusercontent.com/113723/193520478-b479bb50-ddef-4345-bd62-aa04deb5ae99.png)

# Execution
## Sample test with no parameters
The playground contains 3 diferent locust files.

To execute a test, just run the following:

```
locust -f=sample1.py
```

After each execution, a localhost is provided by Locust, where you can open it in your browser: 
![image](https://user-images.githubusercontent.com/113723/193532328-4af84b7f-4e51-4d1f-bb81-31edab33d00a.png)

When the "Start swarming" is pressed, the execution starts:
![image](https://user-images.githubusercontent.com/113723/193532431-1306ec6b-dee3-4a40-abd0-301d0f59f68c.png)


To add more command properties, the command can be updated:
```
locust -f sample1 -u 10 -r 3 -H http://localhost:8000
```
