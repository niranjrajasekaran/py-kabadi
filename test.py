from src import pykabadi

handler = pykabadi.RcaStorageHandler()
start = pykabadi.RcaApp(access_key="73fc9bf7dbe773bc02371a2708249e57",
                        secret_key="cc8c3a60abfbe9577b39508da5a2a2fb",
                        app_id="fantainlive",
                        store_handler=handler)

print "Season"
print "======"
print start.get_season('pkl_2017')
print "Season Team"
print "==========="
print start.get_season_team('pkl_2017', 'pkl_2017_ben_bulls')
print "Match"
print "====="
print start.get_match('pkl_2017_g103')
