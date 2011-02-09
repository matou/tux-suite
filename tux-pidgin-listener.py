#
# Copyright (c) 2011 Matthias Matouesk <matou@taunusstein.net>
# 
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
# 
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
# 

from tuxisalive.api.sh import tux
import re

pattern = "tux:\s*([^<]*)"

def my_func(account, sender, message, conversation, flags):
    if re.findall(pattern, message):
        tux.flippers.onAsync(4)
        tux.mouth.open()
        tospeak = str(re.findall(pattern, message)[0])
        print "tux says: ", tospeak
        tux.tts.speak(tospeak)
        tux.mouth.close()


import dbus, gobject
from dbus.mainloop.glib import DBusGMainLoop
dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
bus = dbus.SessionBus()

bus.add_signal_receiver(my_func,
dbus_interface="im.pidgin.purple.PurpleInterface",
signal_name="ReceivedImMsg")
loop = gobject.MainLoop()
loop.run()
