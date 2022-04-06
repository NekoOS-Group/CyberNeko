import requests
import json
from tgbot.bits.decorators import log_full, log_stack, log_timer

def __post__(url, command, params, proxy):
    r = requests.get( url+command, params = params, proxies=proxy )
    if r.status_code != 200:
        raise Exception("404 not found")
    
    r = json.loads(r.content)
    if not r['ok']:
        raise Exception("Requests failed")

    return r['result']

def post(bot, command, params = ""):
    return __post__( bot.url, command, params, bot.proxy )

def comfirm_params( params_table, params ):
    for x, y in params.items():
        if params_table[x] is None:
            raise Exception( f"Invalid param : '{x}'" ) 
        need = [params_table[x]] if isinstance(params_table[x], type) else params_table[x]
        for t in need:
            if isinstance(y, t):
                break
        else:
            raise Exception( f"For param '{str(need)}' need, but {str(type(y))} given" )
    return True
