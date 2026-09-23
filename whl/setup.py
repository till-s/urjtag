# python extension setup script for building urjtag wheel

from setuptools import setup, Extension

libraries = ['urjtag']
# The next line is copied from auto-generated 'setup.py' in urjtag/bindings/python
# 'configure' would substitute the configured libraries; this may have to be hand
# tuned ATM; substitute the libraries configure found...
libraries.extend( w.replace('-l', '') for w in "-lftdi -lusb-1.0  ".split() if w.replace('-l', '') not in libraries )

pre='urjtag/'

setup(name="urjtag",
      version="2021.03",
      description="urJtag Python Bindings",
      packages=['urjtag'],
      # map installation dir [key] -> source dir [value]
      package_dir = {
        'urjtag': pre + 'data',
      },
      # relative to package_dir [value]
      package_data = {
         'urjtag': ['**'],
      },
      ext_modules=[
        Extension("urjtag", [pre + "bindings/python/chain.c", pre + "bindings/python/register.c"],
                  define_macros=[('HAVE_CONFIG_H', None), ('PYMODULE_SET_DATADIR', '"urjtag"')],
                  include_dirs=[pre, pre + 'include'],
                  library_dirs=[pre + 'src/.libs'],
                  libraries=libraries)
     ])
