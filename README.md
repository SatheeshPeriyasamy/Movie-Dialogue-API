# Movie-Dialogue-API

This project is created using FastAPI, which facilitates easier API creation. When this API is queried, it responds with a random movie dialogue, and you can also query with the movie name for a specific dialogue.

## Procedure:

1. Install Python and check if it is installed using:
   ```sh
   python --version
   ```
2. Open the command prompt and type:
   ```sh
   pip install -r Requirements.txt
   ```
3. Run the application using:
   ```sh
   uvicorn main:app --reload
   ```
4. The application starts running at:
   ```
   http://127.0.0.1:8000/
   ```

## API Endpoints:

- **Random dialogue generation:**
  ```
  http://127.0.0.1:8000/random-dialogue
  ```
- **Dialogue search by movie name:**
  ```
  http://127.0.0.1:8000/dialogue/{movieName}
  ```

The `index.html` file contains a simple web page that connects with the created API.

Happy Coding! 😊
