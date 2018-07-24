#From frida.de/docs/installation
#Gets process information from 'cat' in Linux
#Don't forget sudo sysctl kernel.yama.ptrace_scope=0
#Work on copies, not base files

import frida

def on_message(message, data):
    print("[on_message] message:", message, "data:", data)

session = frida.attach("cat")

script = session.create_script("""'strict';

rpc.exports.enumerateModules = function () {
    return Process.enumerateModulesSync();
};
""")
script.on("message", on_message)
script.load()

print([m["name"] for m in script.exports.enumerate_modules()])
