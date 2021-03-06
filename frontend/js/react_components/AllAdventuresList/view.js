import React from 'react';
import Adventure from '../Adventure/view'

function AdventureListItem(props) {
    return <a href={`/adventure/${props.id}`} className="f-list-item">
        <span className="f-list-item-title">{props.title}</span>
        <span className="f-list-item-descr">{props.description}</span>
    </a>
    
}
export default class extends React.Component {

    constructor() {
        super();
        this.state = {
            adventures: [],
            fetched: false,
        };
    }

    componentDidMount() {
        setTimeout(() => {
            var token = localStorage.token;
            var headers = {'Authorization': token};
            fetch('/api/adventure/',{headers})
                .then((response) => response.json())
                .then((json) => {
                    this.setState({
                        adventures: json,
                        fetched: true,
                    });
                });
        }, 500);
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
                (a) => <AdventureListItem
                    id={a._id}
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
