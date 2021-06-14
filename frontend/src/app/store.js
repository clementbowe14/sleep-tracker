import { configureStore } from '@reduxjs/toolkit'
import sleepReducer from '../features/sleep/sleepSlice'
import userReducer from '../features/user/userSlice'

export const store = configureStore({
    reducer:{
        sleep: sleepReducer,
        user: userReducer,
    },
});

export default store;