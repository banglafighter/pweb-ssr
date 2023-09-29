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

    def render(self, *args, **kwargs):
        return "Working Fine"


class ErrorClass(StandaloneTag):
    tags = {"error_class"}

    def render(self, *args, **kwargs):
        return "Working Fine"


class InputHelp(StandaloneTag):
    tags = {"input_help"}

    def render(self, *args, **kwargs):
        return "Working Fine"


class MakeChecked(StandaloneTag):
    tags = {"make_checked"}

    def render(self, *args, **kwargs):
        return "Working Fine"


class MakeSelect(StandaloneTag):
    tags = {"make_select"}

    def render(self, *args, **kwargs):
        return "Working Fine"


class SetValue(StandaloneTag):
    tags = {"set_value"}

    def render(self, *args, **kwargs):
        return "Working Fine"
