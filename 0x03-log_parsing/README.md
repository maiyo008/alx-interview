# 0x03-log_parsing
----
Log parsing refers to the process of analyzing and extracting meaningful information from log files generated by various software applications, systems, or devices. Logs are records of events, actions, or transactions that occur within a system, and they often contain valuable data about the system's performance, errors, user interactions, and more.

Log files can be generated by web servers, database servers, network devices, security systems, and various other components of a computing environment. They typically contain timestamps, event details, error messages, and other relevant information.

Log parsing involves reading log files, parsing their contents, and extracting specific data points or patterns for analysis or further processing. This extracted data can be used for various purposes, such as monitoring system health, identifying security threats, troubleshooting issues, generating reports, and making informed decisions.

In log parsing, developers or analysts often use regular expressions or specific log parsing tools to extract the required information efficiently. Proper log parsing can greatly aid in understanding the behavior of a system, identifying anomalies, and improving its overall performance and security.

## Tasks

### Tasks 0. Log parsing
Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size> (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
Warning: In this sample, you will have random value - it’s normal to not have the same output as this one.

Sample output
```
root@2c462bd13a86:~/alx-interview/0x03-log_parsing# ./0-generator.py | ./0-stats.py
File size: 4118
400: 1
401: 2
403: 1
404: 2
405: 3
500: 1
File size: 8979
200: 3
400: 1
401: 2
403: 2
404: 4
405: 5
500: 3
File size: 13255
200: 5
301: 3
400: 2
401: 3
403: 4
404: 4
405: 6
500: 3
File size: 18567
200: 6
301: 3
400: 3
401: 5
403: 6
404: 4
405: 8
500: 5
File size: 23330
200: 6
301: 3
400: 6
401: 7
403: 8
404: 5
405: 9
500: 6
File size: 29200
200: 6
301: 4
400: 7
401: 8
403: 10
404: 8
405: 10
500: 7
^CFile size: 30161
200: 6
301: 5
Traceback (most recent call last):
400: 7
  File "./0-generator.py", line 8, in <module>
401: 8
403: 10
404: 8
405: 10
500: 9
    sleep(random.random())
KeyboardInterrupt
```