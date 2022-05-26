# DSI (Display Server Interactions)

DSI allows you to perform basic interactions on your display server, like screenshotting a window or sending input to it.
Currently DSI only supports X11/Xorg (GNU/Linux) but it aims to be cross-platform.

## Usage

look at the [documentation]("https://dsi.readthedocs.io/en/latest/) for moor help

```python
from dsi import DSI

window = DSI.get_active_window()

print("Active window: ")
print("\tName: {}".format(window.name))
print("\tPID: {}".format(window.pid))
```
