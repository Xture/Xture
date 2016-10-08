import '../css/main.styl'
import React from 'react';
import ReactDOM from 'react-dom';

import ListAdventures from 'dom_elements/ListAdventures';

import Baz from 'bazooka';

Baz.register({
    'listAdventures': ListAdventures,
});

Baz.watch();