# SERVER LOGGER
import os
current_dir = os.path.dirname(os.path.abspath(__file__))

import logging
# Configure logging
logging.basicConfig(filename=f"{current_dir}/serverLog.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')