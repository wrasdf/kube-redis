class EventHander:

    def __init__(self):
        self.e = ""

    def onCreated(self, obj):
        print("onCreated ", obj)

    def onDeleted(self, obj):
        print("onDeleted ", obj)

    def onModifed(self, obj):
        print("onModifed ", obj)
