

  const firebaseConfig = {
    apiKey: "AIzaSyAMpOREfPKWyOnedRqVgRsfNZhsxL3UVhw",
    authDomain: "commenttoxy.firebaseapp.com",
    databaseURL: "https://commenttoxy-default-rtdb.firebaseio.com",
    projectId: "commenttoxy",
    storageBucket: "commenttoxy.appspot.com",
    messagingSenderId: "824521023168",
    appId: "1:824521023168:web:b9ed9ac64ac8ede9149725",
    measurementId: "G-HVQVD307FE"
  };

   firebase.initializeApp(firebaseConfig);
  var contactform = firebase.database().ref("contactform")

  document.getElementById('contactform').addEventListener("submit",submitform)

  function submitform (e) {
    e.preventDefault(); // Prevent the default form submission
    // Check if Firebase has been initialized
    if (typeof firebase === 'undefined' || !firebase.app.length) {
      console.error('Firebase is not properly initialized.');
      return;
    }
    var name= getElementVal("username");
    var email= getElementVal("password");
    console.log(username,password);
  }
    // Get form data
    const getElementVal =(id) => {
        return document.getElementById(id).value;
    }
    // Store data in Firebase Realtime Database

