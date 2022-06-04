from json import dump

from mcdreforged.api.all import Serializable, ServerInterface

server = ServerInterface.get_instance().as_plugin_server_interface()
CFG_PATH = 'config/sudo.json'
DEFAULT_CFG: dict = {
    "permission_level": 4,
}


class Config(Serializable):
    min_permission: int = 4

    @classmethod
    def load(cls):
        return server.load_config_simple(CFG_PATH, in_data_folder=False, default_config=DEFAULT_CFG,
                                         echo_in_console=True, target_class=cls, encoding='utf-8')

    def save(self):
        with open(CFG_PATH, "w", encoding='utf-8') as w:
            dump(self.serialize(), w, ensure_ascii=False, indent=4)

    def get(self, key: str, default=None):
        if hasattr(self, key):
            return self.__dict__[key]
        else:
            return default


config = Config.load()
