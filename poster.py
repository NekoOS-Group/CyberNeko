import requests
import io

def __post__(url, command, params, proxy):
    try:
        r = requests.get( url+command, params = params, proxies=proxy )
        if r.status_code != 200:
            raise Exception("404 not found")
        return r.content
    except:
        raise Exception("Error")

def post(bot, command, params = ""):
    return __post__( bot.__getUrl__(), command, params, bot.__getProxy__() )

def comfirm_params( params_table, params ):
    for x, y in params.items():
        if params[x] == None:
            raise Exception( "Invalid param : '" + x + "'" )
        if not isinstance(y ,params_table[x]):
            raise Exception( "For param '" + x + "' : " + str(params_table[x]) + " need, but " + str(type(y)) + " given" )
    return True
