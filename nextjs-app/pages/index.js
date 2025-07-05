import { useEffect, useState } from 'react';
import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

export default function Home() {
  const [average, setAverage] = useState(null);
  const [labels, setLabels] = useState([]);
  const [values, setValues] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8888/api/solar-data')
      .then(res => res.json())
      .then(data => {
        if (data.status === 'success') {
          setAverage(data.data.average_power);
          const monthly = data.data.monthly_data;
          setLabels(Object.keys(monthly));
          setValues(Object.values(monthly));
        }
      })
      .catch(err => console.error(err));
  }, []);

  const chartData = {
    labels,
    datasets: [
      {
        label: 'Power Generation (W/m²)',
        data: values,
        backgroundColor: '#4CAF50'
      }
    ]
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Solar Power Data</h1>
      {average && (
        <p>Average Power Generation: {average.toFixed(2)} W/m²</p>
      )}
      <Bar data={chartData} />
    </div>
  );
}
