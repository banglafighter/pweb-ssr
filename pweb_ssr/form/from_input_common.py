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

    def dict_to_attribute(self, dictionary: dict, ignore: list = []):
        attributes = ""
        for key in dictionary:
            if key in ignore:
                continue

            if dictionary[key] == True:
                attributes += f" {key}"
            elif dictionary[key]:
                attributes += f" {key}={dictionary[key]}"
            attributes = attributes.strip()
        return attributes

    def get_kwargs_value(self, kwargs, key, concat=None, default: any = ""):
        value = None
        if key in kwargs:
            value = kwargs[key]
        if value and concat:
            return f"{value} {concat}".strip()
        elif value:
            return f"{value}".strip()
        elif concat:
            return f"{concat}".strip()
        return default

    def get_form_input(self, field: FormField, kwargs):
        params = {
            "label_class": PWebSSRConfig.INPUT_LABEL_CLASS_NAME,
            "label_required_class": PWebSSRConfig.INPUT_REQUIRED_SIGN_CLASS_NAME,
            "help_message_class": PWebSSRConfig.INPUT_HELP_MESSAGE_CLASS_NAME,
            "error_message_class": PWebSSRConfig.INPUT_ERROR_MESSAGE_CLASS_NAME,
        }

        wrapper_attribute_dict = {}
        wrapper_class = self.get_kwargs_value(kwargs=kwargs, key="wrapper", default=None)
        if wrapper_class:
            wrapper_attribute_dict["class"] = wrapper_class

        wrapper_id = self.get_kwargs_value(kwargs=kwargs, key="wrapper_id", default=None)
        if wrapper_id:
            wrapper_attribute_dict["id"] = wrapper_id

        params["wrapper_attributes"] = self.dict_to_attribute(dictionary=wrapper_attribute_dict)

        input_class = PWebSSRConfig.INPUT_CLASS_NAME
        if field.inputType == "select":
            input_class = PWebSSRConfig.SELECT_CLASS_NAME

        field.add_attribute("class", self.get_kwargs_value(kwargs=kwargs, key="input_class", concat=input_class))
        field.add_attribute("id", self.get_kwargs_value(kwargs=kwargs, key="input_id"))

        if field.isError:
            field.add_attribute("class", PWebSSRConfig.INPUT_ERROR_CLASS_NAME)

        if field.placeholder:
            field.add_attribute("placeholder", field.placeholder)

        if field.required:
            field.add_attribute("required", True)

        if field.inputType != "textarea" and field.inputType != "select":
            field.add_attribute("value", field.value)
            field.add_attribute("type", field.inputType)

        params["input_attributes"] = self.dict_to_attribute(field.allAttributes)
        params["field"] = field
        return ssr_ui_render_html_file(self.form_input_html(), params=params)
