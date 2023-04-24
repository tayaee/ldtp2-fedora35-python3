This is a fork of https://github.com/ldtp/ldtp2, and an effort trying to make it run on VirtualBox 6 + Fedora 35 + Python 3.10.

  * sudo dnf install -y python3-wheel
  * sudo dnf install -y gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel tk-devel git python3-cairo-devel cairo-gobject-devel gobject-introspection-devel
  * /usr/bin/python -m venv venv
  * . venv/bin/activate
  * python -m pip install --upgrade pip
  * (cd venv/lib/python3.10/site-packages; ln -s /usr/lib/python3.10/site-packages/pyatspi)
  * pip install twisted
  * pip install pycairo
  * pip install PyGObject
  * python setup.py build
  * sudo python setup.py install
  * ldtp // This runs fine in pycharm, but fails in command line
  * python examples/gedit.py // This fails in both pycharm and command line
