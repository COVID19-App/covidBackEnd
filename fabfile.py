from datetime import datetime
from fabric.api import *
from fabric.colors import green

env.user = 'ubuntu'
env.host_string = 'Ip'
env.password = 'PASSWORD'
home_path = "/home/ubuntu"
project_name = "covidBackEnd"
settings_staging = "--settings='config.settings.production'"
activate_env_staging = "source {}/envs/covid/bin/activate".format(home_path)
manage = "python3 manage.py"



def deploy_production():
    print("Beginning Deploy:")
    with cd("{}/Covid/covidBackEnd".format(home_path)):
        run("git pull origin dev")
        run("{} && pip install -r requirements.txt".format(activate_env_staging))
        run("{} && {} collectstatic --noinput {}".format(activate_env_staging, manage,
                                                         settings_staging))
        run("{} && {} migrate {}".format(activate_env_staging, manage, settings_staging))
        sudo("service nginx restart", pty=False)
        sudo("supervisorctl restart gunicorn_covid", pty=False)
    print(green("Deploy CovidProject successful"))



