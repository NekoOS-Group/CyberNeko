import requests
import json


def post(url: str, params=None, proxy=None):
    """
    Wrapper of requests.post()

    Args:
        url: the distinction to post
        params: request params
        proxy: proxies

    Returns:
        the dict that server return

    Raises:
        Exception: 404 not found
    """
    r = requests.post(url, params=params, proxies=proxy)
    if r.status_code != 200:
        raise Exception("404 not found")

    return json.loads(r.content)


def verify_params(params_table, params):
    """Verify the type of params to be posted

    Args:
        params_table:
        params:

    Returns:
        True if passed this verification

    Raises:
        Exception1: Invalid param
        Exception2: Invalid type
    """
    for x, y in params.items():
        if params_table[x] is None:
            raise Exception(f"Invalid param : '{x}'")
        need = [params_table[x]] if isinstance(params_table[x], type) else params_table[x]
        for t in need:
            if isinstance(y, t):
                break
        else:
            raise Exception(f"For param '{str(need)}' need, but {str(type(y))} given")
    return True
