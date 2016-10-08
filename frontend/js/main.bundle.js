import '../css/main.styl'
import React from 'react';
import ReactDOM from 'react-dom';

import AllAdventuresList from 'react_components/AllAdventuresList'
import NearbyAdventuresList from 'react_components/NearbyAdventuresList'
import Baz from 'bazooka';


Baz.register({
    'AllAdventuresList': AllAdventuresList,
    'NearbyAdventuresList': NearbyAdventuresList,
});

Baz.watch();
