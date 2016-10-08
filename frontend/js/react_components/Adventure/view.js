import React from 'react';


export default class extends React.Component {
    constructor() { super(); }

    render() {
        return <div>
            <div class="f-column-left">
                <div class="f-map">
                    <span>Latitude: {this.props.location[0]}</span>
                    <span>Longitude: {this.props.location[1]}</span>
                </div>

                <div class="f-pictures">
                    {this.props.images.map(
                        (image_id) => <img class="f-picture" src="/image/{image_id}"/>
                    )}
                </div>
            </div>

            <div class="f-column-right">
                <h1 class="f-title">${this.props.title}</h1>
                <div class="f-desctiption">
                    {this.props.description}
                </div>
            </div>
        </div>
    }
}
