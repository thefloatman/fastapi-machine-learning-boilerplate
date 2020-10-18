# FastAPI + Machine Learning Boilerplate

I learn how to stucture a coding project from zero

## What is inside?

Boilerplate to build Machine Learning API with FastAPI

### Prerequisites

```bash
1. Uvicorn + FastApi
2. Vader

```

## Deployment

Already Deploy to [Heroku](www.heroku.com)

## How to Run it in Local

```bash
pip install -r requirements.txt
```

```bash
uvicorn src.main:app --host=0.0.0.0
```

or

```bash
docker-compose up -d
```

## How to Use the API

Go to here

```bash
http://0.0.0.0:8000/docs
```

or

```bash
curl -X POST --header "Accept: application/json" --header "Content-Type: application/json" -d "{
  \"sentence\": \"Everyone is good\"
}" "http://localhost:8000/analyze"
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
