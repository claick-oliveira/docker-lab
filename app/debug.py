# -*- coding: utf-8 -*-

#!/usr/bin/env python3

import logging
import sys

from api import app


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s %(levelname)s %(message)s")
    logging.StreamHandler(sys.stdout)
    logging.info("Starting API using flask debug server")
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
