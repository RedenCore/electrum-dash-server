from setuptools import setup

setup(
    name="electrum-reden-server",
    version="1.0",
    scripts=['run_electrum_reden_server','electrum-reden-server'],
    install_requires=['plyvel','jsonrpclib', 'irc >= 11, <=14.0', 'x11_hash'],
    package_dir={
        'electrumserver':'src'
        },
    py_modules=[
        'electrumserver.__init__',
        'electrumserver.utils',
        'electrumserver.storage',
        'electrumserver.deserialize',
        'electrumserver.networks',
        'electrumserver.blockchain_processor',
        'electrumserver.server_processor',
        'electrumserver.processor',
        'electrumserver.version',
        'electrumserver.ircthread',
        'electrumserver.stratum_tcp'
    ],
    description="Reden Electrum Server",
    author="Thomas Voegtlin ,ELM4ever, Propulsion, TheLazieR, Tri Nguyen",
    author_email="thomasv@electrum.org, thelazier@gmail.com, tri282@gmail.com",
    license="MIT Licence",
    url="https://github.com/spesmilo/electrum-server/ , https://github.com/RedenCore/electrum-reden-server/",
    long_description="""Server for the Electrum Lightweight Reden Wallet"""
)
