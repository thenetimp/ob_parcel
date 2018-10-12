from flask import Flask, session
from datetime import datetime, timedelta

app = Flask(__name__)

@app.context_processor
def inject_stage_and_region():
    return dict(site_version=(datetime.now() - datetime(1970, 1, 1)).total_seconds())

app.config.from_envvar('OPENBRIDGE_PARCEL_CONFIG')

from parcel.modules.core.views import core_views
app.register_blueprint(core_views)


if __name__ == '__main__':
    print("testing")