from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
import json

# ---------- Globals ---------- #
CSRF = CSRFProtect()
application = Flask(__name__)
with open("_Paragraphs.json", 'r') as ParagraphsFile:
    PF = json.load(ParagraphsFile)


# ---------- Routes ---------- #
@application.route('/', methods=['GET'])
def home_page():
    about_us_string = '\n'.join(PF['About Us'])
    team_strings = PF['Meet The Team']
    services = PF['Services']
    return render_template('HomePage.html', about_us=about_us_string, services=services, team_strings=team_strings)


@application.route('/contact_us', methods=['GET'])
def contact_us_page():
    return render_template('ContactUs.html')


if __name__ == '__main__':
    application.run(debug=False, host='0.0.0.0')



