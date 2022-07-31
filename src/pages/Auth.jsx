import React, { useState } from 'react';
import { useHistory } from 'react-router';

import './Auth.css';
import {useAuth} from "../config/AuthContext";

const Auth = () => {
  const history = useHistory();
  const { login } = useAuth();
  const { signup } = useAuth();
  let [authMode, setAuthMode] = useState('signin');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [name, setName] = useState('');

  const changeAuthMode = () => {
    setAuthMode(authMode === 'signin' ? 'signup' : 'signin');
  };

  const signInHandler = async (e) => {
    e.preventDefault();
    try {
      await login(email, password);
      alert('Login Successful')
      history.push('/')
      setEmail('')
      setPassword('')
    } catch (error) {
      alert('Wrong email or password');
    }
  };

  const signUpHandler = async (e) => {
    console.log(name)
    e.preventDefault();
    try {
      await signup(email, password);
      alert('Signup Successful')
      setName('')
      setEmail('')
      setPassword('')
      changeAuthMode()
    } catch (error) {
      alert('Signup Error');
    }
  };

  if (authMode === 'signin') {
    return (
      <div className='Auth-form-container'>
        <form className='Auth-form'>
          <div className='Auth-form-content'>
            <h3 className='Auth-form-title'>Sign In</h3>
            <label>Email address</label>
            <div style={{display: 'flex', justifyContent: 'center'}}>
              <input
                type='email'
                className='form-control mt-1'
                placeholder='Enter email'
                onChange={(e) => {
                  setEmail(e.target.value);
                }}
              />
            </div>
            <label>Password</label>
            <div style={{display: 'flex', justifyContent: 'center'}}>
              <input
                type='password'
                className='form-control mt-1'
                placeholder='Enter password'
                onChange={(e) => {
                  setPassword(e.target.value);
                }}
              />
            </div>
            <div style={{display: 'flex', justifyContent: 'center'}}>
              <button style={{fontWeight: 'bold', margin: '10px 0', borderRadius: '20px', padding: '1em 2em', background: 'red', outline: 'none', border: 'none', color: 'white'}} onClick={signInHandler} type='submit'>
                Submit
              </button>
            </div>
            <div style={{color: 'black', textAlign: 'center'}} className='text-center'>
              Not registered yet?{' '}
              <span style={{color: 'red', cursor: 'pointer'}} className='link-primary' onClick={changeAuthMode}>
                Sign Up
              </span>
            </div>
            {/* <p className='text-center mt-2'>
              Forgot <a href='#'>password?</a>
            </p> */}
          </div>
        </form>
      </div>
    );
  }

  return (
      <div className='Auth-form-container'>
        <form className='Auth-form'>
          <div className='Auth-form-content'>
            <h3 className='Auth-form-title'>Sign Up</h3>
            <label>Full Name</label>
            <div style={{display: 'flex', justifyContent: 'center'}}>
              <input
                  type='text'
                  className='form-control mt-1'
                  placeholder='e.g Jane Doe'
                  onChange={(e) => {
                    setName(e.target.value);
                }}
              />
            </div>
            <label>Email address</label>
            <div style={{display: 'flex', justifyContent: 'center'}}>
              <input
                  type='email'
                  className='form-control mt-1'
                  placeholder='Enter email'
                  onChange={(e) => {
                    setEmail(e.target.value);
                }}
              />
            </div>
            <label>Password</label>
            <div style={{display: 'flex', justifyContent: 'center'}}>
              <input
                  type='password'
                  className='form-control mt-1'
                  placeholder='Enter password'
                  onChange={(e) => {
                  setPassword(e.target.value);
                }}
              />
            </div>
            <div style={{display: 'flex', justifyContent: 'center'}}>
              <button style={{fontWeight: 'bold', margin: '10px 0', borderRadius: '20px', padding: '1em 2em', background: 'red', outline: 'none', border: 'none', color: 'white'}} onClick={signUpHandler} type='submit'>
                Submit
              </button>
            </div>
            <div style={{color: 'black', textAlign: 'center'}} className='text-center'>
              Already have an account?{' '}
              <span style={{color: 'red', cursor: 'pointer'}} className='link-primary' onClick={changeAuthMode}>
                Sign In
              </span>
            </div>
            {/* <p className='text-center mt-2'>
              Forgot <a href='#'>password?</a>
            </p> */}
          </div>
        </form>
      </div>
  );
};

export default Auth;
