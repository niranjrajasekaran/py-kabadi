# py-kabadi library for Roanuz kabadi API
py-kabadi library for Python using Roanuz kabadi API's.  Easy to install and simple way to access all Roanuz Kabadi API's. Its a Python library for getting Live Kabadi Score, Schedule and Statistics.


## Getting started
1. Install py-kabadi using `pip install https://github.com/niranjfantain/py-kabadi.git`

2. Create a App here [My APP Login](https://www.cricketapi.com/login/?next=/apps/)

3. Import pykabadi and create Authentication using 'RcaFileStorageHandler' or 'RcaStorageHandler' approach.For accessing each API we need to get the 'AccessToken'

    ## Example

    ```rust
    //Use your kabadi API Application details below.

    //RcaStorageHandler
    import pykabadi
    handler = pykabadi.RcaStorageHandler()
    start = pykabadi.RcaApp(access_key="Your_AccessKey", \
                            secret_key="Your_SecretKey", \
                            app_id="Your_APP_ID", \
                            store_handler=handler \
                           )

    'OR'

    //RcaFileStorageHandler(from environmental variable)

    Environmental variable:
        RCA_ACCESS_KEY = access_key
        RCA_SECRET_KEY = secret_key
        RCA_APP_ID = app_id

    handler = pykabadi.RcaFileStorageHandler()
    start = pykabadi.RcaApp(store_handler=handler)

    // After Completing Authentication you can successfully access the API's.

    start.get_match("pkl_2017_g103") //Return Match information in json format
    start.get_season('pkl_2017') //Return Season information in json format
    For more free API's visit : https://www.cricketapi.com/docs/freeapi/
    ```


 ### List of Roanuz Kabadi API

* [Match API](https://www.cricketapi.com/docs/match_api/)  start.get_match("match_key")
* [Season API](https://www.cricketapi.com/docs/season_api/)  start.get_season("season_key")
* [Season Team API](https://www.cricketapi.com/docs/season_api/)  start.get_season_team("season_key", "season_team_key")

 ## Roanuz Cricket API 
	This Library uses the Roanuz Cricket API for fetching cricket scores and stats. Learn more about Litzscore Cricket API on https://www.cricketapi.com/ 

 ## Contact:
    Feel free to call us anytime, We have an amazing team to support you.
    You can contact us at : support@cricketapi.com
