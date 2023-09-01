from pweb_ssr.lib.jinja_tag_helper import StandaloneTag


class FormInput(StandaloneTag):
    tags = {"form_input"}

    def render(self, field, *args, **kwargs):
        pass
