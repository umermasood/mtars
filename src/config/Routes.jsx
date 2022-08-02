import React from 'react';

import { Route, Switch } from 'react-router-dom';

import Home from '../pages/Home';
import Auth from '../pages/Auth'
import Catalog from '../pages/Catalog';
import Detail from '../pages/detail/Detail';
import { AuthProvider } from "./AuthContext";
import ProtectedRoute from './ProtectedRoutes';


const Routes = () => {
    return (
        <AuthProvider>
            <Switch>

                <ProtectedRoute exact path='/:category/:id' component={Detail} />
                <Route

                    path='/auth'
                    component={Auth}
                />
                <Route
                    exact
                    path='/:category/search/:keyword'
                    component={Catalog}
                />
                {/* <Route
                    path='/:category/:id'
                    component={Detail}
                /> */}
                <Route
                    exact
                    path='/:category'
                    component={Catalog}
                />
                <Route
                    path='/'
                    exact
                    component={Home}
                />
            </Switch>
        </AuthProvider>
    );
}

export default Routes;
