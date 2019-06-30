"""

    Open Google ... Login to Console google firebase
    Go to Console... Create new Project
    Go to Database


    Go to Project overview ... go to settings... project settings... service accounts...
    Generate new Private key


"""


var admin = require("firebase-admin");

var serviceAccount = require("path/to/serviceAccountKey.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://project1-7a222.firebaseio.com"
});
