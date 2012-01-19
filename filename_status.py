import sublime_plugin


class FilenameStatusCommand(sublime_plugin.WindowCommand):

    def set_filename_status(self, view, status_key):
        filename = view.file_name()

        if filename is None:
            view.erase_status(status_key)
        else:
            view.set_status(status_key, filename)

    def run(self):
        # Items in the status bar are ordered alphabetically, so the key used
        # will determine the placement of the filename.
        view = self.window.active_view()
        status_key = view.settings().get('filename_status_key', 'filename')

        if view.get_status(status_key):
            view.erase_status(status_key)
        else:
            self.set_filename_status(view, status_key)