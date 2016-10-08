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
            .then((js) => {
                this.setState({'adventures': js});
            });
    }

    render() {
        return <div className="xr-card__container">
            {this.state.adventures.map(
                (a) => (
                    <Adventures 
                        description={a.description}
                        title={a.title}
                        location={a.location}
                    />
                )
            )}
        </div>

    }
}

export default ListAdventures;
