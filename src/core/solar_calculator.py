"""
Solar Panel Data Calculator and Visualizer using NASA Power API
This module fetches solar panel power generation data from NASA's Power API
and provides both calculation and visualization capabilities.
"""

import json
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import logging
import matplotlib.pyplot as plt

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SolarDataCalculator:
    """
    Class for calculating and visualizing solar panel power generation data
    using NASA Power API
    """
    
    def __init__(self, parameters="PS", community="RE", longitude="-77.0720", latitude="38.8848"):
        """
        Initialize the calculator with default parameters
        """
        self.parameters = parameters
        self.community = community
        self.longitude = longitude
        self.latitude = latitude
        self.start_year = "2019"
        self.end_year = "2020"
        
    def get_nasa_url(self):
        """
        Generate the NASA Power API URL
        """
        return ("https://power.larc.nasa.gov/api/temporal/monthly/point?parameters={0}&community={1}&"
                "longitude={2}&latitude={3}&format=JSON&start={4}&end={5}".format(
                    self.parameters, self.community, self.longitude, self.latitude,
                    self.start_year, self.end_year))
    
    def fetch_data(self):
        """
        Fetch data from NASA Power API
        Returns:
            dict: Parsed JSON response from NASA API
        Raises:
            Exception: If API request fails
        """
        try:
            url = self.get_nasa_url()
            logger.info(f"Fetching data from: {url}")
            response = urlopen(url)
            return json.loads(response.read())
        except (URLError, HTTPError) as e:
            logger.error(f"Error fetching data: {str(e)}")
            raise Exception(f"Failed to fetch data from NASA API: {str(e)}")
    
    def calculate_average_power(self):
        """
        Calculate average power generation from NASA data
        Returns:
            float: Average power generation
        """
        try:
            nasa_data = self.fetch_data()
            months_data = nasa_data["properties"]["parameter"]["PS"]
            
            total_power = sum(months_data.values())
            num_months = len(months_data)
            
            if num_months == 0:
                raise ValueError("No data available for calculation")
                
            average_power = total_power / num_months
            logger.info(f"Average power generation: {average_power}")
            return average_power
            
        except KeyError as e:
            logger.error(f"Missing key in API response: {str(e)}")
            raise Exception("Invalid data format from NASA API")
        except Exception as e:
            logger.error(f"Error calculating average power: {str(e)}")
            raise
    
    def visualize_power_data(self):
        """
        Create a visualization of monthly power generation data
        Returns:
            matplotlib.figure.Figure: Power generation plot
        """
        try:
            nasa_data = self.fetch_data()
            months_data = nasa_data["properties"]["parameter"]["PS"]
            
            # Extract month names and power values
            months = list(months_data.keys())
            power_values = list(months_data.values())
            
            # Create plot
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.bar(months, power_values, color='#4CAF50')
            
            # Format plot
            ax.set_title('Monthly Solar Power Generation')
            ax.set_xlabel('Month')
            ax.set_ylabel('Power Generation (W/m²)')
            ax.grid(True, axis='y', alpha=0.3)
            
            # Rotate x-axis labels
            plt.xticks(rotation=45, ha='right')
            
            return fig
            
        except Exception as e:
            logger.error(f"Error creating visualization: {str(e)}")
            raise

def main():
    """
    Main function to run the solar panel power calculator and visualizer
    """
    try:
        calculator = SolarDataCalculator()
        
        # Calculate and print average power
        average_power = calculator.calculate_average_power()
        print(f"What is your Solar panel Wattage?")
        print(f"Average power generation in {calculator.start_year} is: {average_power:.2f} W/m²")
        
        # Create visualization
        fig = calculator.visualize_power_data()
        plt.tight_layout()
        plt.show()
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
