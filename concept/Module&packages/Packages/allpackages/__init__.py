from . import package2

# Optional: Block direct import of package1
__all__ = ['package2']  # This controls what shows up in `from allpackages import *`