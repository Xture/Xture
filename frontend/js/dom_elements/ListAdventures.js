import React from 'react';
import ReactDOM from 'react-dom';
import {h} from 'bazooka';

import ListAdventures from '../react_components/listAdventures/ListAdventures';

const BAZOOKA_PREFIX = 'list';

export default (node) => {
    const {id, csrfToken} = h.getAttrs(BAZOOKA_PREFIX, node);
    ReactDOM.render(
        <ListAdventures />,
        node
    );
}