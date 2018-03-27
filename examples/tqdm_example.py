#!/usr/bin/env python

import tqdm
import time

pbar = tqdm.tqdm(total=10)

for i in range(10):

  time.sleep(0.5)
  pbar.update(1)

pbar.close()
