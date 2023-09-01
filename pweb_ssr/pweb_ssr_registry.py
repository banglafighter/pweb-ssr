from pweb import PWebComponentRegister
from pweb_ssr.pweb_jinja_extend import PWebJinjaExtend


class PWebSSRRegistry(PWebComponentRegister):

    def register_model(self, pweb_db) -> list:
        pass

    def register_controller(self, pweb_app):
        pass

    def run_on_start(self, pweb_app):
        PWebJinjaExtend().register(pweb_app)
