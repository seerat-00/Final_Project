// src/firebase.js
import {initializeApp} from 'firebase/app';
import { getDatabase, ref, onValue } from "firebase/database"; 

const firebaseConfig = {
    apiKey: "AIzaSyD5COSARCdcNU9LmDQO8VXm-sgrb-m1sMQ",
    authDomain: "raspberry-camera-a4a87.firebaseapp.com",
    databaseURL: "https://raspberry-camera-a4a87-default-rtdb.firebaseio.com/",
    projectId: "raspberry-camera-a4a87",
    storageBucket: "raspberry-camera-a4a87.firebasestorage.app",
    messagingSenderId: "262124070899",
    appId: "1:262124070899:web:1fe408ef4b66bdfab45486"
};
  

const app = initializeApp(firebaseConfig);

const database = getDatabase(app);
export { database, ref, onValue }; // 