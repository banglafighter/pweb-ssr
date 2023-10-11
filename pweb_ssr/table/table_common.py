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

    def _page_number_calculate(self, current_page: int, total_page: int):
        delta = 2
        left = current_page - delta
        right = current_page + delta + 1
        range_list = []
        range_with_dots = []
        temp = 0

        for i in range(1, total_page + 1):
            if i == 1 or i == total_page or left <= i < right:
                range_list.append(i)

        for i in range_list:
            if temp:
                if (i - temp) == 2:
                    range_with_dots.append(temp + 1)
                elif (i - temp) != 1:
                    range_with_dots.append("...")
            range_with_dots.append(i)
            temp = i
        return range_with_dots

    def _prepare_pagination_link(self, current_page: int, total_page: int):
        pagination_item = self._page_number_calculate(current_page, total_page)
        pagination_details = []
        url_info = self.request_data.get_url_info()
        for pagination in pagination_item:
            selected = False
            url = "#"
            if pagination == current_page:
                selected = True
            elif pagination != "...":
                url = self.request_data.add_to_query_params(url_info.relativeURLWithParam, {PWebFRConfig.PAGE_PARAM_NAME: pagination})
            pagination_details.append({
                "text": pagination,
                "url": url,
                "selected": selected,
            })
        return pagination_details

    def pagination(self, current_page: int, total_page: int, **kwargs):
        if total_page <= 1:
            return ""
        params = {
            "prev": "",
            "pages": self._prepare_pagination_link(current_page, total_page),
            "next": "",
            "item_per_page_name": PWebFRConfig.ITEM_PER_PAGE_PARAM_NAME,
            "item_per_page_options": PWebSSRConfig.TABLE_ITEM_PER_PAGE_OPTIONS,
            "item_per_page_selected": self.request_data.get_query_args_value(PWebFRConfig.ITEM_PER_PAGE_PARAM_NAME, PWebFRConfig.TOTAL_ITEM_PER_PAGE),
        }
        return ssr_ui_render_html_file(self.html_file.pagination_html(), params=params)

    def search_name_value(self):
        value = self.request_data.get_query_args_value(PWebFRConfig.SEARCH_FIELD_PARAM_NAME, "#")
        if not value or value == "#":
            value = ""
        return "name='" + PWebFRConfig.SEARCH_FIELD_PARAM_NAME + "' value='" + value + "'"
