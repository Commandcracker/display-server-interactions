OS specific code
================

| Note, for the following code, you first need to check what the operating system is.


Example OS check
----------------

.. code-block:: python

   from display_server_interactions import DSI

   if DSI.linux:
      """Code for linux"""
   elif DSI.windows:
      """Code for windows"""
   elif DSI.mac:
      """Code for mac"""
   else:
      raise Exception("Your OS is not supported.")

X11/Xorg (GNU/Linux)
--------------------

Get Window xid
^^^^^^^^^^^^^^

.. code-block:: python

    from display_server_interactions import DSI
    from display_server_interactions.linux import Window

    window: Window = DSI.get_active_window()
    print("XID:", window.xid)

Get Active Window xid
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from display_server_interactions.linux import get_active_window_xid

    print("XID:", get_active_window_xid())

Get Window by xid
^^^^^^^^^^^^^^^^^

.. code-block:: python

   from display_server_interactions.linux import Window

   window = Window(42)
