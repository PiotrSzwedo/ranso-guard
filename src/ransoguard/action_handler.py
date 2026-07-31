def _callback_property(name):

    private_name = f"_{name}"

    def getter(self):
        return getattr(self, private_name)

    def setter(self, value):
        if not callable(value):
            raise TypeError(
                "Handler must be callable"
            )

        setattr(self, private_name, value)

    return property(getter, setter)

class ActionHandler:
    def __init__(self, on_file_created=None, on_file_deleted=None, on_file_modified=None, on_file_moved=None):
        self._on_file_created = on_file_created
        self._on_file_deleted = on_file_deleted
        self._on_file_modified = on_file_modified
        self._on_file_moved = on_file_moved


    on_file_created = _callback_property(
        "on_file_created"
    )

    on_file_deleted = _callback_property(
        "on_file_deleted"
    )

    on_file_modified = _callback_property(
        "on_file_modified"
    )

    on_file_moved = _callback_property(
        "on_file_moved"
    )


