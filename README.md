# Dyson-QA-Solo-Scripts
This repository contains Dyson QA Automation scripts for border and transparency checks. It also contains an additional script used for appending files with the string master or slave

All other files except the below mentioned files are redundant.
1) BORDER_CHECK
2) TRANSPARENCY_CHECK
3) APPEND_MASTER_SLAVE

While converting TRANSPARENCY_CHECK script using pyinstaller, we need to create a hook file called hook-grpc.py and place it inside pyinstaller hooks folder. The hooks file is also attached here in the repository.

For more details: https://stackoverflow.com/questions/51745571/exception-in-grpc-when-trying-to-execute-google-cloud-api?rq=1
