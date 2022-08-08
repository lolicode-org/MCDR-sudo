from mcdreforged.api.all import *

from sudo.config import CFG_PATH, Config

level: int
Prefix = "!!sudo"


def print_help_message(source: CommandSource):
    msg = "!!sudo example_command : execute command as yourself\n" \
          "!!sudo -u example_user example_command : execute command as another user"
    source.reply(msg)


def print_illegal_argument_message(source: CommandSource):
    msg = "Illegal argument! Type !!sudo to get help."
    source.reply(msg)


def execute_command(source: CommandSource, context: dict):
    if not context.get('command'):
        source.reply('The necessary parameter "command" is missing.')
        return
    user = context.get("player") or (source.player if isinstance(source, PlayerCommandSource) else None)
    cmd = f"execute as {user} at {user} run {context.get('command')}" if user else context.get('command')
    source.get_server().execute(cmd)
    source.reply("Command executed.")


def register_command(server: PluginServerInterface):
    server.register_command(
        Literal(Prefix).
        requires(lambda src: src.has_permission(level)).
        on_error(RequirementNotMet,
                 lambda src: src.reply((RText(server.tr('mcdr_command.permission_denied'), color=RColor.red)))).
        runs(print_help_message).
        on_error(UnknownArgument, print_help_message, handled=True).
        then(
            Literal("-u").
            then(
                QuotableText('player').
                then(
                    GreedyText('command').
                    runs(execute_command)
                )
            )
        ).
        then(
            GreedyText('command').
            runs(execute_command)
        )
    )


def on_load(server: PluginServerInterface, old):
    global level
    cfg = server.load_config_simple(CFG_PATH, target_class=Config, in_data_folder=False, echo_in_console=True,
                                    encoding='UTF-8')
    level = cfg.permission_level

    register_command(server)
