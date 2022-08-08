import os.path

from mcdreforged.api.all import Serializable, ServerInterface

server = ServerInterface.get_instance().as_plugin_server_interface()
CFG_PATH = os.path.join('config', 'sudo.json')


class Config(Serializable):
    permission_level: int = 4
