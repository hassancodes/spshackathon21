"""
Main entry point for the SGA Visionary Application
Combines both Flask API and Solar Panel Visualization
"""

import os
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from api.app import app
from core.solar_calculator import SolarDataCalculator
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SGAApplication:
    """
    Main application class that combines Flask API and Solar Panel Visualization
    """
    
    def __init__(self):
        """Initialize the application"""
        self.calculator = SolarDataCalculator()
        self.app = app
        
    def run(self):
        """Run the application"""
        logger.info("Starting SGA Visionary Application")
        try:
            # Start Flask server
            self.app.run(
                host='0.0.0.0',
                port=8888,
                debug=True
            )
        except Exception as e:
            logger.error(f"Application failed to start: {str(e)}")
            raise

def main():
    """Main function to run the application"""
    app = SGAApplication()
    app.run()

if __name__ == "__main__":
    main()
