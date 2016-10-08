import React from 'react';
import Adventures from '../adventure/Adventure'

class ListNearByAdventures extends React.Component {

    constructor() {
        super();
        this.state = {'adventures': []};
    }

    componentDidMount() {
        if ('geolocation' in navigator) {
            navigator.geolocation.getCurrentPosition((pos) => {
                const lat = pos.coords.latitude;
                const lng = pos.coords.longitude;

                fetch(`/adventure/nearest?lat=${lat}&lng=${lng}`)
                    .then((response) => response.json())
                    .then((js) => {
                        this.setState({'adventures': js});
                    });
            });
        }
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

export default ListNearByAdventures;
