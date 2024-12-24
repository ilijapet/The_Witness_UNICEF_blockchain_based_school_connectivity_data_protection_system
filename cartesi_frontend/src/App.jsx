import React from 'react';
import { Route, BrowserRouter as Router, Switch } from 'react-router-dom';

import SignInSide from './components/signInSide';
import SignUp from './components/signUp';
import Logout from './components/logout';
import ForgetPassword from './components/forgetPassword';
import ResetConfirmationMail from './components/resetConfirmationMail';
import ResetConfirmation from './components/resetConfirmation';
import ResetPassword from './components/resetPassword';
import Dashboard from './components/dashboard/dashboard';
import PrivateRoute from './PrivateRoute';

import { AuthProvider } from './AutoContext';
const isAuthenticated = false;

function App() {
  return (
    <Router>
      <AuthProvider>
        <React.StrictMode>
          <Switch>
            <Route exact path="/" component={SignInSide} />
            <Route exact path="/signup" component={SignUp} />
            <Route exact path="/logout" component={Logout} />
            <PrivateRoute
              exact
              path="/profile"
              component={Dashboard}
              isAuthenticated={isAuthenticated}
            />
            <Route exact path="/forgetpassword" component={ForgetPassword} />
            <Route
              exact
              path="/resetconfirmationmail"
              component={ResetConfirmationMail}
            />
            <Route
              exact
              path="/resetpassword/:param1/:param2"
              component={ResetPassword}
            />
            <Route
              exact
              path="/resetconfirmation"
              component={ResetConfirmation}
            />
          </Switch>
        </React.StrictMode>
      </AuthProvider>
    </Router>
  );
}

export default App;
