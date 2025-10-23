# ============================================
# IMPORTING MODULES - LOGGING EXAMPLE
# ============================================
# This demonstrates importing from Python's standard library
# Standard library = modules that come WITH Python (no pip install needed)

# ============================================
# EXAMPLE 1: Simple top-level import
# ============================================
# Some modules are imported directly
import logging

print("=" * 60)
print("EXAMPLE 1: Basic Logging")
print("=" * 60)
print()

# Configure logging to show messages
# level=logging.INFO means "show INFO level and above"
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Different levels of logging (from least to most severe)
logging.debug("This is a DEBUG message - for detailed troubleshooting")
logging.info("This is an INFO message - general information")
logging.warning("This is a WARNING message - something might be wrong")
logging.error("This is an ERROR message - something went wrong")
logging.critical("This is a CRITICAL message - serious problem!")

print()

# ============================================
# EXAMPLE 2: Importing from a sub-module
# ============================================
# Some modules have sub-modules inside them
# Format: from module.submodule import something
# This is NOT top-level - we're going INSIDE the module

print("=" * 60)
print("EXAMPLE 2: Importing from logging.handlers")
print("=" * 60)
print()

# logging.handlers is a SUB-MODULE inside the logging module
# We import RotatingFileHandler from inside logging.handlers
from logging.handlers import RotatingFileHandler

print("We imported RotatingFileHandler from logging.handlers")
print("This is a sub-module import - not top-level!")
print()

# Create a file handler that rotates log files when they get too big
file_handler = RotatingFileHandler(
    "app.log",  # Log file name
    maxBytes=1000,  # Max size: 1000 bytes
    backupCount=3,  # Keep 3 backup files
)

# Set the format for file logs
file_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
)

# Add the handler to the logger
logger = logging.getLogger()
logger.addHandler(file_handler)

# Now messages go to BOTH console and file
logging.info("This message goes to console AND app.log file")
logging.warning("File logging is working!")

print("Check the 'app.log' file - it has the log messages!")
print()

# ============================================
# EXAMPLE 3: Multiple sub-module imports
# ============================================
print("=" * 60)
print("EXAMPLE 3: Importing Multiple Items from Sub-modules")
print("=" * 60)
print()

# Import multiple handlers from the same sub-module
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

print("Imported TWO handlers from logging.handlers:")
print("  1. RotatingFileHandler - rotates by file size")
print("  2. TimedRotatingFileHandler - rotates by time (daily, hourly, etc.)")
print()

# ============================================
# EXAMPLE 4: Why use sub-modules?
# ============================================
print("=" * 60)
print("EXAMPLE 4: Understanding Module Organization")
print("=" * 60)
print()

print("Python organizes code into modules and sub-modules:")
print()
print("logging/                    <- Main module")
print("  ├── __init__.py           <- Top-level (logging.info, logging.error)")
print("  ├── handlers.py           <- Sub-module (logging.handlers)")
print("  └── config.py             <- Sub-module (logging.config)")
print()
print("Top-level import:    import logging")
print("Sub-module import:   from logging.handlers import RotatingFileHandler")
print()

# ============================================
# EXAMPLE 5: Practical logging in a program
# ============================================
print("=" * 60)
print("EXAMPLE 5: Practical Example - Processing Data")
print("=" * 60)
print()

# Simulate processing some data with logging
data = [10, 20, 30, 0, 50]

logging.info("Starting data processing...")

for i, value in enumerate(data):
    try:
        result = 100 / value
        logging.info(f"Processed item {i}: 100 / {value} = {result}")
    except ZeroDivisionError:
        logging.error(f"Cannot divide by zero at index {i}")
    except Exception as e:
        logging.critical(f"Unexpected error: {e}")

logging.info("Data processing complete!")
print()

# ============================================
# SUMMARY
# ============================================
print("=" * 60)
print("SUMMARY: Module Imports")
print("=" * 60)
print()
print("TOP-LEVEL IMPORT (simple):")
print("  import logging")
print("  logging.info('message')")
print()
print("SUB-MODULE IMPORT (going deeper):")
print("  from logging.handlers import RotatingFileHandler")
print("  handler = RotatingFileHandler('file.log')")
print()
print("Standard library = comes with Python (no pip install)")
print("External library = needs pip install (like 'requests')")
print()
print("Next step: Learn pip and external modules like 'requests'!")
