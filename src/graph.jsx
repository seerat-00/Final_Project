// src/components/SensorData.js
import React, { useEffect, useState } from 'react';
import { database, ref, onValue } from './firebase';  // Import functions from the updated Firebase module

const SensorData = () => {
  const [sensorData, setSensorData] = useState([]);

  useEffect(() => {
    const sensorDataRef = ref(database, 'sensor_data');
    
    // Listen for changes to the sensor_data node
    onValue(sensorDataRef, (snapshot) => {
      const data = snapshot.val();
      const dataList = [];
      
      // Convert object data to an array
      for (let id in data) {
        dataList.push(data[id]);
      }

      setSensorData(dataList);
    });

    // Cleanup listener on unmount
    return () => {
      // Firebase automatically handles cleanup of listeners, so we don't need to manually remove it here
    };
  }, []);

  return (
    <div>
      <h2>Sensor Data</h2>
      <ul>
        {sensorData.map((data, index) => (
          <li key={index}>
            <p>Timestamp: {new Date(data.timestamp * 1000).toLocaleString()}</p>
            <p>Relay State: {data.arduino_relay_state}</p>
            <p>Soil Moisture: {data.arduino_soil_moisture}</p>
            <p>Temperature: {data.dht22_temperature} °C</p>
            <p>Humidity: {data.dht22_humidity} %</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default SensorData;
