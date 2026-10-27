import time

from qt.core import QIcon, QTimer

from calibre.gui2.actions import InterfaceAction


class RestartServersAction(InterfaceAction):
    name = 'Restart Servers'
    action_spec = ('Restart servers', None, 'Restart the Content server and the wireless device connection without dialogs', None)
    action_type = 'current'

    def genesis(self):
        self.qaction.setIcon(QIcon.ic('view-refresh.png'))
        self.qaction.triggered.connect(self.restart)
        self.busy = False

    def restart(self):
        if self.busy:
            return
        self.busy = True
        self.qaction.setEnabled(False)
        self.gui.status_bar.show_message('Restarting servers...')
        # Call the device manager directly: the "Disable autostart" question lives in the Connect/share menu
        dm = self.gui.device_manager
        if dm.is_running('smartdevice'):
            dm.stop_plugin('smartdevice')
        if self.gui.content_server is not None:
            self.gui.content_server.stop()
        self.deadline = time.monotonic() + 60
        self.wait_for_content_server()

    def wait_for_content_server(self):
        cs = self.gui.content_server
        if cs is not None and getattr(cs, 'is_running', False) and time.monotonic() < self.deadline:
            QTimer.singleShot(100, self.wait_for_content_server)
            return
        self.gui.content_server = None
        self.start_all()

    def start_all(self):
        errors = []
        try:
            self.gui.start_content_server()
        except Exception as e:
            errors.append(f'Content server: {e}')
        # Same start_plugin the "Smart device control" OK button calls, using the saved settings
        msg = self.gui.device_manager.start_plugin('smartdevice')
        if msg:
            errors.append(f'Wireless: {msg}')
        self.gui.iactions['Connect Share'].set_smartdevice_action_state()
        self.busy = False
        self.qaction.setEnabled(True)
        if errors:
            from calibre.gui2 import error_dialog
            error_dialog(self.gui, 'Restart servers', 'Restart failed', det_msg='\n'.join(errors), show=True)
        else:
            dm = self.gui.device_manager
            port = dm.get_option('smartdevice', 'port_number')
            self.gui.status_bar.show_message(f'Servers restarted: Content server and wireless device connection (port {port})', 8000)
