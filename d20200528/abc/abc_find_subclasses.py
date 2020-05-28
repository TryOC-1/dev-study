import abc  # noqa

import abc_subclass  # noqa
from abc_base import PluginBase

# import abc_register

for sc in PluginBase.__subclasses__():
    print(sc.__name__)
