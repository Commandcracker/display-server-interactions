Getting a Window
================

| Be aware that all of this ways of getting a window can return **None**.
| So you might want to check if the window is **None** before doing anything with it.

Example None check
------------------

.. code-block:: python

    if window is None:
        exit("Window not found!")

Get currently active window
---------------------------

.. code-block:: python

    from dsi import DSI

    window = DSI.get_active_window()

Get a window by its name
------------------------

.. code-block:: python

    from dsi import DSI

    window = DSI.get_window_by_name("Funny Window Name")

Get window by PID
-----------------

.. code-block:: python

    from dsi import DSI

    window = DSI.get_window_by_pid(42)
