import re
from ansible.plugins.callback import CallbackBase

class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'mask_ip_callback'

    def v2_runner_on_ok(self, result):
        host = self._mask_ip(result._host.get_name())
        self._display.display(f"changed: [{host}]")

    def v2_runner_on_changed(self, result):
        host = self._mask_ip(result._host.get_name())
        self._display.display(f"changed: [{host}]")

    def v2_runner_on_failed(self, result, ignore_errors=False):
        host = self._mask_ip(result._host.get_name())
        self._display.display(f"failed: [{host}]")

    def v2_runner_on_unreachable(self, result):
        host = self._mask_ip(result._host.get_name())
        self._display.display(f"unreachable: [{host}]")

    def _mask_ip(self, host):
        return re.sub(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', 'XXX.XXX.XXX.XXX', host)
