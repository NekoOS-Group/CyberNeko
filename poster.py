import requests
import json

def __post__(url, command, params, proxy):
    try:
        print( url, command, params, proxy )
        r = requests.get( url+command, params = params, proxies=proxy )
        if r.status_code != 200:
            raise Exception("404 not found")
        r = json.loads(r.content)
        if not r['ok']:
            raise Exception("Bad requests")
        return r['result']
    except:
        raise Exception("Network Error")

def post(bot, command, params = ""):
    return __post__( bot.__getUrl__(), command, params, bot.__getProxy__() )

def comfirm_params( params_table, params ):
    for x, y in params.items():
        if params[x] == None:
            raise Exception( "Invalid param : '%s'" % s ) 
        need = [params_table[x]] if isinstance(params_table[x],type) else params_table[x]
        for t in need:
            if isinstance(y, t):
                break
        else:
            raise Exception( "For param '%s' need, but %s given" % ( str(need), str(type(y)) ) )
    return True
