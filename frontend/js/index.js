import '../css/main.styl'
import React from 'react';
import ReactDOM from 'react-dom';

import ListAdventures from 'dom_elements/ListAdventures';
import ListNearByAdventures from 'dom_elements/ListNearByAdventures';

import Baz from 'bazooka';

Baz.register({
    'listAdventures': ListAdventures,
    'listNearByAdventures': ListNearByAdventures,
});

Baz.watch();
