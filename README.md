# Face Detection

## Getting Started

This is my full stack machine learning project

### Prerequisites

What things you need to use it

```
1. Uvicorn + FastApi
2. Vader

```

## Deployment

Already Deploy to [this link](https://sonos-app.netlify.app)

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

Please read [CONTRIBUTING.md](https://github.com/rainoverme002/sonos-project) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

[rainoverme002](https://github.com/rainoverme002)

See also the list of [contributors](https://github.com/rainoverme002/sonos-project) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks for all of the contribution from the republic of internet

## Quotes of the Day

* Stay learning and you will get what you want
