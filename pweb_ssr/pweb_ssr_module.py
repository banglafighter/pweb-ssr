from pweb import PWebComponentRegister, PWebModuleDetails
from pweb_ssr.common.pweb_ssr_init import PWebSSRInit
from pweb_ssr.pweb_jinja_extend import PWebJinjaExtend


class PWebSSRModule(PWebComponentRegister):

    def app_details(self) -> PWebModuleDetails:
        return PWebModuleDetails(system_name="pweb-ssr", display_name="PWeb SSR Module")

    def run_on_cli_init(self, pweb_app, config):
        PWebSSRInit.merge_config(config=config)

    def register_model(self, pweb_db) -> list:
        pass

    def register_controller(self, pweb_app):
        pass

    def run_on_start(self, pweb_app, config):
        PWebSSRInit.merge_config(config=config)
        PWebSSRInit.init_default_template_assets(pweb_app)
        PWebJinjaExtend().register(pweb_app)
