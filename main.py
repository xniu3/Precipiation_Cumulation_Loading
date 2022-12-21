import os
import sqlite3
from datetime import date, datetime
from utils import getPrecipByYear, selectTable
from flask import Flask, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.qq.com'  # change to your email server
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '****************'  # change to your own username
app.config['MAIL_PASSWORD'] = '****************'  # change to your own password
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route("/", methods=["GET"])
def index():
    """Get the response from Visual Crossing."""
    precip_2019 = getPrecipByYear.get_precip_by_year(2019)  # [5.196, 16.822, 3.301, 0.254, 0.0] #
    precip_2020 = getPrecipByYear.get_precip_by_year(2020)  # [0.0, 0.0, 0.0, 0.0, 0.0] #
    precip_2021 = getPrecipByYear.get_precip_by_year(2021)  # [0.0, 0.0, 0.0, 0.744, 0.857]#
    precip_2022 = getPrecipByYear.get_precip_by_year(2022)  # [0.0, 0.0, 0.0, 0.0, 5.861]
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    cursor = c.execute("SELECT ID, FIRST_NAME, LAST_NAME, EMAIL  from EMPLOYEE")
    """Judge if the precipitation will cause a schedule delay. """
    if sum(precip_2022) >= (sum(precip_2021) + sum(precip_2020) + sum(precip_2019)) / 3:
        msg = Message('Abnormal Weather Delay', sender='*******@***.***', recipients=[row[3] for row in cursor])
        # change the sender field to your own email address.
        msg.body = "Due to high precipitation, the project is delayed. "
        mail.send(msg)
        return f"The project should be delayed. \n", 200
    else:
        msg = Message('No abnormal Weather Delay', sender='*******@***.***', recipients=[row[3] for row in cursor])
        # change the sender field to your own email address.
        msg.body = "No delay schedule due to precipitation. "
        mail.send(msg)
        return f"The project should not be delayed. \n", 200


if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8000')
    app.run(debug=True, host='127.0.0.1', port=server_port)
