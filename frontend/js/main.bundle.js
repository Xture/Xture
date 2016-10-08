import '../css/main.styl'
import React from 'react';
import ReactDOM from 'react-dom';

import AllAdventuresList from 'react_components/AllAdventuresList'
import Baz from 'bazooka';


Baz.register({
    'AllAdventuresList': AllAdventureList,
});

Baz.watch();
