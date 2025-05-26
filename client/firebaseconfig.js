import { initializeApp } from "firebase/app";
import { getAuth, TwitterAuthProvider, signInWithPopup } from "firebase/auth";

const firebaseConfig = {
    apiKey: "AIzaSyCJgxeHXbY7xDRS61AhkuuW2BI1hfpuL7o",
    authDomain: "tweet-analytica.firebaseapp.com",
    projectId: "tweet-analytica",
    storageBucket: "tweet-analytica.firebasestorage.app",
    messagingSenderId: "642062098119",
    appId: "1:642062098119:web:942a39509d5be1e69468e2",
    measurementId: "G-E4RRW5LRPW"
  };

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const twitterProvider = new TwitterAuthProvider();

const signInWithTwitter = async () => {
  try {
    const result = await signInWithPopup(auth, twitterProvider);
    console.log("User Info:", result.user);
    return result.user;
  } catch (error) {
    console.error("Twitter Sign-In Error:", error);
  }
};

export { auth, signInWithTwitter };
