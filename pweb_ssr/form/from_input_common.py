import pathlib
from ppy_file_text import FileUtil
from pweb_form_rest import FormField
from pweb_form_rest.ui.pweb_ui_helper import ssr_ui_render_html_file
from pweb_ssr.common.pweb_ssr_config import PWebSSRConfig


class FormInputCommon:
    def get_html_path(self):
        if PWebSSRConfig.SSR_HTML_PATH:
            return PWebSSRConfig.SSR_HTML_PATH
        path = pathlib.Path(__file__).parent.parent.resolve()
        return FileUtil.join_path(path, "html")

    def form_input_html(self):
        return FileUtil.join_path(self.get_html_path(), "form-input.html")

    def error_message_html(self):
        return FileUtil.join_path(self.get_html_path(), "error-message.html")

    def pagination_html(self):
        return FileUtil.join_path(self.get_html_path(), "pagination.html")

    def sortable_header_html(self):
        return FileUtil.join_path(self.get_html_path(), "sortable-header.html")

    def get_form_input(self, field: FormField, kwargs):
        return ssr_ui_render_html_file(self.form_input_html())
