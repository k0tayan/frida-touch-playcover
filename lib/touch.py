from dataclasses import dataclass

import frida


class TouchType:
    UNDEFINED = -1
    RELEASE = 0
    PRESS = 1
    MOVE = 2


@dataclass
class SimulateTouch:
    tid: int
    x: int
    y: int
    ttype: int = TouchType.RELEASE


class FridaTouch:
    def __init__(self, host: str = "localhost", port: int = 27042) -> None:
        self.host = host
        self.port = port
        self.device = frida.get_device_manager().add_remote_device(
            f"{self.host}:{self.port}"
        )
        self.session = self.device.attach("Gadget")
        with open("scripts/_index.js", "r", encoding="utf-8") as f:
            js = f.read()
        self.script = self.session.create_script(js)
        self.script.load()

    def post_simulate_touch(self, touch: SimulateTouch):
        self.script.post(
            {
                "type": "in",
                "tid": touch.tid,
                "x": touch.x,
                "y": touch.y,
                "ttype": touch.ttype,
            }
        )
