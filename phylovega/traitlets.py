from traitlets import TraitType
from traitlets.config import Configurable


class VegaMenuOption(TraitType):

    info_text = 'a string or list of strings for menu dropdown'

    def validate(self, obj, value):
        if isinstance(value, str):
            return value
        elif isinstance(value, list):
            return value
        self.error(obj, value)


class VegaRangeOption(TraitType):

    info_text = 'an integer or a tuple of integers for a slider range.'

    def validate(self, obj, value):
        if isinstance(value, int) or isinstance(value, float):
            return value
        if isinstance(value, tuple):
            if len(value) == 2:
                if all(
                    (isinstance(value[0], int),
                     isinstance(value[1], int))):
                    if value[0] < value[1]:
                        return value
        self.error(obj, value)


class VegaColorOption(TraitType): 

    info_text = 'a hex-string color string or "choose" for a color picker widget.'

    def validate(self, obj, value):
        checks = [
            # Must be a string.
            (isinstance(value, str)),
            # First character must be pound sign
            (value[0] == '#'),
            # Length of hex string must be 3 or 6
            (len(value[1:]) == 3 or len(value[1:]) == 6),
        ]
        if all(checks):
            return value
        elif value == '?':
            return value
        self.error(obj, value)


class VegaConfigurable(Configurable):
    """Class hack to fix some problems I encountered with traitlets configurable.
    """
    def __init__(self, config=None, **kwargs):
        super(VegaConfigurable, self).__init__(config=config, **kwargs)
        
        for name, value in config.items():
            try: 
                setattr(self, name, value)
            except AttributeError: 
                pass

    def vega_input(self, name, value):
        """Given a Trait, determine the type of option it is and
         whether to make it a signal
        """
        if value == '?':
            # Color picker
            return ('color', 'signal')
        if isinstance(value, str):
            if value[0] == '#':
                # Color string
                return ('color', 'value')
            else:
                # Column from data
                return ('menu', 'field')
        if type(value) in [int, float]:
            return ('range', 'value')
            
        if isinstance(value, tuple):
            return ('range', 'signal')

        if isinstance(value, list):
            return ('option', 'signal')

        raise Exception("Invalid type to vega-size")
