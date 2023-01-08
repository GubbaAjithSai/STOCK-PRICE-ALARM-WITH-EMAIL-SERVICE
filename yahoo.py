import yfinance as yf
from timeloop import Timeloop
from datetime import timedelta
import os
import smtplib
#email
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('ajtesting0@gmail.com','password')
#stockinfo
data=yf.Ticker("BAJFINANCE.NS")
targetPrice=71920
#dma
prev=data.history('1y')
tl = Timeloop()
@tl.job(interval=timedelta(seconds=10))
def main():
    currPrice =data.info['regularMarketPrice']
    prev=data.history('1y')
    dma200= prev.Close.rolling(200).mean()[-1]
    if(currPrice>=targetPrice):
        os.startfile("C:\\Users\\gubba\\Downloads\\Kalki Bgm.mp3")
        server.sendmail('ajtesting0@gmail.com','gubbaajithsai@gmail.com', 'price alert')
    elif(dma200<currPrice):
        server.sendmail('ajtesting0@gmail.com', 'gubbaajithsai@gmail.com', 'price breached daily moving average(200)')
    else:
        print(currPrice)
tl.start(block=True)