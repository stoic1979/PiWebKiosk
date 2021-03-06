#!/usr/bin/env python

#
# Script for showing webbrowser in GTK on respberry pi
#
# Copyright (C) 2017  Navjot Singh <weavebytes@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
import gtk
import webkit
import gobject
import sys, warnings


def on_webkit_webframe_scrollbars_policy_changed(widget):
    return True # to stop propagation


url = "http://0.0.0.0:5000/"
 
width=800
height=480
 
win = gtk.Window()
webview = webkit.WebView()

wf = webview.get_main_frame()
wf.connect("scrollbars-policy-changed", on_webkit_webframe_scrollbars_policy_changed)

sw = gtk.ScrolledWindow()
sw.set_policy(gtk.POLICY_NEVER, gtk.POLICY_NEVER)
 
win.set_size_request(width,height)
win.set_decorated(False)
win.connect("destroy", lambda q: gtk.main_quit())
 
webview.load_uri(url)
 
toolbar = gtk.Toolbar()
 
vbox = gtk.VBox(False, 0)
vbox.pack_start(toolbar, False, True, 0)
 
vbox.add(sw)
win.add(vbox)
sw.add(webview)
 
win.maximize()
win.show_all()

gtk.main()
