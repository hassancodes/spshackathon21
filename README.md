
# SGA Visionary Submission

A web application that integrates NASA's Power API to provide solar panel data and crop information.

## Project Overview
This application provides:
- Solar panel power generation data using NASA's Power API
- Crop information and documentation
- User-friendly interface for accessing solar and agricultural data

## Features
- Solar panel power generation calculations
- Crop information pages
- Documentation section
- About us page

## Setup Instructions
1. Ensure Python 3.x is installed
2. Install required dependencies:
   ```
   pip install flask
   ```
3. Run the application:
   ```
   python src/main.py
   ```
4. Open your browser and navigate to `http://localhost:8888`

### Frontend (Next.js)
1. Ensure Node.js is installed
2. Install dependencies:
   ```
   cd nextjs-app && npm install
   ```
3. Start the development server:
   ```
   npm run dev
   ```
4. Visit `http://localhost:3000` to view the React frontend

## Project Structure
- `main.py`: Contains NASA API integration code
- `api/app.py`: Flask web server implementation
- `static/`: Contains HTML, CSS, and other static files
- `nextjs-app/`: Next.js frontend application
- `README.md`: Project documentation

## API Integration
The application uses NASA's Power API to fetch solar panel power generation data. The API endpoint is configured to fetch monthly data for a specific location.

## Contributing
Please feel free to submit issues and enhancement requests!

## License
This project is licensed under the MIT License - see the LICENSE file for details

## Acknowledgments
- NASA Power API for solar data
- Flask framework for web development
