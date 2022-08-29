from gi.repository import GObject, Eog

class EomKeysPlugin(GObject.Object, Eog.WindowActivatable):
    window = GObject.property(type=Eog.Window)

    def __init__(self):
        GObject.Object.__init__(self)
        self.action_key_pairs = {'win.go-next': 'Return',
                                 'win.go-previous': 'BackSpace',
                                 'win.close': 'Q'}

        self.original_keys_for_action = {}
        app = Eog.Application.get_instance()
        for action,key in self.action_key_pairs.items():
            self.original_keys_for_action[action] = app.get_accels_for_action(action)


    def do_activate(self):
        app = Eog.Application.get_instance()
        for action,key in self.action_key_pairs.items():
            self.extend_action_key(action, key)

    def do_deactivate(self):
        app = Eog.Application.get_instance()
        for action,key in self.action_key_pairs.items():
            self.retract_action_key(action, key)

    def extend_action_key(self, action, key):
        app = Eog.Application.get_instance()
        app.set_accels_for_action(action, [key] + self.original_keys_for_action[action] + [None])

    def retract_action_key(self, action, key):
        app = Eog.Application.get_instance()
        app.set_accels_for_action(action, self.original_keys_for_action[action] + [None])
