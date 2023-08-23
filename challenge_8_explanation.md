### Steps to Create an Inventory Item via the Django Shell
1. Get into the django shell by running `python manage.py shell`
2. Import the models by running `from interview.inventory.models import Inventory, InventoryType, InventoryLanguage, InventoryTag`
3. You'll need to locate the correct `InventoryType` and `InventoryLanguage`:
   ```
   type = InventoryType.objects.get(name='Movie')
   language = InventoryLanguage.objects.get(name='English')
   ```
4. Create the inventory item:
   ```
   item = Inventory.objects.create(
       name='<Your Movie Title>',
       type=type,
       language=language,
       metadata={
        "year": <YEAR>,
        "actors": [<LIST OF ACTORS>],
        "imdb_rating": <IMDB RATING>,
        "rotten_tomatoes_rating": <ROTTEN TOMATOES RATING>,
        "film_locations": [<LIST OF FILM LOCATIONS>],
       }
   )
   ```
   You'll need to replace the following:
    - `<Your Movie Title>` with the title of the movie you're adding
    - `<YEAR>` with the year the movie was released
    - `<LIST OF ACTORS>` with a list of actors in the movie
    - `<IMDB RATING>` with the IMDB rating of the movie
    - `<ROTTEN TOMATOES RATING>` with the Rotten Tomatoes rating of the movie
    - `<LIST OF FILM LOCATIONS>` with a list of film locations for the movie
5. If you would like to include tags, you can do so by running:
   ```
   tag = InventoryTag.objects.get(name='<TAG NAME>')
   item.tags.add(tag)
   ```
   You'll need to replace `<TAG NAME>` with the name of the tag you want to add.  You can add as many tags as you want by repeating the last line with a different tag name.

### Steps to Create an Inventory Item via the API (Browser)
1. Activate the virtual environment by running `source .venv/bin/activate`
2. Start the server by running `./manage.py runserver 0.0.0.0:8000`.  You may need to run `python manage.py migrate` first.
3. In your browser, navigate to `http://localhost:8000/inventory/`
4. Fill out the form on the bottom of the page and click `POST`.  The metadata field should contain the following:
   ```
    {
        "year": <YEAR>,
        "actors": [<LIST OF ACTORS>],
        "imdb_rating": <IMDB RATING>,
        "rotten_tomatoes_rating": <ROTTEN TOMATOES RATING>,
        "film_locations": [<LIST OF FILM LOCATIONS>],
    }
   ```

### Steps to Create an Inventory Item via the API (cURL)
1. Activate the virtual environment by running `source .venv/bin/activate`
2. Start the server by running `./manage.py runserver
3. Run the following command:
   ```
   curl -X POST \
     http://localhost:8000/inventory/ \
     -H 'Content-Type: application/json' \
     -d '{
        "name": "<Your Movie Title>",
        "type": <TYPE ID>,
        "language": <LANGUAGE ID>,
        "tags": [],
        "metadata": {
            "year": <YEAR>,
            "actors": [<LIST OF ACTORS>],
            "imdb_rating": <IMDB RATING>,
            "rotten_tomatoes_rating": <ROTTEN TOMATOES RATING>,
            "film_locations": [<LIST OF FILM LOCATIONS>]
        }
    }'
   ```
   You'll need to replace the following:
    - `<Your Movie Title>` with the title of the movie you're adding
    - `<YEAR>` with the year the movie was released
    - `<LIST OF ACTORS>` with a list of actors in the movie
    - `<IMDB RATING>` with the IMDB rating of the movie
    - `<ROTTEN TOMATOES RATING>` with the Rotten Tomatoes rating of the movie
    - `<LIST OF FILM LOCATIONS>` with a list of film locations for the movie