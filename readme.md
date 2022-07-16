<h3 align="center">Coffee Notes</h3>

  <p align="center">
    Coffee journaling app that allows users to track their dial in processes with each new bag for the best taste and experience.
    <br />



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>

</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

   I am a passionate coffee lover who is constantly bringing home new bags to try. Each new coffee requires slightly different settings (grind size, extraction method) for best results. I created Coffee Apps to track each new bag and experience. 
    <br/>
    Coffee Notes stores all user entries in their dashboard. Users can add or update a coffee anytime. The fields being tracked are name, image, grind setting, brewing method, rating, flavor notes, and general thoughts. Through modified entries, users have the ability to fine tune each bag to produce the best cup. 
<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [React.js](https://reactjs.org/)
* [Django](https://www.djangoproject.com/)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get your own local version of this app follow these steps...

### Prerequisites

For ease of use it is suggested to use npm. If you do now have npm you can install it using the command below
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/destinyfrith/coffeenotes-api.git
   ```
2. Create virtual environment
   ```sh
   pipenv shell
   ```
3. Install requirements
   ```sh
   pipenv install -r requirements.txt
   ```
4. Create .env file in project root for secret key 
5. Run command for random secret key and paste key into .env file
  ```sh
   python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
   ```
6. Run makemigrations, migrate, and loaddata to set up server models and dummy data
7. Clone/Open [React client](https://github.com/destinyfrith/coffeenotes-client)


