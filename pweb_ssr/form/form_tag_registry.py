from pweb_form_rest import FormField
from pweb_ssr.form.from_input_common import FormInputCommon
from pweb_ssr.lib.jinja_tag_helper import StandaloneTag


form_input_common = FormInputCommon()


class FormInput(StandaloneTag):
    tags = {"form_input"}

    def render(self, field: FormField, *args, **kwargs):
        return form_input_common.get_form_input(field=field, kwargs=kwargs)


class InputError(StandaloneTag):
    tags = {"input_error"}

    def render(self, field: FormField, *args, **kwargs):
        return form_input_common.get_input_error(field=field, kwargs=kwargs)


class ErrorClass(StandaloneTag):
    tags = {"error_class"}

    def render(self, field: FormField, *args, **kwargs):
        return form_input_common.get_error_class(field=field, kwargs=kwargs)


class InputHelp(StandaloneTag):
    tags = {"input_help"}

    def render(self, field: FormField, *args, **kwargs):
        return form_input_common.get_input_help(field=field, kwargs=kwargs)


class MakeChecked(StandaloneTag):
    tags = {"make_checked"}

    def render(self, key, value, *args, **kwargs):
        return form_input_common.get_make_checked(key=key, value=value, kwargs=kwargs)


class MakeSelect(StandaloneTag):
    tags = {"make_select"}

    def render(self, key, value, *args, **kwargs):
        return form_input_common.get_make_select(key=key, value=value, kwargs=kwargs)


class SetValue(StandaloneTag):
    tags = {"set_value"}

    def render(self, value, *args, **kwargs):
        return form_input_common.get_set_value(value=value, kwargs=kwargs)
