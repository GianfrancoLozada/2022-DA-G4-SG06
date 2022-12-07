var fs = require("firebase-admin");

var serviceAccount = require("./clave.json");

fs.initializeApp({
  credential: fs.credential.cert(serviceAccount),
  databaseURL: "https://experiencia-3-default-rtdb.firebaseio.com"
});

var db = admmin.database();
var ref = db.ref("server/data");
var usersRef = ref.child("nodejs");
usersRef.set({
  usuarios: {
    names: "Carlos reyes",
    age: 28,
    salary: 2304.54
  }
});