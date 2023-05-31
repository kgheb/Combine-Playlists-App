This app uses the spotipy library to connect to the Spotify API
This app combines multiple spotify playlists into one big playlist while keeping the original playlists intact


To allow the spotify app to access your account:


* Go to https://developer.spotify.com/dashboard and sign in with your spotify account
* Click “create app” at the top right
* Enter the following details
   * App Name: "My App"
   * App Description: "Allows python code to access the Spotify API"
   * Website: leave empty
   * Redirect URI: "https://localhost/"
* Check the agreement and click save
* Click settings at the top right
* Copy your “Client ID” and paste it in the “client-id.txt” file
* Save the file and close
* Click “View client secret”
* Copy your “Client secret” and paste it in the “client-secret.txt” file
* Save the file and close
* You can now close the developer page


Before running the app (App.py), you must run Authentication.py:
* Run Authentication.py
   * You will be redirected to your browser to sign in to spotify
   * When the prompt from spotify pops up to allow access, click “agree”
   * You will be redirected to another webpage beginning with “https://localhost/”
   * Copy the ENTIRE url and paste it into the terminal where the python file is being run (where it says “Enter the URL you were redirected to:”)
   * Press enter
   * The app is now authenticated


Now you can run App.py → follow the instructions within the app to combine your playlists
* NOTE: before running the app, I suggest creating a new playlist that your playlists will be combined into
