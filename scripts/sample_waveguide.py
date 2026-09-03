"""Straight waveguide connected to an S-bend, exported to GDS."""

from pathlib import Path

import gdsfactory as gf

gf.gpdk.PDK.activate()

OUTPUTS_DIR = Path(__file__).resolve().parent.parent / "outputs"


def build() -> gf.Component:
    c = gf.Component()

    straight = c << gf.components.straight(length=10)
    sbend = c << gf.components.bend_s(size=(15, 5))

    sbend.connect("o1", straight.ports["o2"])

    c.add_port("o1", port=straight.ports["o1"])
    c.add_port("o2", port=sbend.ports["o2"])

    return c


if __name__ == "__main__":
    component = build()
    OUTPUTS_DIR.mkdir(exist_ok=True)
    gds_path = component.write_gds(OUTPUTS_DIR / "sample_waveguide.gds")
    print(f"Wrote {gds_path}")
    # component.show()  # opens the layout in KLayout, if installed
