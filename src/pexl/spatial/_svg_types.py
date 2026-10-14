"""Small callback aliases shared by SVG drawing helpers; no runtime model."""

from collections.abc import Callable
from xml.etree.ElementTree import Element

ElementFactory = Callable[..., Element]
TextWriter = Callable[..., None]
CoordinateMap = Callable[[float], float]
