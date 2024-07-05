
curl -X POST \
    -H 'Content-Type: application/json' \
    -d '{"user": 3, "crypto": "ABAN", "amount": 1}' \
    'http://localhost:8080/api/buy'
