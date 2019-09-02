from invoke.tasks import task
from invoke.collection import Collection
import fabric2
from fabric2.connection import Connection

hostname = "192.168.8.182"

class CliConnection(Connection):

    def update_config(self, user):
        self.user = user
        return self

context = CliConnection(hostname,user="bar")

class Taskset(object):
    """
    NOTE: This should be added to the repo
    """
    def __init__(self, context):
        self.context = context

    def run(self, cmd, echo=True, **kwargs):
        self.context.run(cmd, echo=echo, **kwargs)

class CliTaskset(Taskset):
    @task
    def which_user(self):
        self.context.update_config(user="bar")
        with self.context.update_config(user="root"):
            self.run("whoami")


ns = Collection()
ns.add_collection(Collection.from_class(CliTaskset(context)), name="clitaskset")
