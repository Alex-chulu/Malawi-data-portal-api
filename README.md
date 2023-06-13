![historical_places](https://github.com/Alex-chulu/Malawi-data-portal-api/assets/72263272/b0cc02b5-f543-45ba-86dd-587c681fbc30)

For a project landing page, here is the link https://alex-chulu.github.io/Malawi-data-portal-api/
# Malawi Data Portal API

The Malawi Data Portal API provides access to various data sets about Malawi, 
including information on the total population, regions, major cities, districts, 
historical places, hospitals, schools, and villages. This API allows developers to 
retrieve and utilize the data for their applications or research purposes.

Growing up in Malawi, I witnessed firsthand the challenges faced due to limited access 
to organized and reliable data. This inspired me to develop the Malawi Data Portal API, 
a platform that provides easy access to crucial data about Malawi.

I realized that access to comprehensive and up-to-date data is essential for informed decision-making
in various sectors such as healthcare, education, and urban planning. This project aims to bridge the 
data gap and empower individuals and organizations with the information they need to make impactful decisions.


## Base URL

The base URL for the API is: `https://api.malawidataportal.com` `This is a test url and not used in production. 
For API use in production please contact the developer of the API`

## Endpoints

The following endpoints are available in the Malawi Data Portal API:

### 1. Total Population
![Population](https://github.com/Alex-chulu/Malawi-data-portal-api/assets/72263272/606b5c7a-807f-42ad-9a4a-dd17a18b2173)


- Endpoint: `/population`
- Method: GET
- Description: Retrieves the total national population of Malawi.
- Response Format: JSON
- Example Response:
  ```json
  {
    "totalPopulation": 19000000
  }
  ```

### 2. Regions

- Endpoint: `/regions`
- Method: GET
- Description: Retrieves the list of regions in Malawi.
- Response Format: JSON
- Example Response:
  ```json
  {
    "regions": [
      "Northern",
      "Central",
      "Southern"
    ]
  }
  ```

### 3. Major Cities
![Cities](https://github.com/Alex-chulu/Malawi-data-portal-api/assets/72263272/5b240bbf-f410-470f-bd4d-049f2e0d1b6f)


- Endpoint: `/cities`
- Method: GET
- Description: Retrieves a list of major cities in Malawi, along with their population and location data.
- Response Format: JSON
- Example Response:
  ```json
  {
    "cities": [
      {
        "name": "Lilongwe",
        "population": 989615,
        "latitude": -13.9833,
        "longitude": 33.7833
      },
      {
        "name": "Blantyre",
        "population": 832082,
        "latitude": -15.7833,
        "longitude": 35.0000
      },
      ...
    ]
  }
  ```

### 4. Districts

- Endpoint: `/districts`
- Method: GET
- Description: Retrieves a list of all districts in Malawi, along with their population and any 
- available data on hospitals, schools, or villages within each district.
- Response Format: JSON
- Example Response:
  ```json
  {
    "districts": [
      {
        "name": "Lilongwe",
        "population": 1830321,
        "hospitals": [
          {
            "name": "Kamuzu Central Hospital",
            "location": "Lilongwe",
            "bedCount": 500
          },
          ...
        ],
        "schools": [
          {
            "name": "Lilongwe High School",
            "location": "Lilongwe",
            "studentCount": 1200
          },
          ...
        ],
        "villages": [
          {
            "name": "Mtsiliza",
            "location": "Lilongwe",
            "population": 2500
          },
          ...
        ]
      },
      {
        "name": "Blantyre",
        "population": 1186187,
        "hospitals": [...],
        "schools": [...],
        "villages": [...]
      },
      ...
    ]
  }
  ```

### 5. Historical Places

- Endpoint: `/historical-places`
- Method: GET
- Description: Retrieves a list of important historical places in Malawi, along with any available 
- data on their significance and historical context.
- Response Format: JSON
- Example Response:
  ```json
  {
    "historicalPlaces": [
      {
        "name": "Mua Mission",
        "description": "Mua Mission is a historic Catholic mission known for its cultural museum, art center, 
        and historical significance in preserving Malawian culture and traditions.",
        "location": "Mua, Dedza"
      },
      {
        "name": "Chongoni Rock Art Area",
        "description": "Chongoni Rock Art Area is a UNESCO World Heritage Site featuring ancient rock paintings, 
        showcasing the rich cultural heritage of Malawi's early inhabitants.",
        "location": "Dedza"
      },
      ...
    ]
  }
  ```
# Tech Stack
The following technologies were used to create this API:

Flask (Python web framework)
Flask-RESTful (RESTful API extension for Flask)
SQLAlchemy (database toolkit for Python)

# Installation
Clone this repository.
Navigate to the project directory in your terminal.
Create a virtual environment and activate it. (Optional)
Install dependencies
Run the application

## Authentication

The Malawi Data Portal API does not require authentication for accessing the available endpoints, at least for this V1

## Rate Limiting

To ensure fair usage and prevent abuse, the API has a rate limiting mechanism. Each endpoint has a specific 
rate limit defined. If the rate limit is exceeded, you will receive a 429 (Too Many Requests) response. 
Please adhere to the rate limits to ensure uninterrupted access to the API.

## Error Handling

In case of errors or invalid requests, the API will return appropriate HTTP status codes along with error messages 
to help identify and resolve issues.

400 - Bad Request
404 - Not Found
500 - Internal Server Error

## Support and Contact

If you have any questions, issues, or feedback regarding the Malawi Data Portal API, please contact me at `chulualexandar@gmail.com`.

# Authors
Alexander Chulu
Email: chulualexandar@gmail.com 

# License
This project is licensed under the MIT License - see the LICENSE.md file for details.

We hope you find the Malawi Data Portal API useful for your projects or research. Happy coding!
