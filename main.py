import os
from datetime import date, datetime
from flask import Flask, request
from utils import getPrecipByYear
# pylint: disable=C0103
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """Get the response from Visual Crossing."""
    Precip_2019 = getPrecipByYear.get_precip_by_year(2019)
    Precip_2020 = getPrecipByYear.get_precip_by_year(2020)
    Precip_2021 = getPrecipByYear.get_precip_by_year(2021)
    Precip_2022 = getPrecipByYear.get_precip_by_year(2022)
    if sum(Precip_2022) >= (sum(Precip_2021) + sum(Precip_2020) + sum(Precip_2019)) / 3:
        return f"The project should be delayed. \n", 200
    else:
        return f"The project should not be delayed. \n", 200

# [END eventarc_audit_bq_handler]

# [START eventarc_audit_bq_server]
if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8000')
    app.run(debug=True, host='127.0.0.1', port=server_port)
