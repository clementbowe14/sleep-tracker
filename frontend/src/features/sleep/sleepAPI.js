import {createAsyncThunk, createSlice} from '@reduxjs/toolkit'

const initialState = {
    //empty array of sleep days
    sleep: []
}

export const sleepSlice({
    
    name:'sleep',
    initialState,

})