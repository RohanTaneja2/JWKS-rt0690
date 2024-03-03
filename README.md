# JWKS Server

This is a simple implementation of a JWKS (JSON Web Key Set) server using Python and Flask. The server provides public keys with unique identifiers (kid) for verifying JSON Web Tokens (JWTs), implements key expiry for enhanced security, and includes an authentication endpoint.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Requirements

To run the JWKS server, you need the following dependencies:

- Python 3.x
- Flask
- cryptography
- python-jose

You can install these dependencies using pip:

```
pip install flask cryptography python-jose
```

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/jwks-server.git
```

2. Navigate to the project directory:

```
cd jwks-server
```

## Usage

To start the server, run the following command:

```
python app.py
```

The server will start on port 8080 by default.

## Endpoints

The server provides the following endpoints:

- `/jwks`: Returns public keys in JWKS format.
- `/auth`: Authentication endpoint that returns a signed JWT.

## Testing

A basic test suite is included in the `tests` directory. To run the tests, execute the following command:

```
python -m unittest discover tests
```
