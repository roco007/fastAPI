Postman cUrl:

curl --location 'http://localhost:8000/P_value1?q_param1=Q_value1' \
--header 'Content-Type: application/json' \
--data '{
    "query": "What is the meaning of life?",
    "prompt": "The meaning of life is..."
}'
