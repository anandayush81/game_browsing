# Games
#### Browsing games for different plateforms
## Setup instructions

### Server

  - #### Step 1 (optional but recommended)

     Create a python virtual environment by using virtualenv or conda
     
     ```bash
     python -m venv env && source venv/bin/activate
     ```
  - #### Step 2
    Clone this repo
    ```bash
    git clone https://github.com/Vishnu44d/game_browsing.git && cd env
    ```

  - #### Step 3
    Install dependencies
    ```bash
    pip3 install -r requirements.txt
    ```
  - #### Step 4
    - running the server
      ```bash
        python3 server.py
      ```

## Api
  The Api end points are `'\'`
  - ### /games/
  ```javascript
  {
    "status": "OK/Fail",
    "data/message": "data or error message" 
  }
  ```
  ## Example of games api
  ```javascript
  {
      "platform": "PlayStation Vita"	
  }
  ```
  ### Output of above request
 ```javascript
    {
        "data": [
            {
            "editors_choice": true,
            "genre": "Platformer",
            "plateform": "PlayStation Vita",
            "score": 9.0,
            "title": "LittleBigPlanet PS Vita"
            },
            {
            "editors_choice": true,
            "genre": "Platformer",
            "plateform": "PlayStation Vita",
            "score": 9.0,
            "title": "LittleBigPlanet PS Vita -- Marvel Super Hero Edition"
            },
            {
            "editors_choice": true,
            "genre": "Sports",
            "plateform": "PlayStation Vita",
            "score": 6.0,
            "title": "Madden NFL 13"
            },
            {
            "editors_choice": true,
            "genre": "Sports",
            "plateform": "PlayStation Vita",
            "score": 4.0,
            "title": "FIFA Soccer 13"
            },
            {
            "editors_choice": true,
            "genre": "RPG",
            "plateform": "PlayStation Vita",
            "score": 5.8,
            "title": "New Little King's Story"
            }
        ],
        "status": "OK"
    }
```

  Example of search api
  ```javascript
  {
      "title": "NHL 13"	
  }
  ```
   ### Output of above request
   ```javascript
  {
    "data": [
        {
        "editors_choice": true,
        "genre": "Sports",
        "plateform": "Xbox 360",
        "score": 8.5,
        "title": "NHL 13"
        }
    ],
    "status": "OK"
}
```