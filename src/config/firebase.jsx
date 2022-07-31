import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';
import 'firebase/compat/firestore';

const firebaseConfig = {
  apiKey: 'AIzaSyB7fUCM702lDAff1TKvV8UC69YX3R3CyD0',

  authDomain: 'auth-dev-9e577.firebaseapp.com',

  projectId: 'auth-dev-9e577',

  storageBucket: 'auth-dev-9e577.appspot.com',

  messagingSenderId: '746222309018',

  appId: '1:746222309018:web:1a12d0d12fbfa9b8479923',
};

const app = firebase.initializeApp(firebaseConfig);

export default app;
export const auth = firebase.auth();
export const db = firebase.firestore();
