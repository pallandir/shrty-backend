<a name="readme-top"></a>

<br />
<div align="center">
  <a href="#">
    <img src="./public-assets/logo.svg" alt="Logo" width="80" height="80">
  </a>
  <h3 align="center">Shrty</h3>

  <p align="center">
    Simple URL shortener.
    <br />
    <br />
    <a href="https://github.com/pallandir/shrty-backend/issues">Report Bug</a>
    ·
    <a href="https://github.com/pallandir/shrty-backend/issues">Request Feature</a>
  </p>
</div>

## About This Project

**Shrty** is a fun Python project built to practice clean architecture and good development practices. It includes:

- **Database migrations** using [`alembic`](https://alembic.sqlalchemy.org/)
- **ORM** integration with [`SQLAlchemy`](https://www.sqlalchemy.org/)
- **Repository pattern** and **dependency injection** to decouple database logic from business logic thanks to [`FastAPI`](https://fastapi.tiangolo.com/) integration

URL shorteners are widely used today to map long URLs to shorter, more manageable ones. **Shrty** takes a unique approach by integrating **emojis** into the shortened URLs, a feature rarely seen in other tools.

### Why Emojis?

A typical short URL of 6 characters using uppercase letters and digits (`[A-Z0-9]`, 36 possible characters) can represent: 
36^6 = 2,176,782,336 possible URLs.

Now, consider using just a subset of available emojis — say **1,500** out of the ~3,790 emojis that exist today. A 4-character emoji-based URL gives:
1,500^3 = 3,375,000,000 possible URLs.

Knowing that there are around 1.2 billion website today in the world and 200,000 new ones created everyday, this approach not only supports more mappings than traditional shorteners but also results in **shorter** and more **visually distinctive** URLs.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

first you need to setup your virtual environment and install dependancies

```sh

# Create your virtual environment
python3 venv -m ./venv 

# Activate it
source venv/bin/activate

# Install dependancies
pip install -r requirements/dev.txt
```

Setup your environment variables as defined in .env.example, then start the project:

```sh
python -m app.main # Allow to run the app as a module
```

> [!IMPORTANT]  
> You'll need to setup a proper postgresql instance on your local machine in order to allow connectivity with the app. 


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

This repository and all its content is under `GNU General Public License v3.0`.

<p align="right">(<a href="#readme-top">back to top</a>)</p>