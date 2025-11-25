#!/usr/bin/env python3
import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Vte", "2.91")
from gi.repository import Gtk, Vte, GLib
from gi.repository import Gtk, Vte, GLib, Gdk


class MyTerminalWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="My VTE Terminal")
        self.set_default_size(900, 500)

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.vbox)

        menubar = Gtk.MenuBar()
        filemenu = Gtk.Menu()
        file_item = Gtk.MenuItem(label="File")
        file_item.set_submenu(filemenu)

        new_tab = Gtk.MenuItem(label="New Tab")
        new_tab.connect("activate", self.on_new_tab)
        filemenu.append(new_tab)

        menubar.append(file_item)
        self.vbox.pack_start(menubar, False, False, 0)

        self.notebook = Gtk.Notebook()
        self.vbox.pack_start(self.notebook, True, True, 0)

        self.add_terminal_tab()

    def add_terminal_tab(self):
        term = Vte.Terminal()

        term.set_color_background(Gdk.RGBA(0, 0, 0, 1))      # black
        term.set_color_foreground(Gdk.RGBA(0, 1, 0, 1))      # green


        term.spawn_async(
            Vte.PtyFlags.DEFAULT,                             # pty flags
            GLib.get_home_dir(),                              # working directory
            ["/bin/bash", "-c", "bash --login"],              # argv MUST be a list
            [],                                               # envv MUST be a list
            GLib.SpawnFlags.DEFAULT,                          # spawn flags
            None,                                             # child setup
            None,                                             # child setup data
            -1,                                               # timeout
            None,                                             # cancellable
            None,                                             # callback
            None                                              # user data
        )


        scrolled = Gtk.ScrolledWindow()
        scrolled.add(term)

        label = Gtk.Label("shell")
        page = self.notebook.append_page(scrolled, label)
        self.notebook.set_current_page(page)
        term.grab_focus()

    def on_new_tab(self, widget):
        self.add_terminal_tab()

win = MyTerminalWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
