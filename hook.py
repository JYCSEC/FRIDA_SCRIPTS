from __future__ import print_function
import frida
import sys

session = frida.attach("app_to_hook")
script = session.create_script("""
Interceptor.attach(ptr("%s"), {
    onEnter: function(args) {
        send(args[0].toInt32());
        args[0] = ptr("1337");
        }
    });
""" % int(sys.argv[1], 16))
def on_message(message, data):
    print(message)
script.on('message', on_message)
script.load()
sys.stdin.read()

