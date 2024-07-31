import React, { useState } from 'react';
import Dashboard from './components/Dashboard';
import VoiceCommand from './components/VoiceCommand';
import axios from 'axios';

const App = () => {
    const [data, setData] = useState([]);

    const fetchData = async () => {
        const response = await axios.get('/api/data');
        setData(response.data);
    };

    const handleCommand = (command) => {
        // Handle voice command
        console.log('Voice Command:', command);
    };

    return (
        <div>
            <h1>MachiEm</h1>
            <button onClick={fetchData}>Fetch Data</button>
            <Dashboard data={data} />
            <VoiceCommand onCommand={handleCommand} />
        </div>
    );
};

export default App;
