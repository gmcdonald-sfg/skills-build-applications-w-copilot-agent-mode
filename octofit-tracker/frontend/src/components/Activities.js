import React, { useEffect, useState } from 'react';

const getApiUrl = () => {
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  if (codespace) {
    return `https://${codespace}-8000.app.github.dev/api/activities/`;
  }
  return 'http://localhost:8000/api/activities/';
};

export default function Activities() {
  const [data, setData] = useState([]);
  useEffect(() => {
    const url = getApiUrl();
    console.log('Fetching Activities from:', url);
    fetch(url)
      .then(res => res.json())
      .then(json => {
        const results = json.results || json;
        setData(results);
        console.log('Activities data:', results);
      });
  }, []);
  return (
    <div>
      <h2>Activities</h2>
      <ul>
        {data.map((a, i) => (
          <li key={a.id || i}>{a.user?.name || a.user} - {a.workout?.name || a.workout} ({a.date})</li>
        ))}
      </ul>
    </div>
  );
}
