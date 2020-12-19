The script will use the alphadvantage.co api to get information on a stock for example Tesla and send an SMS notification to the user if the price of the stock increases or decreases by atleast 5% each day

1. Application will pull stock prices
2. It will calculate the percentage increase or decrease in the stock's cost at close of day
3. Twilio is used to send 3 sms each containing an article about the stock if there is a difference of >= 5%

# Installation:

- ###clone the application

`git https://github.com/webdev2145/stock-tracker.git`

- ###change into the directory

`cd stock-tracker`
  
- ###execute the application

`python3 main.py`
  
### Note: 
- There is currently no automation configured eg. cron job or python anywhere could be used

- I will look into adding those steps at a later date

- I have removed my twilio, news and stock api keys (These are **NEEDED** for the script to work)

[Alphavantage!] (https://www.alphavantage.co)

[Stock News] https://newsapi.org

[Twilio] https://www.twilio.com


