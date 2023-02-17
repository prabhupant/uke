# uke
Make background task in Python easier again!

## Usage

```python

import uke
import time

@uke.job
def run():
    # Do awesome things here in the background
    time.sleep(5)

for i in range(100):
    run()

```
