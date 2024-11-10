// src/App.js
import React from 'react';
import SensorData from './graph';

function App() {
  return (
    <div className="App">
      <h1>Raspberry Pi Sensor Dashboard</h1>
      <SensorData />
    </div>
  );
}

export default App;
