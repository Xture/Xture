import React from 'react';
import Adventure from '../Adventure/view'


export default class extends React.Component {

    constructor() {
        super();
        this.state = {
            adventures: [],
            fetched: false,
        };
    }

    componentDidMount() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    const lng = position.coords.longitude;
                    const lat = position.coords.latitude;

                    var token = localStorage.token;
                    var headers = {'Authorization': token};

                    fetch(`/api/adventure/nearest?lat=${lat}&lng=${lng}`, {headers})
                        .then((response) => response.json())
                        .then((json) => {
                            this.setState({
                                adventures: json,
                                fetched: true,
                            });
                        });
                },
                (err) => { /* TODO: handle that */
                    // function showError(error) {
                    //     switch(error.code) {
                    //         case error.PERMISSION_DENIED:
                    //             x.innerHTML = "User denied the request for Geolocation."
                    //             break;
                    //         case error.POSITION_UNAVAILABLE:
                    //             x.innerHTML = "Location information is unavailable."
                    //             break;
                    //         case error.TIMEOUT:
                    //             x.innerHTML = "The request to get user location timed out."
                    //             break;
                    //         case error.UNKNOWN_ERROR:
                    //             x.innerHTML = "An unknown error occurred."
                    //             break;
                }
            )
        }
    }

    renderSpinner() {
        return <div className="f-spinner"/>
    }

    renderEmptyList() {
        return <div className="f-list_holder f-list_holder-empty"></div>
    }

    renderList() {
        return <div className="f-list_holder">
            {this.state.adventures.map(
                (a) => <Adventure
                    location={a.location}
                    images={a.images}
                    description={a.description}
                    title={a.title}
                />
            )}
        </div>
    }

    render() {
        if (!this.state.fetched) {
            return this.renderSpinner();
        } else if (this.state.adventures.length == 0) {
            return this.renderEmptyList();
        } else {
            return this.renderList();
        }
    }
}
