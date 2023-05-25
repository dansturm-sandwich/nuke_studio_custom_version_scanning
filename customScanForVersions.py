import hiero.core, hiero.ui 
from PySide2 import QtWidgets, QtCore 
from hiero.core import events 

class customScanForVersions(QtWidgets.QAction): 
    def __init__(self): 
        QtWidgets.QAction.__init__(self, "Custom Scan For Versions", None) 

        self.setShortcut("x")
        self.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.triggered.connect(self.doit)
        
    def doit(result):
        sel = hiero.ui.getTimelineEditor(hiero.ui.activeSequence()).selection()

        for item in sel:
            version = item.currentVersion()
            hiero.ui.ScanForVersions._DoScanForVersions([version], None, True)


scanAct = customScanForVersions()
hiero.ui.mainWindow().addAction(scanAct)

def AddActionToMenu(event): 
    menu = event.menu 
    menu.addAction(scanAct) 

events.registerInterest((events.EventType.kShowContextMenu, events.EventType.kTimeline), AddActionToMenu)