#!/usr/bin/env python
import user_info

try:
    user_info.get_info('zs',125)
except ValueError as e:
    print(e)
