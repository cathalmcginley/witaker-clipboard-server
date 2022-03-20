import multiprocessing
import xerox

class AuthorizedClipboardUtilException(Exception):
    def __init__(self, message):
        super().__init__(message)

class AuthorizedClipboardUtil:

    def __init__(self, session_key):
        self.session_key = session_key
        self.queue = multiprocessing.Queue()

    def copy_text_to_clipboard(self, auth_key, text):
        if (auth_key == self.session_key):
            xerox.copy(text)
            self.queue.put(text)
        else:
            print(self.session_key)
            raise AuthorizedClipboardUtilException(f"Cannot copy text '{text}' to clipboard; auth key '{auth_key}' is invalid ({self.session_key})")


    def paste_text_from_clipboard(self, auth_key):
        if (auth_key == self.session_key):
            return xerox.paste()
        else:
            raise AuthorizedClipboardUtilException(f"Cannot paste text from clipboard; auth key '{auth_key}' is invalid")




    