import React, { useEffect, useState } from 'react';

const getApiUrl = () => {
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  if (codespace) {
    return `https://${codespace}-8000.app.github.dev/api/users/`;
  }
  return 'http://localhost:8000/api/users/';
};

export default function Users() {
  const [data, setData] = useState([]);
  useEffect(() => {
    const url = getApiUrl();
    console.log('Fetching Users from:', url);
    fetch(url)
      .then(res => res.json())
      .then(json => {
        const results = json.results || json;
        setData(results);
        console.log('Users data:', results);
      });
  }, []);
  return (
    <div>
      <h2>Users</h2>
      <ul>
        {data.map((u, i) => (
          <li key={u.id || i}>{u.name} ({u.email}) - {u.team?.name || u.team}</li>
        ))}
      </ul>
    </div>
  );
}
