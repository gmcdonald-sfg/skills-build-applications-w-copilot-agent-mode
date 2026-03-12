import React, { useEffect, useState } from 'react';

const getApiUrl = () => {
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  if (codespace) {
    return `https://${codespace}-8000.app.github.dev/api/workouts/`;
  }
  return 'http://localhost:8000/api/workouts/';
};

export default function Workouts() {
  const [data, setData] = useState([]);
  useEffect(() => {
    const url = getApiUrl();
    console.log('Fetching Workouts from:', url);
    fetch(url)
      .then(res => res.json())
      .then(json => {
        const results = json.results || json;
        setData(results);
        console.log('Workouts data:', results);
      });
  }, []);
  return (
    <div>
      <h2>Workouts</h2>
      <ul>
        {data.map((w, i) => (
          <li key={w.id || i}>{w.name}: {w.description}</li>
        ))}
      </ul>
    </div>
  );
}
