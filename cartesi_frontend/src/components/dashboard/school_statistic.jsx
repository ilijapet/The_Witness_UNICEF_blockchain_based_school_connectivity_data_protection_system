import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Title from './title';

export default function SchoolStatistic(props) {
  const data = props.data;

  if (!data) {
    return <div>No data available</div>;
  }

  console.log(data, 'bla truc');
  console.log(data.download_speed);
  console.log('Upload speed:', data.upload_speed);
  console.log('Latency:', data.latency);

  return (
    <React.Fragment>
      <Title>Communication device statistic</Title>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell>School ID</TableCell>
            <TableCell>Download speed</TableCell>
            <TableCell>Upload speed</TableCell>
            <TableCell>Latency</TableCell>
            <TableCell align="right">Last update</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          <TableRow key={data.id}>
            <TableCell>{data.school_id}</TableCell>
            <TableCell
              style={{ color: data.download_speed !== 0 ? 'inherit' : 'red' }}
            >
              {data.download_speed !== undefined
                ? data.download_speed
                : 'Not Operational'}
            </TableCell>
            <TableCell style={{ color: data.upload_speed ? 'inherit' : 'red' }}>
              {data.upload_speed !== undefined
                ? data.upload_speed
                : 'Not Operational'}
            </TableCell>
            <TableCell style={{ color: data.latency ? 'inherit' : 'red' }}>
              {data.latency !== undefined ? data.latency : 'Not Operational'}
            </TableCell>
            <TableCell align="right">{data.timestamp}</TableCell>
          </TableRow>
        </TableBody>
      </Table>
    </React.Fragment>
  );
}
