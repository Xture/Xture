import '../css/main.styl'
import React from 'react';
import ReactDOM from 'react-dom';

import AllAdventuresList from './react_components/AllAdventuresList';
import CreateAdventureForm from './react_components/CreateAdventureForm';
import Login from './react_components/Login';
import NearbyAdventuresList from './react_components/NearbyAdventuresList';

import Baz from 'bazooka';


Baz.register({
    'AllAdventuresList': AllAdventuresList,
    'CreateAdventureForm': CreateAdventureForm,
    'Login': Login,
    'NearbyAdventuresList': NearbyAdventuresList,
});

Baz.watch();
