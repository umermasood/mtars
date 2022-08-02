import React, { Fragment } from "react";
import { Redirect, Route } from "react-router-dom";

import { useAuth } from './AuthContext'

const ProtectedRoute = ({ component: Component, ...rest }) => {

    const { currentUser } = useAuth();

    return (
        <Fragment>
            {(
                <Route
                    {...rest}
                    render={(props) => {
                        if (!currentUser) {
                            return <Redirect to="/auth" />;
                        }

                        return <Component {...props} />;
                    }}
                />
            )}
        </Fragment>
    );
};

export default ProtectedRoute;