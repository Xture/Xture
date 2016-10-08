import React from 'react';

export default class FullAdventure extends React.Component {

    constructor() {
        super();
        this.state = {
            adventure: null
        }
    }

    renderSpinner() {
        return <div className="xr-spinner"/>
    }

    renderWithoutImages() {
        return <div className="xr-images__holder
                               xr-images__holder_empty"
        />
    }

    renderImages() {
        if (this.state.adventure.images) {
            return <div className="xr-images__list">
                {this.state.adventure.photos.map(
                    (a) => <img src='/images/{a.id}'/>
                )}
            </div>
        }else{
            {this.renderWithoutImages()}
        }
    }

    renderMedia() {
        return <div className="xr-adventure__media">
            <div className="xr-map__secondary">

            </div>
            {this.renderImages()}
        </div>
    }

    renderDetails() {
        return <div className="xr-adventure__detail">
            <div className="xr-adventure__title">
                {this.state.adventure.title}
            </div>
            <div className="xr-adventure__desc">
                {this.state.adventure.description}
            </div>
        </div>
    }

    render() {
        return <div className="xr-adventure">
            {this.renderMedia()}
            {this.renderDetails()}
        </div>
    }

}