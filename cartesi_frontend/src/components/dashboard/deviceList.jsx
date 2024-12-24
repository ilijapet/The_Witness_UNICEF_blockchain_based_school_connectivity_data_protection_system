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

function createData(id, name, shipTo, paymentMethod, status) {
  return { id, name, shipTo, paymentMethod, status };
}
function preventDefault(event) {
  event.preventDefault();
}

export default function SchoolList() {
  const rows = [
    createData(0, 'Paraguay', 'Asunción', 'AC32'),
    createData(1, 'Serbia', 'Belgrade', 'AC32. '),
    createData(2, 'Bangladesh', 'Dhaka', 'AC32'),
    createData(3, 'Colombia', 'Bogota', 'AC44'),
    createData(4, 'Venezuela', 'Caracas', 'AC32'),
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
              <TableCell>{row.shipTo}</TableCell>
              <TableCell>{row.paymentMethod}</TableCell>
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
