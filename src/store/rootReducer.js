import { combineReducers } from 'redux';
import { persistReducer } from 'redux-persist';
import storage from 'redux-persist/lib/storage';
import exampleReducer from '../reducers/exampleReducer';

const rootReducer = combineReducers({
    example: exampleReducer
});

const persistConfig = {
    key: 'root',
    storage,
    whitelist: ['example'] // Add the names of the reducers you want to persist
};

export default persistReducer(persistConfig, rootReducer);
