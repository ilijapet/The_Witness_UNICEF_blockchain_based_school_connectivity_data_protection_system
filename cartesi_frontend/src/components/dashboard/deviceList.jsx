import * as React from 'react';
// import { useState, useEffect } from 'react';
// import Link from '@mui/material/Link';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Button from '@mui/material/Button';
import Title from './title';

function createData(id, name, city, school, device_type) {
  return { id, name, city, school, device_type };
}

function preventDefault(event) {
  event.preventDefault();
}

export default function SchoolList() {
  const rows = [
    createData(0, 'Paraguay', 'Asunción', 'Asunción', 'AC32'),
    createData(1, 'Serbia', 'Belgrade', 'Branka Radicevica', 'AC32'),
    createData(2, 'Bangladesh', 'Dhaka', 'Dhaka', 'AC32'),
    createData(3, 'Colombia', 'Bogota', 'Bogota', 'AC44'),
    createData(4, 'Venezuela', 'Caracas', 'Caracas', 'AC32'),
  ];

  return (
    <React.Fragment>
      <Title> Schools </Title>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell>State</TableCell>
            <TableCell>City</TableCell>
            <TableCell>School</TableCell>
            <TableCell>Device </TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow key={row.id}>
              <TableCell>{row.name}</TableCell>
              <TableCell>{row.city}</TableCell>
              <TableCell>{row.school}</TableCell>
              <TableCell>{row.device_type}</TableCell>
              <TableCell align="right">
                <Button
                  color="inherit"
                  href="https://www.international-school.edu.rs/"
                >
                  link
                </Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </React.Fragment>
  );
}
