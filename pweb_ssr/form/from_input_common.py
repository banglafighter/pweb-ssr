from copy import copy
from pweb_form_rest import FormField
from pweb_form_rest.ui.pweb_ui_helper import ssr_ui_render_html_file
from pweb_ssr.common.pweb_ssr_config import PWebSSRConfig
from pweb_ssr.common.pweb_ssr_html_file import PWebSSRHTMLFile


class FormInputCommon:
    html_file: PWebSSRHTMLFile = PWebSSRHTMLFile()

    def dict_to_attribute(self, dictionary: dict, ignore: list = []):
        attributes = ""
        for key in dictionary:
            if key in ignore:
                continue

            if dictionary[key] == True and key != "value":
                attributes += f" {key}"
            elif dictionary[key]:
                attributes += f" {key}='{dictionary[key]}'"
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

    def _get_wrapper_attribute(self, field: FormField, kwargs):
        wrapper_attribute_dict = {}
        concat = None
        if field.inputType == "checkbox" or field.inputType == "radio":
            concat = PWebSSRConfig.CHECKBOX_WRAPPER_CLASS_NAME
        wrapper_class = self.get_kwargs_value(kwargs=kwargs, key="wrapper", default=None, concat=concat)
        if wrapper_class:
            wrapper_attribute_dict["class"] = wrapper_class

        wrapper_id = self.get_kwargs_value(kwargs=kwargs, key="wrapper_id", default=None)
        if wrapper_id:
            wrapper_attribute_dict["id"] = wrapper_id

        return self.dict_to_attribute(dictionary=wrapper_attribute_dict)

    def _get_input_attribute(self, field: FormField, kwargs):
        input_class = PWebSSRConfig.INPUT_CLASS_NAME
        if field.inputType == "select":
            input_class = PWebSSRConfig.SELECT_CLASS_NAME
        elif field.inputType == "checkbox" or field.inputType == "radio":
            input_class = PWebSSRConfig.CHECKBOX_CLASS_NAME

        field.add_attribute("class", self.get_kwargs_value(kwargs=kwargs, key="input_class", concat=input_class))
        field.add_attribute("id", self.get_kwargs_value(kwargs=kwargs, key="input_id"))
        field.add_attribute("name", field.name)

        if field.isError:
            field.add_attribute("class", PWebSSRConfig.INPUT_ERROR_CLASS_NAME)

        if field.placeholder and field.inputType != "select":
            field.add_attribute("placeholder", field.placeholder)

        if field.required:
            field.add_attribute("required", True)

        if field.inputType != "textarea" and field.inputType != "select":
            field.add_attribute("value", field.value)
            field.add_attribute("type", field.inputType)

        return self.dict_to_attribute(field.allAttributes)

    def _get_select_options(self, field: FormField, params):
        if field.inputType != "select" or not field.selectOptions:
            return params

        options = []
        for item in field.selectOptions:
            label = field.selectOptions[item]
            option = {
                "label": label,
                "value": item,
            }
            if field.value and str(field.value) == str(item):
                option['selected'] = True
            elif field.defaultValue and str(field.defaultValue) == str(item):
                option['selected'] = True
            options.append(option)
        params["options"] = options
        return params

    def _set_radio_checkbox_attrs(self, field: FormField):
        if field.inputType != "checkbox" and field.inputType != "radio":
            return field

        if str(field.checked) == str(field.value):
            field.add_attribute("checked", True)
        field.value = f"{field.checked}"
        return field

    def _overwrite_by_kwargs(self, field: FormField, kwargs):
        overwrite_attrs = ["label", "value", "checked", "unchecked"]
        for name in overwrite_attrs:
            if name in kwargs and hasattr(field, name):
                setattr(field, name, kwargs[name])
        return field

    def get_form_input(self, field: FormField, kwargs):
        field = copy(field)
        field = self._overwrite_by_kwargs(field=field, kwargs=kwargs)
        field = self._set_radio_checkbox_attrs(field=field)
        params = {
            "label_required_class": PWebSSRConfig.INPUT_REQUIRED_SIGN_CLASS_NAME,
            "help_message_class": PWebSSRConfig.INPUT_HELP_MESSAGE_CLASS_NAME,
            "error_message_class": PWebSSRConfig.INPUT_ERROR_MESSAGE_CLASS_NAME,
            "wrapper_attributes": self._get_wrapper_attribute(kwargs=kwargs, field=field),
            "input_attributes": self._get_input_attribute(field=field, kwargs=kwargs),
            "field": field
        }

        if field.inputType == "checkbox" or field.inputType == "radio":
            params["label_class"] = PWebSSRConfig.INPUT_LABEL_CHECKBOX_CLASS_NAME
        else:
            params["label_class"] = PWebSSRConfig.INPUT_LABEL_CLASS_NAME

        params = self._get_select_options(field=field, params=params)
        return ssr_ui_render_html_file(self.html_file.form_input_html(), params=params)

    def get_input_error(self, field: FormField, kwargs):
        params = {
            "error_message_class": PWebSSRConfig.INPUT_ERROR_MESSAGE_CLASS_NAME,
            "field": field
        }
        return ssr_ui_render_html_file(self.html_file.error_message_html(), params=params)

    def get_input_help(self, field: FormField, kwargs):
        params = {
            "help_message_class": PWebSSRConfig.INPUT_HELP_MESSAGE_CLASS_NAME,
            "field": field
        }
        return ssr_ui_render_html_file(self.html_file.help_message_html(), params=params)

    def get_error_class(self, field: FormField, kwargs):
        if field.isError:
            return PWebSSRConfig.INPUT_ERROR_CLASS_NAME
        return ""

    def get_make_checked(self, key, value, kwargs):
        if str(key) == str(value):
            return "checked"
        return ""

    def get_make_select(self, key, value, kwargs):
        if str(key) == str(value):
            return "selected"
        return ""

    def get_set_value(self, value, kwargs):
        if value or value == 0:
            return f"value='{value}'"
        return value
