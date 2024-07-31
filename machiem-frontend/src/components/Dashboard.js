import React from 'react';
import DataVisualization from './DataVisualization';

const Dashboard = ({ data }) => {
    return (
        <div>
            <h1>Dashboard</h1>
            <DataVisualization data={data} />
        </div>
    );
};

export default Dashboard;
