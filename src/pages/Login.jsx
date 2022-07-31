import React from "react";
import { DialogAuth } from "react-mui-auth-page";

const MyDialogAuthComponent = () => {
  const handleSignIn = ({ email, password }) => {
    console.log({ email, password });
  };
  const handleSignUp = async ({ email, name, password }) => {
    // await doSomethingAsync();
    console.log(email, name, password);
  };
  const handleForget = ({ email }) => {
    console.log({ email });
  };

  const handleSocial = {
    Google: () => {},
  };

  const onCloseHandler = () => {
    console.log('form closed')
  }

  return (
    <DialogAuth
      open={true}
      textFieldVariant="outlined"
      onClose={onCloseHandler}
      handleSignUp={handleSignUp}
      handleForget={handleForget}
      handleSignIn={handleSignIn}
      handleSocial={handleSocial}
    />
  );
};

export default MyDialogAuthComponent;
