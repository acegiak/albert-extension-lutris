# -*- coding: utf-8 -*-

"""
Lutris launcher - List and launch Lutris games
"""

import subprocess
from collections import namedtuple
from shutil import which
import sqlite3
from os.path import expanduser
from albertv0 import *

# Window = namedtuple("Lutris", ["wid", "desktop", "wm_class", "host", "wm_name"])

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Lutris Launcher"
__version__ = "1.0"
__author__ = "Ash McAllan"
__dependencies__ = []
home = expanduser("~")

def handleQuery(query):
    
    conn = sqlite3.connect(home+"/.local/share/lutris/pga.db")
    
    results = []
    c = conn.cursor()
    if len(query.string) > 0:
        for row in c.execute("SELECT * FROM games where name like ?;",["%"+query.string+"%"]):
            ex = ["lutris","lutris:rungame/"+row[2]]
            info(ex)
            results.append(Item(id=row[16],
                                icon=iconLookup("lutris_"+row[2]),
                                text=row[1],
                                subtext="lutris - "+str(row[3]),
                                actions=[
                                    ProcAction(text="Launch",commandline=ex)]))
        c.close()
        return results
    c.close()
