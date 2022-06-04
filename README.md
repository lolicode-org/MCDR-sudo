Sudo plugin for MCDReforged
-----

Execute any command as the server or any player.

#### Examples:

give yourself op:
```plaintext
!!sudo op @s
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
