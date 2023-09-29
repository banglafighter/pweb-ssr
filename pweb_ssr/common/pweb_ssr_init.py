from flask import Blueprint
import pweb_ssr.common.pweb_ssr_config
from application.config.app_config import Config
from ppy_common import ObjectHelper
from pweb_ssr import SSRTemplateAssets
from pweb_ssr.common.pweb_ssr_config import PWebSSRConfig


class PWebSSRInit:

    @staticmethod
    def init_default_template_assets(pweb_app):
        if PWebSSRConfig.DEFAULT_TEMPLATE_ASSETS and isinstance(PWebSSRConfig.DEFAULT_TEMPLATE_ASSETS, SSRTemplateAssets):
            ssr_template_assets = PWebSSRConfig.DEFAULT_TEMPLATE_ASSETS
            pweb_app.register_blueprint(Blueprint(
                name=ssr_template_assets.name,
                import_name=ssr_template_assets.import_name,
                static_folder=ssr_template_assets.static_folder,
                static_url_path=ssr_template_assets.static_url_path,
                template_folder=ssr_template_assets.template_folder,
                url_prefix=ssr_template_assets.url_prefix,
            ))

    @staticmethod
    def merge_config(config):
        ObjectHelper.copy_config_property(config, pweb_ssr.common.pweb_ssr_config.PWebSSRConfig)

    @staticmethod
    def get_app_name():
        return Config.APP_NAME
