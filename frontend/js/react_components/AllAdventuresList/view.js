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
        fetch('/adventure/')
        .then((response) => response.json())
        .then((json) => {
            this.setState({
                adventures: json,
                fetched: true,
            });
        });
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
