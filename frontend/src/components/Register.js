// src/components/Register.js

import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import Navbar from './Navbar';
import FooterSmall from './FooterSmall';

// Bilder importieren (falls benötigt)
import registerBgImage from '../assets/img/register_bg_2.png';

const Register = () => {
  // Zustandsvariablen für die Eingabefelder
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [birthday, setBirthday] = useState('');

  // Funktion zum Behandeln des Registrierungsformulars
  const handleSubmit = async (e) => {
    e.preventDefault();

    // POST-Request an den Server senden
    try {
      const response = await fetch('http://localhost:5000/create_person', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ first_name: firstName, last_name: lastName, email, password, birthday }),
      });

      const data = await response.json();

      if (response.ok) {
        // Erfolgreiche Registrierung
        alert('Registrierung erfolgreich!');
        // Weiterleitung oder weitere Aktionen hier
      } else {
        // Fehlgeschlagene Registrierung
        alert('Registrierung fehlgeschlagen: ' + data.message);
      }
    } catch (error) {
      console.error('Fehler bei der Registrierung:', error);
      alert('Ein Verbindungsfehler ist aufgetreten.');
    }
  };

  return (
    <>
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
              <div className="w-full lg:w-6/12 px-4">
                {/* Registrierungsformular */}
                <div className="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-white border-0">
                  <div className="rounded-t mb-0 px-6 py-6">
                    <div className="text-center">
                      <h6 className="text-gray-500 text-sm font-bold">
                        Erstelle ein Konto
                      </h6>
                    </div>
                    <hr className="mt-6 border-b-1 border-gray-300" />
                  </div>
                  <div className="flex-auto px-4 lg:px-10 py-10 pt-0">
                    <form onSubmit={handleSubmit}>
                      {/* Vorname */}
                      <div className="relative w-full mb-3">
                        <label
                          className="block uppercase text-gray-700 text-xs font-bold mb-2"
                          htmlFor="first_name"
                        >
                          Vorname
                        </label>
                        <input
                          type="text"
                          id="first_name"
                          value={firstName}
                          onChange={(e) => setFirstName(e.target.value)}
                          required
                          className="border-0 px-3 py-3 rounded text-sm shadow focus:outline-none focus:ring w-full"
                          placeholder="Vorname eingeben"
                        />
                      </div>
                      {/* Nachname */}
                      <div className="relative w-full mb-3">
                        <label
                          className="block uppercase text-gray-700 text-xs font-bold mb-2"
                          htmlFor="last_name"
                        >
                          Nachname
                        </label>
                        <input
                          type="text"
                          id="last_name"
                          value={lastName}
                          onChange={(e) => setLastName(e.target.value)}
                          required
                          className="border-0 px-3 py-3 rounded text-sm shadow focus:outline-none focus:ring w-full"
                          placeholder="Nachname eingeben"
                        />
                      </div>
                      {/* E-Mail */}
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
                      {/* Passwort */}
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
                      {/* Geburtsdatum */}
                      <div className="relative w-full mb-3">
                        <label
                          className="block uppercase text-gray-700 text-xs font-bold mb-2"
                          htmlFor="birthday"
                        >
                          Geburtsdatum
                        </label>
                        <input
                          type="date"
                          id="birthday"
                          value={birthday}
                          onChange={(e) => setBirthday(e.target.value)}
                          required
                          className="border-0 px-3 py-3 rounded text-sm shadow focus:outline-none focus:ring w-full"
                          placeholder="Geburtsdatum eingeben"
                        />
                      </div>
                      <div className="flex items-center">
                        <label className="inline-flex items-center cursor-pointer">
                          <input
                            id="customCheckRegister"
                            type="checkbox"
                            className="form-checkbox border-0 rounded text-gray-800 ml-1 w-5 h-5 ease-linear transition-all duration-150"
                            required
                          />
                          <span className="ml-2 text-sm font-semibold text-gray-700">
                            Ich stimme den{' '}
                            <a href="#agb" className="text-blue-500 hover:text-blue-700">
                              Nutzungsbedingungen
                            </a>{' '}
                            zu.
                          </span>
                        </label>
                      </div>
                      <div className="text-center mt-6">
                        <button
                          className="bg-gray-800 text-white active:bg-gray-600 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg focus:outline-none w-full"
                          type="submit"
                        >
                          Registrieren
                        </button>
                      </div>
                    </form>
                  </div>
                </div>
                <div className="flex flex-wrap mt-6 relative z-10">
                  <div className="w-full text-center">
                    <Link to="/" className="text-gray-700 hover:text-gray-900">
                      <small>Bereits ein Konto? Einloggen</small>
                    </Link>
                  </div>
                </div>
              </div>
            </div>
          </div>
          {/* Footer mit absolute Positionierung */}
          <FooterSmall absolute />
        </section>
      </main>
    </>
  );
};

export default Register;
