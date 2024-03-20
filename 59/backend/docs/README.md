# ChatGPT4All Backend

This project provides the "Geocoding" API for my GPT, [Action Geo](/Day-59-Action-Geo.md).

## Table of Contents

- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Nginx Configuration](#nginx-configuration)
- [HelloWorld API](#helloworld-api)
  - [Development](#development)
  - [Production](#production)
- [Geocoding API](#geocoding-api)
  - [Development](#development-1)
  - [Production](#production-1)
- [License](#license)

## Setup

### Prerequisites

- Python 3.x
- pip
- Nginx

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/BlueBirdBack/100-Days-of-GPTs
   cd 100-Days-of-GPTs/59/backend
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Nginx Configuration

Configure Nginx to proxy requests to the backend services. Add the following configuration to your Nginx configuration file:

```nginx
server {
    listen 443 ssl;
    server_name chatgpt4all.top;

    ssl_certificate /root/projects/chatgpt4all.top.pem;
    ssl_certificate_key /root/projects/chatgpt4all.top.key;

    location / {
        proxy_pass http://localhost:4318;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /geocode {
        proxy_pass http://localhost:4319;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /reverse {
        proxy_pass http://localhost:4319;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable the configuration by creating a symbolic link:
```bash
ln -s /etc/nginx/sites-available/chatgpt4all.top /etc/nginx/sites-enabled/
```

Reload Nginx:
```bash
systemctl reload nginx
```

## HelloWorld API

Refer to [Day 58 backend](/58/backend/docs/README.md) for the HelloWorld API.

### Development

To run the HelloWorld API in development mode:
```
uvicorn main:app_hello --host 0.0.0.0 --port 4318
```

### Production

To run the HelloWorld API in production mode:
```
nohup uvicorn main:app_hello --host 0.0.0.0 --port 4318 > uvicorn.log 2>&1 &
```

## Geocoding API

The Geocoding API provides geocoding and reverse geocoding functionality using the OpenStreetMap Nominatim service.

### Development

To run the Geocoding API in development mode:
```
uvicorn main:app_geocode --host 0.0.0.0 --port 4319
```

### Production

To run the Geocoding API in production mode:
```
nohup uvicorn main:app_geocode --host 0.0.0.0 --port 4319 > uvicorn.log 2>&1 &
```

## License

This project is licensed under the [MIT License](/LICENSE).
