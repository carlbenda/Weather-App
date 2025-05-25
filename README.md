# Atmos - Weather Insights

A stunning, modern Django weather application with an eye-catching UI that provides real-time weather information and forecasts using WeatherAPI.

## Features

- Beautiful dark-themed interface with advanced visual effects
- Real-time weather data for any city worldwide
- One-click geolocation for automatic weather detection
- 7-day detailed weather forecasts
- Comprehensive weather metrics (temperature, conditions, humidity, wind speed, and rain chance)
- New searches automatically clear previous results
- Fully responsive design across all devices

## UI Highlights

- **Advanced Visual Design**
  - Stunning dark theme with subtle gradient backgrounds
  - Neumorphic elements with realistic shadows and depth
  - Gradient text and accent colors for visual appeal
  - Decorative elements and animated micro-interactions

- **Interactive Elements**
  - Hover animations on all interactive components
  - Subtle transitions and transforms for fluid experience
  - Animated weather icons and indicators
  - Visual feedback for user actions

- **Modern Typography & Layout**
  - Clean, contemporary typography with Manrope font
  - Thoughtful information hierarchy and spacing
  - Grid-based stats display with hover effects
  - Optimized for both desktop and mobile

- **Responsive Excellence**
  - Fluid layouts that adapt to any screen size
  - Mobile-optimized touch targets and spacing
  - Properly scaled elements on smaller screens
  - Consistent experience across all devices

## Technical Highlights

- CSS custom properties for consistent theming
- Advanced CSS techniques (gradients, backdrop-filter, text effects)
- Subtle animations using CSS keyframes
- JavaScript enhancements for mobile experience

## Requirements

- Python 3.x
- Django 5.x
- Requests library

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd weather_project
   ```

2. Install the required packages:
   ```
   pip install django requests
   ```

3. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Run the server:
   ```
   python manage.py runserver
   ```

5. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

## How to Use

1. Enter a city name in the search box and click "Search", or
2. Click the "My Location" button to use your device's geolocation
3. View current weather with beautiful visualizations
4. Scroll down to see the detailed 7-day forecast
5. Each new search automatically clears previous results