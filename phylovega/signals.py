from .marks import TreeMarkOptions


class TreeSignals(TreeMarkOptions):

    def vega_signal(self, name, value):
        inp, key = self.vega_input(name, value)
        if key == 'signal':
            method = getattr(self, '{}_spec'.format(inp))
            return method(name, value)
        return None

    def range_spec(self, name, value):
        return {
            'name': name,
            'bind': {
                'input': 'range',
                'min': value[0],
                'max': value[1],
                #'step': 1
            }
        }

    def menu_spec(self, name, value):
        return {
            'name': name,
            'bind': {
                'input': 'select',
                'options': value
            }
        }

    def color_spec(self, name, value):
        return {
            'name': name,
            'value': '#000',
            'bind': {
                'input': 'color'
            }
        }

    def get_spec(self):
        spec = {'signals': []}
        for name in TreeMarkOptions.class_own_traits():
            trait = getattr(self, name)
            stuff = self.vega_signal(name, trait)
            if stuff is not None:
                spec['signals'].append(stuff)
        return spec
