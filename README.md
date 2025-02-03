# Number Classification API

A Django REST API that takes a number and returns interesting mathematical properties about it, along with a fun fact.

## Features

- Classifies numbers based on various mathematical properties
- Provides fun facts about numbers using the Numbers API
- Handles CORS for cross-origin requests
- Returns responses in JSON format
- Input validation and error handling

## API Specification

### Endpoint 

## Error Handling

The API handles various error cases:
- Invalid input (non-numeric values)
- Missing number parameter
- Server-side errors

## Deployment

This API is deployed at: [Add your deployment URL here]

## CORS Configuration

The API is configured to handle CORS (Cross-Origin Resource Sharing) and accepts requests from:
- http://localhost:8080
- http://127.0.0.1:9000
- [Add any other allowed origins]

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

[Add your license here]

## Contact

[Add your contact information here]

## Acknowledgments

- [Numbers API](http://numbersapi.com) for providing number facts
- [Add any other acknowledgments]

### Success Response (200 OK) 

## Dependencies

- Django 5.1.5
- Django REST Framework 3.15.2
- Django CORS Headers 4.6.0
- Requests 2.31.0

## API Usage Examples

1. Get properties of number 371:
```
GET /api/classify-number?number=371
```

2. Get properties of number 28:
```
GET /api/classify-number?number=28
```

3. Invalid input:
```
GET /api/classify-number?number=abc
```

## Properties Explained

- **is_prime**: Checks if the number is prime (only divisible by 1 and itself)
- **is_perfect**: Checks if the number equals the sum of its proper divisors
- **properties**: Array containing "armstrong" and/or "odd"/"even"
- **digit_sum**: Sum of all digits in the number
- **fun_fact**: Interesting mathematical fact about the number

## Local Development Setup

1. Clone the repository
```bash
git clone <repository-url>
cd <project-directory>
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Start the development server
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/classify-number`

## Testing

To run the tests:
```bash
python manage.py test
```