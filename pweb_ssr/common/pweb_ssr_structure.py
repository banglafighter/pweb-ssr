class SSRTemplateAssets:
    name: str = None
    import_name: str = None
    static_folder: str = None
    static_url_path: str = None
    template_folder: str = None
    url_prefix: str = "/"

    def __init__(
            self,
            name: str,
            import_name: str,
            static_folder: str,
            static_url_path: str,
            template_folder: str,
            url_prefix: str | None = None,
    ):
        self.name = name
        self.import_name = import_name
        self.static_folder = static_folder
        self.static_url_path = static_url_path
        self.template_folder = template_folder
        if url_prefix:
            self.url_prefix = url_prefix
