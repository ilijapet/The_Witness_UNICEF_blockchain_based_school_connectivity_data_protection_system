import { useHistory } from 'react-router-dom';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import { TextField, Stack } from '@mui/material';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { useForm } from 'react-hook-form';
import { DevTool } from '@hookform/devtools';

import { useLocation } from 'react-router-dom';

import { axiosInstance } from '../axios';
import defaultTheme from '../utils';
import Copyright from './Copyright';

export default function ResetPassword() {
  const location = useLocation();

  console.log(
    `user/resetpassword/${location.pathname.split('/')[2]}/${
      location.pathname.split('/')[3]
    }/`,
  );

  const form = useForm({
    defualtValues: {
      email: '',
    },
  });

  const { register, handleSubmit, formState, control } = form;
  const { errors } = formState;

  const history = useHistory();

  const resetPassword = async (event) => {
    try {
      const password = event['password'];
      const response = await axiosInstance.patch(
        `user/resetpassword/${location.pathname.split('/')[2]}/${
          location.pathname.split('/')[3]
        }/`,
        JSON.stringify({ password: password }),
      );

      console.log(response.data);

      // Here Im going to redirect to the reset password confirmation page
      history.push({
        pathname: '/resetconfirmation',
        state: { absurl: response.data['absurl'] },
      });
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <ThemeProvider theme={defaultTheme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            New password
          </Typography>

          <Stack>
            <form onSubmit={handleSubmit(resetPassword)} noValidate>
              <Grid container spacing={2}>
                <Grid item xs={12}>
                  <TextField
                    required
                    fullWidth
                    id="password"
                    label="Password"
                    name="password"
                    type="password"
                    autoComplete="password"
                    {...register('password', { required: 'Email is required' })}
                    error={!!errors.password}
                    helperText={errors.password?.message}
                  />
                </Grid>
              </Grid>
              <Button
                type="submit"
                fullWidth
                variant="contained"
                sx={{ mt: 3, mb: 2 }}
              >
                Submit
              </Button>
            </form>
          </Stack>
        </Box>
        <Copyright sx={{ mt: 5 }} />
      </Container>
      <DevTool control={control} />
    </ThemeProvider>
  );
}
