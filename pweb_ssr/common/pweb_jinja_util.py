class PWebJinjaUtil:

    @staticmethod
    def register_global_variable(pweb_app, variables: dict):
        if pweb_app and pweb_app.jinja_env and pweb_app.jinja_env.globals:
            for variable in variables:
                if variable not in pweb_app.jinja_env.globals:
                    pweb_app.jinja_env.globals[variable] = variables[variable]
