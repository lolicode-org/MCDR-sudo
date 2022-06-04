from mcdreforged.api.all import *

from sudo.config import config

level = config.get("permission_level", 4)


def on_user_info(server: PluginServerInterface, info: Info):
    message = info.content
    if not message.startswith("!!sudo"):
        return
    if not info.get_command_source().has_permission(level):
        info.get_command_source().reply(RText(server.tr('mcdr_command.permission_denied'), color=RColor.red))
        return
    params = message.split(" ", maxsplit=3)

    if len(params) == 1:
        info.get_command_source()\
            .reply("Use !!sudo [-u Username] command to execute command as server or specific user.")
        return
    elif len(params) >= 4 and params[1] == '-u':
        user = params[2]
        command = params[3]
    else:
        user = info.player
        command = message.split(" ", maxsplit=1)[1]
    server.execute(f"execute as {user} at {user} run {command}")
