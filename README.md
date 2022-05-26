# Display Server Interactions

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

### Sending mouse clicks

```python
window.send_mouse_click(100, 100)
```

### Move the mouse pointer

```python
window.warp_pointer(x=100, y=100)
```
