import pathlib
from ppy_file_text import FileUtil
from pweb_ssr.common.pweb_ssr_config import PWebSSRConfig


class PWebSSRHTMLFile:
    def get_html_path(self):
        if PWebSSRConfig.SSR_HTML_PATH:
            return PWebSSRConfig.SSR_HTML_PATH
        path = pathlib.Path(__file__).parent.parent.resolve()
        return FileUtil.join_path(path, "html")

    def form_input_html(self):
        return FileUtil.join_path(self.get_html_path(), "form-input.html")

    def error_message_html(self):
        return FileUtil.join_path(self.get_html_path(), "error-message.html")

    def help_message_html(self):
        return FileUtil.join_path(self.get_html_path(), "help-message.html")

    def pagination_html(self):
        return FileUtil.join_path(self.get_html_path(), "pagination.html")

    def sortable_header_html(self):
        return FileUtil.join_path(self.get_html_path(), "sortable-header.html")
