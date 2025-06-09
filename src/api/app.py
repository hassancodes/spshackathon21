"""
Flask server for SGA Visionary Submission
Provides endpoints for accessing static content and API endpoints
"""

from flask import Flask, render_template, jsonify, request, abort
from core.solar_calculator import SolarDataCalculator
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    """Serve the main index page"""
    return app.send_static_file('index.html')

@app.route('/crops')
def crops():
    """Serve crops information page"""
    return app.send_static_file('crops.html')

@app.route('/documentation')
def documentation():
    """Serve documentation page"""
    return app.send_static_file('documentation.html')

@app.route('/aboutus')
def aboutus():
    """Serve about us page"""
    return app.send_static_file('aboutus.html')

@app.route('/api/solar-data', methods=['GET'])
def get_solar_data():
    """
    API endpoint to get solar panel power generation data
    Returns:
        JSON response with solar power data
    """
    try:
        calculator = SolarDataCalculator()
        average_power = calculator.calculate_average_power()
        return jsonify({
            'status': 'success',
            'data': {
                'average_power': average_power,
                'units': 'W/m²',
                'year': calculator.start_year
            }
        })
    except Exception as e:
        logger.error(f"Error in solar data API: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'status': 'error',
        'message': 'Resource not found'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors"""
    logger.error(f"Internal error: {str(error)}")
    return jsonify({
        'status': 'error',
        'message': 'Internal server error'
    }), 500

if __name__ == '__main__':
    logger.info("Starting Flask server on port 8888")
    app.run(port=8888, debug=True)
