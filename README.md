# Buzzfeed NLP Classifier

The project in this repository is used to classify brazilian buzzfeed headline as Clickbait or not.

### Technologies

Python  
Docker  
HTML  
CSS

## Run webapp with Docker

In the webapp folder run in cmd:
```bash
docker build . -t buzzfeed
```

After the image is built, run:
```bash
docker run -d --network="host" buzzfeed
```

To access the webapp, go to
```bash
localhost:5000
```