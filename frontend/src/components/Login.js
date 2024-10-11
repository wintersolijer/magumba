// src/components/Login.js

import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import Navbar from './Navbar';
import FooterSmall from './FooterSmall';

// Bilder importieren
import registerBgImage from '../assets/img/register_bg_2.png';
import githubIcon from '../assets/img/github.svg';
import googleIcon from '../assets/img/google.svg';

const Login = () => {
  // Zustandsvariablen für E-Mail und Passwort
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  // Funktion zum Behandeln des Login-Formulars
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });

      const data = await response.json();

      if (response.ok) {
        // Erfolgreiches Login
        alert('Login erfolgreich!');
        // Weiterleitung oder weitere Aktionen hier
      } else {
        // Fehlgeschlagenes Login
        alert('Login fehlgeschlagen: ' + data.message);
      }
    } catch (error) {
      console.error('Fehler beim Login:', error);
      alert('Ein Verbindungsfehler ist aufgetreten.');
    }
  };

  // Mock-Funktion für Google Login
  const handleMockGoogleLogin = () => {
    // Simulierte Benutzerinformationen
    const mockUser = {
      name: 'Max Mustermann',
      email: 'max.mustermann@example.com',
      // Weitere Benutzerinformationen
    };

    console.log('Mock Google User:', mockUser);
    alert('Mock Google Login erfolgreich!');
    // Hier kannst du weitere Aktionen durchführen, z.B. Weiterleitung
  };

  return (
    <>
      {/* Navbar */}
      <Navbar transparent />
      <main>
        <section className="relative w-full h-full py-40 min-h-screen">
          {/* Hintergrundbild */}
          <div
            className="absolute top-0 w-full h-full bg-blueGray-800 bg-no-repeat bg-full"
            style={{
              backgroundImage: `url(${registerBgImage})`,
            }}
          ></div>
          <div className="container mx-auto px-4 h-full">
            <div className="flex content-center items-center justify-center h-full">
              <div className="w-full lg:w-4/12 px-4">
                {/* Login-Formular */}
                <div className="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-white border-0">
                  <div className="rounded-t mb-0 px-6 py-6">
                    <div className="text-center mb-3">
                      <h6 className="text-gray-500 text-sm font-bold">
                        Melde dich an mit
                      </h6>
                    </div>
                    <div className="btn-wrapper text-center">
                      {/* GitHub Login Button */}
                      <button
                        className="bg-white active:bg-gray-50 text-gray-700 font-normal px-4 py-2 rounded shadow hover:shadow-md inline-flex items-center font-bold text-xs mr-2"
                        type="button"
                        style={{ transition: 'all .15s ease' }}
                      >
                        <img alt="GitHub" className="w-5 mr-1" src={githubIcon} />
                        GitHub
                      </button>
                      {/* Mock Google Login Button */}
                      <button
                        className="bg-white active:bg-gray-50 text-gray-700 font-normal px-4 py-2 rounded shadow hover:shadow-md inline-flex items-center font-bold text-xs"
                        type="button"
                        onClick={handleMockGoogleLogin}
                        style={{ transition: 'all .15s ease' }}
                      >
                        <img alt="Google" className="w-5 mr-1" src={googleIcon} />
                        Google
                      </button>
                    </div>
                    <hr className="mt-6 border-b-1 border-gray-300" />
                  </div>
                  <div className="flex-auto px-4 lg:px-10 py-10 pt-0">
                    <div className="text-gray-500 text-center mb-3 font-bold">
                      <small>Oder melde dich mit deinen Zugangsdaten an</small>
                    </div>
                    <form onSubmit={handleSubmit}>
                      <div className="relative w-full mb-3">
                        <label
                          className="block uppercase text-gray-700 text-xs font-bold mb-2"
                          htmlFor="email"
                        >
                          E-Mail
                        </label>
                        <input
                          type="email"
                          id="email"
                          value={email}
                          onChange={(e) => setEmail(e.target.value)}
                          required
                          className="border-0 px-3 py-3 rounded text-sm shadow focus:outline-none focus:ring w-full"
                          placeholder="E-Mail eingeben"
                        />
                      </div>
                      <div className="relative w-full mb-3">
                        <label
                          className="block uppercase text-gray-700 text-xs font-bold mb-2"
                          htmlFor="password"
                        >
                          Passwort
                        </label>
                        <input
                          type="password"
                          id="password"
                          value={password}
                          onChange={(e) => setPassword(e.target.value)}
                          required
                          className="border-0 px-3 py-3 rounded text-sm shadow focus:outline-none focus:ring w-full"
                          placeholder="Passwort eingeben"
                        />
                      </div>
                      <div className="flex items-center">
                        <label className="inline-flex items-center cursor-pointer">
                          <input
                            id="customCheckLogin"
                            type="checkbox"
                            className="form-checkbox border-0 rounded text-gray-800 ml-1 w-5 h-5 ease-linear transition-all duration-150"
                          />
                          <span className="ml-2 text-sm font-semibold text-gray-700">
                            Merken
                          </span>
                        </label>
                      </div>
                      <div className="text-center mt-6">
                        <button
                          className="bg-gray-800 text-white active:bg-gray-600 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg focus:outline-none w-full"
                          type="submit"
                        >
                          Einloggen
                        </button>
                      </div>
                    </form>
                  </div>
                </div>
                <div className="flex flex-wrap mt-6 relative z-10">
                  <div className="w-1/2">
                    <a
                      href="#passwort-vergessen"
                      className="text-gray-700 hover:text-gray-900"
                    >
                      <small>Passwort vergessen?</small>
                    </a>
                  </div>
                  <div className="w-1/2 text-right">
                    <Link to="/register" className="text-gray-700 hover:text-gray-900">
                      <small>Jetzt registrieren</small>
                    </Link>
                  </div>
                </div>
              </div>
            </div>
          </div>
          {/* Footer */}
          <FooterSmall absolute />
        </section>
      </main>
    </>
  );
};

export default Login;
