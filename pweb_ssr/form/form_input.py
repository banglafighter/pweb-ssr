from pweb_ssr.lib.jinja_tag_helper import StandaloneTag


class FormInput(StandaloneTag):
    tags = {"form_input"}

    def render(self, *args, **kwargs):
        return "Working Fine"
