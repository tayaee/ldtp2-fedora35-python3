sudo dnf install -y python3-wheel
sudo dnf install -y gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel tk-devel git python3-cairo-devel cairo-gobject-devel gobject-introspection-devel
/usr/bin/python -m venv venv
. venv/bin/activate
python -m pip install --upgrade pip
(cd venv/lib/python3.10/site-packages; ln -s /usr/lib/python3.10/site-packages/pyatspi)
pip install twisted
pip install pycairo PyGObject

