from traitlets import TraitType
from traitlets.config import Configurable

class HexColorString(TraitType):

    info_text = 'a hex color string.'

    def validate(self, obj, value):
        """Check that its a valid hex string."""
        checks = [
            # Must be a string.
            (isinstance(value, str)),
            # First character must be pound sign
            (value[0] == '#'),
            # Length of hex string must be 3 or 6
            (len(value[1:]) == 3 or len(value[1:]) == 6),
        ]
        # Check if any tests fail.
        if False in checks:
            self.error(obj, value)

        # Else return validated value.
        return value


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
