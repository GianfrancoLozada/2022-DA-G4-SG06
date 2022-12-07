
var fs = require("firebase-admin");

var serviceAccount = require("./clave.json");

fs.initializeApp({
  credential: fs.credential.cert(serviceAccount),
  databaseURL: "https://experiencia-3-default-rtdb.firebaseio.com"
});

// Escribir información en BD
const db = fs.firestore();
const GameDB = db.collection('videojuegos');

const HotWheels = GameDB.doc('Unleashed');
HotWheels.set({
  ID: 1023,
  Titulo: 'HotWheels unleashed',
  TamañoGB: 26.87,
  Precio: 60,
});

const Fall = GameDB.doc('Guys');
Fall.set({
  ID: 2388,
  Titulo: 'Fall Guys',
  TamañoGB: 5.81,
  Precio: 0,
});

const GTA = GameDB.doc('V');
GTA.set({
  ID: 9302,
  Titulo: 'GTAV',
  TamañoGB: 72,
  Precio: 100,
});

async function getDocument(db) {
  var muestra = GameDB.doc('Unleashed');
  var doc = await muestra.get();
  if (!doc.exists) {
  console.log('No such document!');
  } else {
  console.log('Document data:', doc.data());
  }
  getDocument(db)
}

const UserDB = db.collection('Usuarios');

const U1 = UserDB.doc('Usuario1');
U1.set({
  ID: 12,
  Nombre:'CatCrash92',
  Email:'Cattalina@emailg.com'
});

const U2 = UserDB.doc('Usuario2');
U2.set({
  ID: 93,
  Nombre:'MGTrappper234',
  Email:'JEduardo@emailg.pe'
});

const U3 = UserDB.doc('Usuario3');
U3.set({
  ID: 63,
  Nombre:'Upsideup',
  Email:'PabloCobrar@emailg.com'
});