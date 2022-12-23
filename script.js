// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyByyvG_8PTsyPeDSbvBJj252oNa_zdYEBU",
  authDomain: "birdpi-35dd0.firebaseapp.com",
  databaseURL: "https://birdpi-35dd0-default-rtdb.europe-west1.firebasedatabase.app",
  projectId: "birdpi-35dd0",
  storageBucket: "birdpi-35dd0.appspot.com",
  messagingSenderId: "987008306339",
  appId: "1:987008306339:web:acca21820342749c818316"
};

firebase.initializeApp(firebaseConfig);

// Get a reference to the file storage service
const storage = firebase.storage();
// Get a reference to the database service
const database = firebase.database();

// Create camera database reference
const camRef = database.ref("file");

// Sync on any updates to the DB. THIS CODE RUNS EVERY TIME AN UPDATE OCCURS ON THE DB.
camRef.limitToLast(1).on("value", function(snapshot) {
  snapshot.forEach(function(childSnapshot) {
    const image = childSnapshot.val()["image"];
    const time = childSnapshot.val()["timestamp"];
    const storageRef = storage.ref(image);

    storageRef
      .getDownloadURL()
      .then(function(url) {
        console.log(url);
        document.getElementById("photo").src = url;
        document.getElementById("time").innerText = time;
      })
      .catch(function(error) {
        console.log(error);
      });
  });
});