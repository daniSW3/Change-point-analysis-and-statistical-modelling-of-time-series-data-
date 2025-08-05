import React, { useState, useEffect } from 'react';
import axios from 'axios';
import {
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer,
  BarChart, Bar, Legend
} from 'recharts';
import './App.css';

const App: React.FC = () => {
  const [prices, setPrices] = useState([]);
  const [events, setEvents] = useState([]);
  const [model, setModel] = useState({});
  const [startDate, setStartDate] = useState('1987-05-20');
  const [endDate, setEndDate] = useState('1987-06-26');

  useEffect(() => {
    axios.get('http://localhost:5000/api/prices', { params: { start_date: startDate, end_date: endDate } })
      .then(response => setPrices(response.data));
    axios.get('http://localhost:5000/api/events')
      .then(response => setEvents(response.data));
    axios.get('http://localhost:5000/api/model')
      .then(response => setModel(response.data));
  }, [startDate, endDate]);

  const handleFilter = (e: React.FormEvent) => {
    e.preventDefault();
    // Filter logic here
  };

  // Prepare data with event highlights
  const chartData = prices.map((price: any) => ({
    date: price.Date,
    price: price.Price,
    event: events.some((event: any) => event['Start Date'].slice(0, 10) === price.Date.slice(0, 10)) ? 1 : 0,
  }));

  return (
    <div className="p-4 max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Brent Oil Price Dashboard</h1>
      <form onSubmit={handleFilter} className="mb-4">
        <input
          type="date"
          value={startDate}
          onChange={(e) => setStartDate(e.target.value)}
          className="mr-2 p-1 border"
        />
        <input
          type="date"
          value={endDate}
          onChange={(e) => setEndDate(e.target.value)}
          className="mr-2 p-1 border"
        />
        <button type="submit" className="p-1 bg-blue-500 text-white">Filter</button>
      </form>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={chartData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="price" stroke="#8884d8" />
          <Line type="monotone" dataKey="event" stroke="#ff7300" strokeWidth={2} dot={false} />
        </LineChart>
      </ResponsiveContainer>
      <h2 className="text-xl mt-4">Event Impact</h2>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={chartData.filter((d: any) => d.event === 1)}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="price" fill="#82ca9d" />
        </BarChart>
      </ResponsiveContainer>
      <div className="mt-4">
        <p>Change Points: {model.change_points?.join(', ')}</p>
        <p>Runtime: {model.runtime} seconds</p>
      </div>
    </div>
  );
};

export default App;