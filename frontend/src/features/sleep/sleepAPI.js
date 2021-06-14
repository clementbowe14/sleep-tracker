import {createAsyncThunk, createSlice} from '@reduxjs/toolkit'

// initial state will be read at the start of the
const initialState = {
    sleep: [],
    status: 'idle',
}

export const createSleep = createAsyncThunk(
    'createSleep'
    async (sleep) =>{
        
    }
)

export const sleepSlice = createSlice({
    
    //
    name:'sleep',
    initialState,

    //reducers for the sleep
    reducers: {

    }

})