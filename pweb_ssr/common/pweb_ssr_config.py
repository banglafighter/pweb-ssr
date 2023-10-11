from pweb_ssr.common.pweb_ssr_structure import SSRTemplateAssets


class PWebSSRConfig:
    DEFAULT_TEMPLATE_ASSETS: SSRTemplateAssets = None
    SSR_HTML_PATH: str = None

    # Form Input HTML Class Name
    INPUT_LABEL_CLASS_NAME = "form-label"
    INPUT_LABEL_CHECKBOX_CLASS_NAME = "form-check-label"
    INPUT_REQUIRED_SIGN_CLASS_NAME = "text-danger me-1"
    INPUT_CLASS_NAME = "form-control"
    CHECKBOX_CLASS_NAME = "form-check-input"
    CHECKBOX_WRAPPER_CLASS_NAME = "form-check"
    SELECT_CLASS_NAME = "form-select"
    INPUT_ERROR_CLASS_NAME = "is-invalid"
    INPUT_ERROR_MESSAGE_CLASS_NAME = "invalid-feedback"
    INPUT_HELP_MESSAGE_CLASS_NAME = "form-text"

    # Table Related Class
    TABLE_SORT_ICON_NAME = "fa-sort"
    TABLE_SORT_ASC_ICON_NAME = "fa-sort-down"
    TABLE_SORT_DESC_ICON_NAME = "fa-sort-up"
    TABLE_SORT_ICON_OTHER_CLASS_NAME = "me-1 fas"
    TABLE_SORT_LINK_CLASS_NAME = "text-decoration-none"
    TABLE_ITEM_PER_PAGE_OPTIONS: str = [25, 50, 100, 200, 500]
