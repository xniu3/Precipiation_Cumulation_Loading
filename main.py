import os
from datetime import date, datetime
from utils import getPrecipByYear
from flask import Flask, request
from flask_mail import Mail, Message
# pylint: disable=C0103
app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.*****.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '*********@***.***'
app.config['MAIL_PASSWORD'] = '*************'
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/", methods=["GET"])
def index():
    """Get the response from Visual Crossing."""
    Precip_2019 = [5.196, 16.822, 3.301, 0.254, 0.0] # getPrecipByYear.get_precip_by_year(2019)
    Precip_2020 = [0.0, 0.0, 0.0, 0.0, 0.0] # getPrecipByYear.get_precip_by_year(2020)
    Precip_2021 = [0.0, 0.0, 0.0, 0.744, 0.857]# getPrecipByYear.get_precip_by_year(2021)
    Precip_2022 = [0.0, 0.0, 0.0, 0.0, 5.861] # getPrecipByYear.get_precip_by_year(2022)
    if sum(Precip_2022) >= (sum(Precip_2021) / len(Precip_2021) + sum(Precip_2020) / len(Precip_2020) + sum(Precip_2019) / len(Precip_2019)) / 3:
        msg = Message('Abnormal Weather Delay', sender='2592784446@qq.com', recipients=['1952066849@qq.com'])
        msg.body = "Due to high precipitation, the project is delayed. "
        mail.send(msg)
        return f"The project should be delayed. \n", 200
    else:
        msg = Message('No abnormal Weather Delay', sender='2592784446@qq.com', recipients=['1952066849@qq.com'])
        msg.body = "No delay schedule due to precipitation. "
        mail.send(msg)
        return f"The project should not be delayed. \n", 200

# [END eventarc_audit_bq_handler]

# [START eventarc_audit_bq_server]
if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8000')
    app.run(debug=True, host='127.0.0.1', port=server_port)