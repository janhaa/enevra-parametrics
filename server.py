from flask import Flask, escape, request
from flask_cors import CORS, cross_origin
import configparser
Config = configparser.ConfigParser()

import os

app = Flask(__name__)
cors = CORS(app)

created = False

@app.route("/generateModel")
@cross_origin()
def genModel():
    global created
    fluegel_breite = request.args.get("fb", "10")
    fluegel_laenge = request.args.get("fl", "5")
    armband_laenge = request.args.get("al", "22")
    hinten_breite = request.args.get("hb", "18")

    # freecadcmd doesn"t accept arguments which are passed to script
    # so pass parameters through ini file for now
    cfgfile = open("config.ini","w")
    if not created:
        Config.add_section("parameters")
        created = True
    Config.set("parameters", "fluegel_breite", str(fluegel_breite))
    Config.set("parameters", "fluegel_laenge", str(fluegel_laenge))
    Config.set("parameters", "armband_laenge", str(armband_laenge))
    Config.set("parameters", "hinten_breite", str(hinten_breite))
    Config.write(cfgfile)
    cfgfile.close()

    os.system("freecadcmd test_model_hole.py")
    return "ok"

app.run(host="0.0.0.0")