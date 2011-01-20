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
