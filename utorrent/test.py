from utorrent.connection import Connection
from utorrent.uTorrent import Desktop

url ='C:\\Users\\ArmandoAnglesey\\Downloads\\Regata_OS_20-nv.x86_64-20.1.4.iso.torrent'
utorrentcfg = {
    "host": '127.0.0.1:7070',
    "login": 'admin',
    "password": 'password',
    "api": None,
    "default_torrent_format": "{hash_code} {status} {progress}% {size} {dl_speed} {ul_speed} {ratio} {peer_info} eta: {eta} {name} {label}",
}

connection = Connection(utorrentcfg["host"], utorrentcfg["login"], utorrentcfg["password"], None,None)
instance = Desktop(connection)
torrent = instance.torrent_add_file(url, download_dir = 'C:\\Users\\ArmandoAnglesey\\Downloads')

props = []
name = 'label'
value = 'test'
props.append( { torrent: { name: value } } )
print(instance.torrent_set_props(props))