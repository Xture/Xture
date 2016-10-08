import React from 'react';
import ReactDOM from 'react-dom';
import {h} from 'bazooka';

import ListNearByAdventures from '../react_components/listAdventures/ListNearByAdventures';

const BAZOOKA_PREFIX = 'list';

export default (node) => {
    const {id, csrfToken} = h.getAttrs(BAZOOKA_PREFIX, node);
    ReactDOM.render(
        <ListNearByAdventures />,
        node
    );
}
