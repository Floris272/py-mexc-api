# Welcome to the mexc api docs!

Python wrapper for the Mexc api

[mexc docs](https://www.mexc.com/mexc-api)

## Usage

### Requirements
- Python 3.11 or newer
- requests
- websocket-client

### installation
```
pip install mexc-api
```

### api key
generate an api key here: 
[https://www.mexc.com/user/openapi](https://www.mexc.com/user/openapi)


### Example
```python
import time
from mexc_api.spot import Spot
from mexc_api.websocket import SpotWebsocketStreamClient
from mexc_api.common.enums import Side, OrderType, StreamInterval, Action
from mexc_api.common.exceptions import MexcAPIError

KEY = "<KEY>"
SECRET = "<KEY>"

spot = Spot(KEY, SECRET)

server_time = spot.market.server_time()
print(server_time)

order_book = spot.market.order_book("MXUSDT")
print(order_book)

order = spot.account.test_new_order(
    "MXUSDT",
    Side.BUY,
    OrderType.LIMIT,
    '1',
    price='1'
)
print(order)

ws = SpotWebsocketStreamClient(
    KEY,
    SECRET,
    on_message=print
)
time.sleep(1)
ws.klines("MXUSDT", StreamInterval.ONE_MIN)
ws.account_orders()

time.sleep(5)
ws.account_orders(Action.UNSUBSCRIBE)
ws.klines("MXUSDT", StreamInterval.ONE_MIN, Action.UNSUBSCRIBE)
ws.stop()
```

```{toctree}
---
hidden:
maxdepth: 2
---
spot
websocket_stream
enums
exceptions
```