""" This is the main flask routing module """
from flask import Flask, request
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from .modules import run

# app initialization
app = Flask(__name__, static_url_path='/app/app/static')

# Scheduler initialization
# Calling 'run.main' every 7 days
sched = BackgroundScheduler(daemon=True, timezone='Europe/Rome')
# Does not start automatically
sched.add_job(run.main, 'interval', days=7)
sched.start()

@app.route("/")
def hello():
    """ Serve static page """
    return app.send_static_file('index.html')

@app.route("/run")
def force_run():
    """ Run job now """
    for job in sched.get_jobs():
        # job.modify(next_run_time=datetime.now(), kwargs={"force":True})
        # WARNING: This is a synchronous call
        job.func(force=True)
    return "Job scheduled to run in a minute. Go back <a href='/'>HOME</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)
