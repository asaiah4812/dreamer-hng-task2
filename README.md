# Number Classification API

A sophisticated Django REST API that analyzes numbers, providing mathematical properties and interesting facts. Built for the HNG Stage 2 Backend Task.

## 🚀 Live Demo
- API Endpoint: [Your Railway URL]
- Documentation: [Your Documentation URL]

## ✨ Features

- **Number Properties Analysis**
  - Prime number detection
  - Perfect number verification
  - Armstrong number identification
  - Odd/Even classification
  - Digit sum calculation
  
- **Additional Features**
  - Fun mathematical facts from Numbers API
  - Cross-Origin Resource Sharing (CORS) support
  - Fast response time (< 500ms)
  - Comprehensive error handling
  - JSON response format

## 📖 API Documentation

### Base URL
```
https://[your-railway-url]/api
```

### Endpoints

#### Get Number Properties
```http
GET /classify-number?number={integer}
```

##### Parameters
| Name   | Type    | Description                |
|--------|---------|----------------------------|
| number | integer | The number to be analyzed  |

##### Success Response (200 OK)
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number..."
}
```

##### Error Response (400 Bad Request)
```json
{
    "number": "invalid_input",
    "error": true
}
```

### Property Definitions

- **is_prime**: True if the number is only divisible by 1 and itself
- **is_perfect**: True if the number equals the sum of its proper divisors
- **properties**: Array containing combinations of:
  - "armstrong" - if the sum of its digits raised to the power of number of digits equals the number
  - "odd"/"even" - based on number's parity
  - "negative" - for negative numbers
- **digit_sum**: Sum of all digits in the absolute value of the number
- **fun_fact**: Interesting mathematical fact about the number

## 🛠️ Technology Stack

- Python 3.13.1
- Django 5.1.5
- Django REST Framework
- Railway for deployment
- Numbers API integration

## ⚙️ Local Development

1. **Clone the Repository**
```bash
git clone https://github.com/asaiah4812/dreamer-hng-task2.git
cd dreamer-hng-task2
```

2. **Set Up Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Run Development Server**
```bash
python manage.py migrate
python manage.py runserver
```

5. **Access the API**
```
http://localhost:8000/api/classify-number?number=371
```

## 🚀 Deployment

This project is configured for deployment on Railway:

1. Push your code to GitHub
2. Connect your GitHub repository to Railway
3. Add environment variables:
   - `SECRET_KEY`: Your Django secret key
   - `DEBUG`: False
4. Deploy!


## ⚡ Performance Optimizations

- Caching for external API calls
- Optimized mathematical calculations
- Response time monitoring
- Error handling with timeouts

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

## 👨‍💻 Developer

**Asaiah Henson**
- GitHub: [@asaiah4812](https://github.com/asaiah4812)
- Project Link: [dreamer-hng-task2](https://github.com/asaiah4812/dreamer-hng-task2)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Numbers API](http://numbersapi.com) for providing mathematical facts
- HNG Internship for the project requirements
- Django and DRF communities

## 📞 Support

For support, email hensonasaiah21@gmail.com or create an issue in the GitHub repository.
