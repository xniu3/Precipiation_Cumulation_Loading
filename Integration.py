import os
import sqlite3
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

from utils import getPrecipByYear, selectTable
from flask import Flask, request
from flask_mail import Mail, Message
# pylint: disable=C0103
app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.qq.com'# change to your email server
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '****************'# change to your own username
app.config['MAIL_PASSWORD'] = '****************'# change to your own password
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

def Precipitation_Cumulation_Loading():
    """Get the response from Visual Crossing."""
    precip_prev3 = getPrecipByYear.get_precip_by_date((datetime.now() - relativedelta(years=3)))
    precip_prev2 = getPrecipByYear.get_precip_by_date((datetime.now() - relativedelta(years=2)))
    precip_prev1 = getPrecipByYear.get_precip_by_date((datetime.now() - relativedelta(years=1)))
    precip_now = getPrecipByYear.get_precip_today()
    conn = sqlite3.connect('db.sqlite3') # May adopt a new database
    c = conn.cursor()
    cursor = c.execute("SELECT ID, FIRST_NAME, LAST_NAME, EMAIL  from EMPLOYEE")
    """Judge if the precipitation will cause a schedule delay. """
    if sum(precip_now) >= (sum(precip_prev1) + sum(precip_prev2) + sum(precip_prev3)) / 3:
        msg = Message('Abnormal Weather Delay', sender='*******@***.***', recipients=[row[3] for row in cursor])
        msg.body = "Due to high precipitation, the project is delayed. "
        mail.send(msg)
    return


if __name__ == '__main__':
    Precipitation_Cumulation_Loading()
