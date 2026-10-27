from calibre.customize import InterfaceActionBase

load_translations()


class RestartServersPlugin(InterfaceActionBase):
    name = 'Restart Servers'
    description = _('Restart the Content server and the wireless device connection with one click and no dialogs')
    supported_platforms = ['windows', 'osx', 'linux']
    author = 'Daniel Hernández'
    version = (0, 1, 0)
    minimum_calibre_version = (7, 0, 0)
    actual_plugin = 'calibre_plugins.restart_servers.ui:RestartServersAction'
