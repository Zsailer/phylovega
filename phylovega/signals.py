

def get_signal_specification(
    length_slider=None,
    height_slider=None,
    ):
    """
    """
    signals = []

    if length_slider is not None:
        slider1 = get_length_slider(
            min=length_slider[0],
            max=length_slider[1],
            step=length_slider[2]
        )
        signals.append(slider1)

    if height_slider is not None:
        slider2 = get_height_slider(
            min=height_slider[0],
            max=height_slider[1],
            step=height_slider[2]
        )
        signals.append(slider2)

    specification = dict(
        signals=signals
    )
    return specification


def get_height_slider(
        min=0,
        max=500,
        step=50,
    ):
    """
    """
    value = int((max-min)/2)
    bind = dict(
        input="range",
        min=min,
        max=max,
        step=step
    )
    specification = dict(
        name="height_slider",
        value=value,
        bind=bind,
    )
    return specification


def get_length_slider(
        min=0,
        max=500,
        step=50,
    ):
    """
    """
    value = int((max-min)/2)
    bind = dict(
        input="range",
        min=min,
        max=max,
        step=step
    )
    specification = dict(
        name="length_slider",
        value=value,
        bind=bind,
    )
    return specification
