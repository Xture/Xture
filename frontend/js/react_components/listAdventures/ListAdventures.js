import React from 'react';
import Adventures from '../adventure/Adventure'

class ListAdventures extends React.Component {

    constructor() {
        super();
        this.state = {'adventures': []};
    }

    componentDidMount() {
        fetch('/adventure/')
            .then((response) => response.json())
            .then((j) => {
                this.setState({'adventures': j});
            });
    }

    render() {
        return <div className="xr-card__container">
            {this.state.adventures.map(
                (x) => <Adventure />
            )}

        </div>

    }
}

export default ListAdventures;