name = "Witaker Clipboard Server"
version = "0.2.0"

from witaker.clipboardserver.clipboard_model import (
    clipboard_content_response,
    clipboard_error_response,
    ClipboardContent,
    ClipboardCopyRequest,
    ClipboardRequestBody,
    ClipboardResponseBody,
    ClipboardText,
)

from witaker.clipboardserver.clipboard_util import (
    AuthorizedClipboardUtil,
    AuthorizedClipboardUtilException,
)

from witaker.clipboardserver.clipboard_server import app

from witaker.clipboardserver.clipboard_server_run import (
    DEFAULT_SERVER_PORT,
    start_flask_webserver,
    start_server_process,
    stop_server_process,
)

from witaker.clipboardserver.clipboard_server_main import clipboard_server_cli_main

def get_auth_marker(server_port, auth_key):
    return f"witaker:clipboard-server[port={server_port},auth-key='{auth_key}']"
