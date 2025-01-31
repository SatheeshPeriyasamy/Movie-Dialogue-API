from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

dialogues = [
    {"movie": "The Godfather", "dialogue": "I'm going to make him an offer he can't refuse."},
    {"movie": "The Dark Knight", "dialogue": "Why so serious?"},
    {"movie": "Titanic", "dialogue": "I'm the king of the world!"},
    {"movie": "Forrest Gump", "dialogue": "Life is like a box of chocolates. You never know what you're gonna get."},
    {"movie": "Star Wars", "dialogue": "May the Force be with you."},
    {"movie": "Gladiator", "dialogue": "Are you not entertained?"},
    {"movie": "The Terminator", "dialogue": "I'll be back."},
    {"movie": "Scarface", "dialogue": "Say hello to my little friend!"},
    {"movie": "Rocky", "dialogue": "It ain't about how hard you hit. It's about how hard you can get hit and keep moving forward."},
    {"movie": "Jaws", "dialogue": "You're gonna need a bigger boat."}
]

@app.get("/")
def home():
    return {"message": "Welcome to the Movie Dialogue API!"}

@app.get("/random-dialogue")
def get_random_dialogue():
    return random.choice(dialogues)

@app.get("/dialogue/{movie_name}")
def get_dialogue_by_movie(movie_name: str):
    result = [d for d in dialogues if d["movie"].lower() == movie_name.lower()]
    return result if result else {"error": "Movie not found"}
