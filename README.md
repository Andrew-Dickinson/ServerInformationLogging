# Server Information Logging
A simple set of python scripts to report information on the status of a Linux server. 

Uses <a href="https://github.com/nikdoof/python-ts3">python-ts3</a> and <a href="https://gist.github.com/pklaus/856268">ping.py</a> to gather information about the status of a linux server. The results are published to an html file located in ./www_dev/ and several csv files located under ./www_dev/logs/

The html file log_analysis.html is included and is designed to query the csv output to create pretty graphs of the statistical output. This implements the <a href="https://developers.google.com/chart/">google charts javascript api</a>.

# Raw Log
![alt tag](https://raw.githubusercontent.com/Andrew-Dickinson/ServerInformationLogging/master/screenshots/Capture4.PNG)

# Pretty log
![alt tag](https://raw.githubusercontent.com/Andrew-Dickinson/ServerInformationLogging/master/screenshots/Capture.PNG)
![alt tag](https://raw.githubusercontent.com/Andrew-Dickinson/ServerInformationLogging/master/screenshots/Capture2.PNG)
![alt tag](https://raw.githubusercontent.com/Andrew-Dickinson/ServerInformationLogging/master/screenshots/Capture3.PNG)


