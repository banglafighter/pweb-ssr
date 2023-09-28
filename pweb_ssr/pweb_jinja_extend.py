class PWebJinjaExtend:
    _extensions = [
        "pweb_ssr.form.form_input.FormInput"
    ]

    def register(self, pweb_app):
        self.register_extension(pweb_app)

    def register_extension(self, pweb_app):
        for extension in self._extensions:
            pweb_app.jinja_env.add_extension(extension)
