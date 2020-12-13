import axios from "axios";
import jwt_decode from "jwt-decode";
import {
  GET_ERRORS,
  SET_CURRENT_USER,
  USER_LOADING
} from "./types";

// Register User
export const registerUser = (userData, history) => dispatch => {
  axios
    .post("/auth/signup", userData)
    .then(res => history.push("/login")) // re-direct to login on successful register
};

// Login - get user token
export const loginUser = userData => dispatch => {
  axios
    .post("/auth/login", userData)
    .then(res => {
      // Save to localStorage
      // Set token to localStorage
      var status = res.data.status
      if (status == true) {
        localStorage.setItem("user", res.data.res)
        dispatch(setCurrentUser(res.data.res));
        console.log("Auth Success")

      }
    })
};

// Set logged in user
export const setCurrentUser = decoded => {
  return {
    type: SET_CURRENT_USER,
    payload: decoded
  };
};

// User loading
export const setUserLoading = () => {
  return {
    type: USER_LOADING
  };
};

// Log user out
export const logoutUser = () => dispatch => {
  localStorage.removeItem("user");
  dispatch(setCurrentUser({}));
};