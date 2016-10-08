import React from 'react';
import ReactDOM from 'react-dom';
import {h} from 'bazooka';

import FullAdventure from 'view';

export default (node) => {
    ReactDOM.render(
        <FullAdventure />,
        node
    );
}