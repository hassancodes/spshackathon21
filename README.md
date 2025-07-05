
# SolarSave

SolarSave is a NASA‑powered web application that helps growers plan solar panels and crops. By combining real solar data with straightforward tools, the project demonstrates how space technology can support sustainable agriculture.

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

### Why SolarSave?
- Built on trusted NASA POWER data for reliable solar insights
- Simple HTML interface that can be extended to modern frameworks
- Open-source code ready for integration with your own tools

## Setup Instructions
1. Ensure Python 3.x is installed
2. Install required dependencies:
   ```
   pip install -r src/requirements.txt
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
- `docs/`: Markdown documentation used for GitHub Pages

## API Integration
The application uses NASA's Power API to fetch solar panel power generation data. The API endpoint is configured to fetch monthly data for a specific location.

## Running Tests
Run the unit tests with:
```bash
pytest
```

## Contributing
Please feel free to submit issues and enhancement requests!

## Documentation
Additional documentation is stored in the `docs/` directory. When pushed to GitHub, these files can be published using GitHub Pages.

## License
This project is licensed under the MIT License - see the LICENSE file for details

## Acknowledgments
- NASA Power API for solar data
- Flask framework for web development
