This app uses the spotipy library to connect to the Spotify API
The "Combine-App" app combines all of your spotify playlists into one big playlist while keeping the original playlists intact
The "Delete-App" app deletes songs that are in a big playlist and not in any of your other playlists


Run the following in your python terminal before running the python files:
   "pip install spotipy"


To allow the spotify apps to access your account:

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


Before running the apps (Combine-App.py and Delete-App.py), you must run Authentication.py:

* Run Authentication.py
   * You will be redirected to your browser to sign in to spotify
   * When the prompt from spotify pops up to allow access, click “agree”
   * You will be redirected to another webpage beginning with “https://localhost/” (Note: you will get a connection error, this is fine, just proceed to the next step)
   * Copy the ENTIRE url and paste it into the terminal where the python file is being run (where it says “Enter the URL you were redirected to:”)
   * Press enter
   * The app is now authenticated


Now you can run Combine-App.py and Delete-App.py → follow the instructions within the app to combine your playlists

NOTES:
* Before running the app, I suggest creating a new playlist that your playlists will be combined into 
* Any playlists you do not want to add to your everything playlist should be private on your profile. This app will only combine your public playlists
* The apps take a long time to run. The app will close automatically 5 seconds after finishing
* If the app closes suddenly while running, it was most likely an error with the Spotify API. Try the app again, if the error ocurrs again, wait some time before retrying
