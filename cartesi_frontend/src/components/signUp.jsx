// import * as React from "react";
import { useHistory } from 'react-router-dom';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import { TextField, Stack } from '@mui/material';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { ThemeProvider } from '@mui/material/styles';
import { useForm } from 'react-hook-form';
import { DevTool } from '@hookform/devtools';
// import { green } from "@mui/material/colors";

import { axiosInstance } from '../axios';
import defaultTheme from '../utils';
import Copyright from './Copyright';

export default function SignUp() {
  const form = useForm({
    defualtValues: {
      email: '',
      password: '',
      username: '',
    },
  });

  const { register, handleSubmit, formState, control } = form;
  const { errors } = formState;

  const history = useHistory();

  const handler = async (event) => {
    await axiosInstance
      .post('user/register/', {
        email: event['email'],
        password: event['password'],
        user_name: event['username'],
      })
      .then((res) => {
        history.push('/');
        console.log(res);
        console.log(res.data);
      })
      .catch((error) => {
        console.error('There was an error!', error.response.data);
        alert('There was an error!');
      });
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
            Sign up
          </Typography>

          <Stack>
            <form onSubmit={handleSubmit(handler)} noValidate>
              <Grid container spacing={2}>
                <Grid item xs={12} sm={12}>
                  <TextField
                    autoComplete="username"
                    name="firstName"
                    required
                    fullWidth
                    id="firstName"
                    label="Username"
                    autoFocus
                    {...register('username', {
                      required: 'Username is required',
                    })}
                    error={!!errors.username}
                    helperText={errors.username?.message}
                  />
                </Grid>
                <Grid item xs={12}>
                  <TextField
                    required
                    fullWidth
                    id="email"
                    label="Email Address"
                    name="email"
                    autoComplete="email"
                    {...register('email', { required: 'Email is required' })}
                    error={!!errors.email}
                    helperText={errors.email?.message}
                  />
                </Grid>
                <Grid item xs={12}>
                  <TextField
                    required
                    fullWidth
                    name="password"
                    label="Password"
                    type="password"
                    id="password"
                    autoComplete="new-password"
                    {...register('password', {
                      required: 'Password is required',
                    })}
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
                Sign Up
              </Button>
            </form>
          </Stack>
          <Grid container justifyContent="flex-end">
            <Grid item>
              <Link href="/" variant="body2">
                Already have an account? Sign in
              </Link>
            </Grid>
          </Grid>
        </Box>
        <Copyright sx={{ mt: 5 }} />
      </Container>
      <DevTool control={control} />
    </ThemeProvider>
  );
}
