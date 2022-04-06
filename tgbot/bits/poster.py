import requests
import json
#from strings import decorating
import time

def __post__(url, command, params, proxy, logger=None):
    try:
        if logger != None : 
            global time_offset
            time_offset = time.perf_counter()
            #logger.info( "%-80s" % ( "API request : %s %s " % ( decorating( command, 33 ), str(params) ) ) )
        
        r = requests.get( url+command, params = params, proxies=proxy )
        if r.status_code != 200:
            raise Exception("404 not found")
        r = json.loads(r.content)
        if not r['ok']:
            raise Exception("Bad requests")
        
        if logger != None : 
            pass
            #logger.info( decorating( "Success! TTL=%fs\n" % (time.perf_counter() - time_offset), 32 ) )
        
        return r['result']
    except:
        raise Exception("Network Error")

def post(bot, command, params = ""):
    return __post__( bot.__getUrl__(), command, params, bot.__getProxy__(), bot.logger )

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
