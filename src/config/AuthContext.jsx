import React, {useContext, useEffect, useState} from 'react';
import {deleteDoc, doc, getDoc} from 'firebase/firestore';

import {auth, db} from './firebase';

const AuthContext = React.createContext();

export function useAuth() {
  return useContext(AuthContext);
}

export function AuthProvider({ children }) {
  const [loading, setLoading] = useState(true);
  const [currentUser, setCurrentUser] = useState();

  async function signup(email, password) {
    const cred = await auth.createUserWithEmailAndPassword(email, password);
    await db.collection('users').doc(cred.user.uid).set({
      email: cred.user.email,
    });
  }

  function login(email, password) {
    return auth.signInWithEmailAndPassword(email, password);
  }

  function logout() {
    return auth.signOut();
  }

  async function getMoviesCollectionData() {
    // * fetch the stored movies in the firestore movie collection
    const firestoreMoviesResponse = [];
    const data = await db.collection('movies').get();
    data.docs.forEach((element) => {
      firestoreMoviesResponse.push(element.data());
    });
    return firestoreMoviesResponse;
  }

  async function storeMovieInCollection(movie) {
    /**
     * @param movie takes in a movie json which is to be stored in the movies
     * collection.
     */
    await db.collection('movies').doc(movie.title).set(movie);
  }

  const checkForDocExistence = async (movieDoc) => {
    const docRef = doc(db, 'movies', movieDoc);
    const docSnap = await getDoc(docRef);

    return !!docSnap.exists();
  };

  const deleteMovieFromCollection = async (movieDoc) => {
    await deleteDoc(doc(db, 'movies', movieDoc));
  };

  useEffect(() => {
    // Listen for authentication status changes
    return auth.onAuthStateChanged((user) => {
      try {
        user
            ? console.log(user.email, 'is logged in')
            : console.log('Currently no user is logged in');
      } catch (error) {
        console.log('error thrown :', error);
      }
      setCurrentUser(user);
      setLoading(false);
    });
  }, []);

  const value = {
    currentUser,
    signup,
    login,
    logout,
    getMoviesCollectionData,
    storeMovieInCollection,
    deleteMovieFromCollection,
    checkForDocExistence,
  };

  return (
    <AuthContext.Provider value={value}>
      {loading ? <div>loading...</div> : children}
    </AuthContext.Provider>
  );
}
