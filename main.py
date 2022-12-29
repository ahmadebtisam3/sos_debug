#!/bin/python3

import sys


from generate_debug import generate_debug_report
from plugins import get_plugins


all_plugins = {plugin.__name__: plugin() for plugin in get_plugins()}


if __name__ == "__main__":
    plugins_obj = []
    plugins_args = sys.argv[1:]
    if plugins_args:
        for plugin_name in plugins_args:
            if plugin := all_plugins.get(plugin_name):
                plugins_obj.append(plugin)
            else:
                raise ValueError(f"Invalid plugin {plugin_name}. Plugin on this name is not registered")
    else:
        plugins_obj.extend(all_plugins.values())
    folder = generate_debug_report(plugins_obj)
    print("debug is generated at: ", folder)
