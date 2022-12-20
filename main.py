import os
from datetime import date, datetime
from flask import Flask, request
from utils import getPrecipByYear
# pylint: disable=C0103
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """Get the response from Visual Crossing."""
    print(getPrecipByYear.get_precip_by_year(2021))
    return (f"The project should be delayed. \n", 200)

# [END eventarc_audit_bq_handler]

# [START eventarc_audit_bq_server]
if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8000')
    app.run(debug=True, host='127.0.0.1', port=server_port)