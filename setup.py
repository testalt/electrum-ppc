#!/usr/bin/python

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp


version = imp.load_source('version', 'lib/version.py')
util = imp.load_source('version', 'lib/util.py')

if sys.version_info[:3] < (2, 6, 0):
    sys.exit("Error: Electrum requires Python version >= 2.6.0...")

usr_share = '/usr/share'
if not os.access(usr_share, os.W_OK):
    usr_share = os.getenv("XDG_DATA_HOME", os.path.join(os.getenv("HOME"), ".local", "share"))

data_files = []
if (len(sys.argv) > 1 and (sys.argv[1] == "sdist")) or (platform.system() != 'Windows' and platform.system() != 'Darwin'):
    print "Including all files"
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum-ppc.desktop']),
        (os.path.join(usr_share, 'app-install', 'icons/'), ['icons/electrum-ppc.png'])
    ]
    if not os.path.exists('locale'):
        os.mkdir('locale')
    for lang in os.listdir('locale'):
        if os.path.exists('locale/%s/LC_MESSAGES/electrum.mo' % lang):
            data_files.append((os.path.join(usr_share, 'locale/%s/LC_MESSAGES' % lang), ['locale/%s/LC_MESSAGES/electrum.mo' % lang]))


appdata_dir = util.appdata_dir()
if not os.access(appdata_dir, os.W_OK):
    appdata_dir = os.path.join(usr_share, "electrum-ppc")

data_files += [
    (appdata_dir, ["data/README"]),
    (os.path.join(appdata_dir, "cleanlook"), [
        "data/cleanlook/name.cfg",
        "data/cleanlook/style.css"
    ]),
    (os.path.join(appdata_dir, "sahara"), [
        "data/sahara/name.cfg",
        "data/sahara/style.css"
    ]),
    (os.path.join(appdata_dir, "dark"), [
        "data/dark/name.cfg",
        "data/dark/style.css"
    ])
]

for lang in os.listdir('data/wordlist'):
    data_files.append((os.path.join(appdata_dir, 'wordlist'), ['data/wordlist/%s' % lang]))


setup(
    name="Electrum-ppc",
    version=version.ELECTRUM_VERSION,
    install_requires=[
        'slowaes',
        'ecdsa>=0.9',
        'pbkdf2',
        'requests',
        'pyasn1',
        'pyasn1-modules',
        'qrcode',
        'SocksiPy-branch',
        'tlslite'
    ],
    package_dir={
        'electrum_ppc': 'lib',
        'electrum_ppc_gui': 'gui',
        'electrum_ppc_plugins': 'plugins',
    },
    scripts=['electrum-ppc'],
    data_files=data_files,
    py_modules=[
        'electrum_ppc.account',
        'electrum_ppc.bitcoin',
        'electrum_ppc.blockchain',
        'electrum_ppc.bmp',
        'electrum_ppc.commands',
        'electrum_ppc.daemon',
        'electrum_ppc.i18n',
        'electrum_ppc.interface',
        'electrum_ppc.mnemonic',
        'electrum_ppc.msqr',
        'electrum_ppc.network',
        'electrum_ppc.network_proxy',
        'electrum_ppc.old_mnemonic',
        'electrum_ppc.paymentrequest',
        'electrum_ppc.paymentrequest_pb2',
        'electrum_ppc.plugins',
        'electrum_ppc.qrscanner',
        'electrum_ppc.simple_config',
        'electrum_ppc.synchronizer',
        'electrum_ppc.transaction',
        'electrum_ppc.util',
        'electrum_ppc.verifier',
        'electrum_ppc.version',
        'electrum_ppc.wallet',
        'electrum_ppc.x509',
        'electrum_ppc_gui.gtk',
        'electrum_ppc_gui.qt.__init__',
        'electrum_ppc_gui.qt.amountedit',
        'electrum_ppc_gui.qt.console',
        'electrum_ppc_gui.qt.history_widget',
        'electrum_ppc_gui.qt.icons_rc',
        'electrum_ppc_gui.qt.installwizard',
        'electrum_ppc_gui.qt.lite_window',
        'electrum_ppc_gui.qt.main_window',
        'electrum_ppc_gui.qt.network_dialog',
        'electrum_ppc_gui.qt.password_dialog',
        'electrum_ppc_gui.qt.paytoedit',
        'electrum_ppc_gui.qt.qrcodewidget',
        'electrum_ppc_gui.qt.qrtextedit',
        'electrum_ppc_gui.qt.receiving_widget',
        'electrum_ppc_gui.qt.seed_dialog',
        'electrum_ppc_gui.qt.transaction_dialog',
        'electrum_ppc_gui.qt.util',
        'electrum_ppc_gui.qt.version_getter',
        'electrum_ppc_gui.stdio',
        'electrum_ppc_gui.text',
        'electrum_ppc_plugins.btchipwallet',
        'electrum_ppc_plugins.coinbase_buyback',
        'electrum_ppc_plugins.cosigner_pool',
        'electrum_ppc_plugins.exchange_rate',
        'electrum_ppc_plugins.greenaddress_instant',
        'electrum_ppc_plugins.labels',
        'electrum_ppc_plugins.trezor',
        'electrum_ppc_plugins.virtualkeyboard',
    ],
    description="Lightweight Peercoin Wallet",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU GPLv3",
    url="https://ppc.electrum-alt.org",
    long_description="""Lightweight Peercoin Wallet"""
)
