OS specific code
================

| Note, for the following code, you first need to check what the operating system is.


Example OS check
----------------

.. code-block:: python

   from display_server_interactions import DSI

   with DSI() as dsi:
      if dsi.linux:
         """Code for linux"""
      elif dsi.windows:
         """Code for windows"""
      elif dsi.mac:
         """Code for mac"""
      else:
         raise Exception("Your OS is not supported.")

X11/Xorg (GNU/Linux)
--------------------

Get Window xid
^^^^^^^^^^^^^^

.. code-block:: python

   from display_server_interactions import DSI

   with DSI() as dsi:
      window = dsi.get_active_window()
      if dsi.linux:
         print("XID:", window.xid)
      else:
         raise Exception("Your OS is not supported.")

Get Active Window xid
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from display_server_interactions import DSI
   from display_server_interactions.linux import get_active_window_xid

   with DSI() as dsi:
      if dsi.linux:
         print("XID:", get_active_window_xid(dsi.xlib))
      else:
         raise Exception("Your OS is not supported.")

Get Window by xid
^^^^^^^^^^^^^^^^^

.. code-block:: python

   from display_server_interactions import DSI
   from display_server_interactions.linux import Window

   with DSI() as dsi:
      if dsi.linux:
         window = Window(42, dsi.xlib)
      else:
         raise Exception("Your OS is not supported.")
