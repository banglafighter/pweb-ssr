class PWebJinjaExtend:
    _extensions = [
        "pweb_ssr.form.form_input.FormInput",
        "pweb_ssr.form.input_common.InputError",
        "pweb_ssr.form.input_common.ErrorClass",
        "pweb_ssr.form.input_common.InputHelp",
        "pweb_ssr.form.input_common.MakeChecked",
        "pweb_ssr.form.input_common.MakeSelect",
        "pweb_ssr.form.input_common.SetValue",
    ]

    def register(self, pweb_app):
        self.register_extension(pweb_app)

    def register_extension(self, pweb_app):
        for extension in self._extensions:
            pweb_app.jinja_env.add_extension(extension)
