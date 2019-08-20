# Games
#### Browsing games for different plateforms
## Setup instructions

### Server

  - #### Step 1 (optional but recommended)

     Create a python virtual environment by using virtualenv or conda
     ```bash
     conda create -n env python3.6
     ```
     or

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
  - ### /user/
  ```javascript
  {
    "status": "success/fail",
    "data/message": "data or error message" 
  }
  ```