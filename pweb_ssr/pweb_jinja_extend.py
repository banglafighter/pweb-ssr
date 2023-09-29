class PWebJinjaExtend:
    _extensions = [
        "pweb_ssr.form.form_tag_registry.FormInput",
        "pweb_ssr.form.form_tag_registry.InputError",
        "pweb_ssr.form.form_tag_registry.ErrorClass",
        "pweb_ssr.form.form_tag_registry.InputHelp",
        "pweb_ssr.form.form_tag_registry.MakeChecked",
        "pweb_ssr.form.form_tag_registry.MakeSelect",
        "pweb_ssr.form.form_tag_registry.SetValue",
    ]

    def register(self, pweb_app):
        self.register_extension(pweb_app)

    def register_extension(self, pweb_app):
        for extension in self._extensions:
            pweb_app.jinja_env.add_extension(extension)
