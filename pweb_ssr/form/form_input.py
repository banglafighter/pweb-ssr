from pweb_form_rest import FormField
from pweb_ssr.lib.jinja_tag_helper import StandaloneTag


class FormInput(StandaloneTag):
    tags = {"form_input"}

    def render(self, field: FormField, *args, **kwargs):
        return "Working Fine"
