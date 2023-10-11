from pweb_ssr.common.pweb_ssr_init import PWebSSRInit


class PWebJinjaExtend:
    _global_variables = {
        "pweb_app_name": PWebSSRInit.get_app_name(),
    }

    _extensions = [
        "pweb_ssr.form.form_tag_registry.FormInput",
        "pweb_ssr.form.form_tag_registry.InputError",
        "pweb_ssr.form.form_tag_registry.ErrorClass",
        "pweb_ssr.form.form_tag_registry.InputHelp",
        "pweb_ssr.form.form_tag_registry.MakeChecked",
        "pweb_ssr.form.form_tag_registry.MakeSelect",
        "pweb_ssr.form.form_tag_registry.SetValue",

        "pweb_ssr.table.table_tag_registry.SortableHeader",
        "pweb_ssr.table.table_tag_registry.Pagination",
        "pweb_ssr.table.table_tag_registry.SearchNameValue",
    ]

    def register(self, pweb_app):
        self.register_extension(pweb_app)
        self.register_global_variable(pweb_app)

    def register_extension(self, pweb_app):
        for extension in self._extensions:
            pweb_app.jinja_env.add_extension(extension)

    def register_global_variable(self, pweb_app):
        if pweb_app and pweb_app.jinja_env and pweb_app.jinja_env.globals:
            for method in self._global_variables:
                if method not in pweb_app.jinja_env.globals:
                    pweb_app.jinja_env.globals[method] = self._global_variables[method]
