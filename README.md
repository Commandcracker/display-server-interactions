# Display Server Interactions

[![PyPI version](https://badge.fury.io/py/display-server-interactions.svg)](https://pypi.org/project/display-server-interactions/)
[![Documentation Status](https://readthedocs.org/projects/display-server-interactions/badge/?version=latest)](https://display-server-interactions.readthedocs.io/en/latest)
[![Downloads](https://pepy.tech/badge/display-server-interactions)](https://pepy.tech/project/display-server-interactions)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/display-server-interactions)](https://pypi.org/project/display-server-interactions/)

[![License](https://img.shields.io/github/license/Commandcracker/display-server-interactions)](https://github.com/Commandcracker/display-server-interactions/blob/main/LICENSE.txt)
[![GitHub stars](https://img.shields.io/github/stars/Commandcracker/display-server-interactions)](https://github.com/Commandcracker/display-server-interactions/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Commandcracker/display-server-interactions)](https://github.com/Commandcracker/display-server-interactions/network)
[![GitHub issues](https://img.shields.io/github/issues/Commandcracker/display-server-interactions)](https://github.com/Commandcracker/display-server-interactions/issues)

DSI allows you to perform basic interactions on your display server, like screenshotting a window or sending input to it.
Currently, DSI only supports X11/Xorg (GNU/Linux) but it aims to be cross-platform.

**WARNING: Please Do not use DSI in production, because it's currently in development!**

## Quick overview

Look at the [documentation](https://display-server-interactions.readthedocs.io/en/latest/) for moor information's

### Get a window

```python
from display_server_interactions import DSI
window = DSI.get_active_window()
```

### Get basic window information

```python
print("Active window: ")
print("\tName: {}".format(window.name))
print("\tPID: {}".format(window.pid))
```

### Take a screenshot of the window

```python
import cv2
import numpy as np

img = np.array(window.get_image())
cv2.imshow(f'Screenshot of "{window.name}"', img)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```

### Sending keys to a window

```python
window.send_str("Hello World")
```

### Move the mouse pointer

```python
window.warp_pointer(x=42, y=73)
```

### Sending mouse clicks

```python
window.send_mouse_click(x=42, y=73)
```
