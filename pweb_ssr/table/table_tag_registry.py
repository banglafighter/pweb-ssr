from pweb_ssr.lib.jinja_tag_helper import StandaloneTag
from pweb_ssr.table.table_common import TableCommon

table_common = TableCommon()


class SortableHeader(StandaloneTag):
    tags = {"sortable_header"}

    def render(self, name, display_name=None, *args, **kwargs):
        return table_common.sortable_header(name=name, display_name=display_name, kwargs=kwargs)


class Pagination(StandaloneTag):
    tags = {"pagination"}

    def render(self, current_page: int, total_page: int, *args, **kwargs):
        return table_common.pagination(current_page=current_page, total_page=total_page, kwargs=kwargs)


class SearchNameValue(StandaloneTag):
    tags = {"search_name_value"}

    def render(self, *args, **kwargs):
        return table_common.search_name_value()
