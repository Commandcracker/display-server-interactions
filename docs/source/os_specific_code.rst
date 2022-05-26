OS specific code
================

| Note, for the following code, you first need to check what the operating system is.


Example OS check
----------------

.. code-block:: python

   from dsi import __os_name

   if __os_name == "linux":
      # Code for linux
      pass

   elif __os_name == "windows":
      # Code for windows
      pass

   elif __os_name == "darwin":
      # Code for macosx
      pass

   else:
      # Error out if os is not supported
      raise NotImplementedError("Your OS is not supported.")



X11/Xorg (GNU/Linux)
--------------------

Get Window xid
^^^^^^^^^^^^^^

.. code-block:: python

    from dsi import DSI
    from dsi.linux import Window

    window: Window = DSI.get_active_window()
    print("XID:", window.xid)

Get Active Window xid
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from dsi.linux import get_active_window_xid

    print("XID:", get_active_window_xid())

Get Window by xid
^^^^^^^^^^^^^^^^^

.. code-block:: python

   from dsi.linux import Window

   window = Window(42)
