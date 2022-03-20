import secrets
import xerox

from witaker.clipboardserver import (
    name,
    version,
    app,
    DEFAULT_SERVER_PORT,
    start_flask_webserver,
    get_auth_marker,
    get_auth_marker_color,
    AuthorizedClipboardUtil,
)


# TODO: future, override default port - set debug key
# TODO: add Colorama color output
def clipboard_server_cli_main():
    port = DEFAULT_SERVER_PORT
    secret_auth_key = secrets.token_hex()
    xerox.copy(get_auth_marker(port, secret_auth_key))
    print(f" * Initializing {name} {version}  -  {get_auth_marker_color(port, secret_auth_key)}")

    clipboard_util = AuthorizedClipboardUtil(secret_auth_key)
    app.config["clipboard_util"] = clipboard_util

    start_flask_webserver(port, app)
    return 0
