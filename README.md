Sudo plugin for MCDReforged
-----

Execute any command as the server or any player.

#### Examples:

give yourself a command block:
```plaintext
!!sudo give @s command_block
```

kill Steve:
```plaintext
!!sudo -u Steve kill @s
```

#### Config:
```json
{
  "permission_level": 4
}
```
`permission_level`: Minimum permission required to use this command, defaults to 4.
