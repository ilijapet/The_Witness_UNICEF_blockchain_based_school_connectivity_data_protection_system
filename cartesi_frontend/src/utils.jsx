import { green } from '@mui/material/colors';
import { createTheme } from '@mui/material/styles';

const defaultTheme = createTheme({
  palette: {
    mode: 'dark',
    primary: {
      main: green[500],
    },
    secondary: {
      main: green[500],
    },
  },
});

export default defaultTheme;
