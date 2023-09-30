from ppy_file_text import StringUtil
from pweb_form_rest import PWebFRConfig
from pweb_form_rest.crud.pweb_request_data import RequestData
from pweb_form_rest.ui.pweb_ui_helper import ssr_ui_render_html_file
from pweb_ssr.common.pweb_ssr_config import PWebSSRConfig
from pweb_ssr.common.pweb_ssr_html_file import PWebSSRHTMLFile


class TableCommon:
    html_file: PWebSSRHTMLFile = PWebSSRHTMLFile()
    request_data: RequestData = RequestData()

    def sortable_header(self, name, display_name, **kwargs):
        if not display_name:
            display_name = StringUtil.human_readable(name)

        icon = PWebSSRConfig.TABLE_SORT_ICON_NAME
        sort_field_key = PWebFRConfig.SORT_FIELD_PARAM_NAME
        sort_order_key = PWebFRConfig.SORT_ORDER_PARAM_NAME
        url_sort_field = self.request_data.get_query_args_value(sort_field_key, None)
        url_sort_order = self.request_data.get_query_args_value(sort_order_key, None)
        sort_fields = {sort_field_key: name, sort_order_key: "asc"}
        if url_sort_field and url_sort_field == name:
            icon = PWebSSRConfig.TABLE_SORT_ASC_ICON_NAME
            order = "asc"
            if url_sort_order == "asc":
                icon = PWebSSRConfig.TABLE_SORT_DESC_ICON_NAME
                order = "desc"
            sort_fields[sort_order_key] = order

        url_info = self.request_data.get_url_info()
        url = self.request_data.add_to_query_params(url_info.relativeURLWithParam, sort_fields)
        params = {
            "display_name": display_name,
            "icon": icon,
            "url": url,
            "icon_class": PWebSSRConfig.TABLE_SORT_ICON_OTHER_CLASS_NAME,
            "link_class": PWebSSRConfig.TABLE_SORT_LINK_CLASS_NAME
        }
        return ssr_ui_render_html_file(self.html_file.sortable_header_html(), params=params)
