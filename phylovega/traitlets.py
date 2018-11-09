from traitlets import TraitType


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


