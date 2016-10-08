import React from 'react';


class Adventure extends React.Component{
    constructor(){
        super();
    }

    render() {
        return <div>
            Adventure
            <h1>${this.props.title}</h1>

            <div>
                <span>Description</span>: <span>${this.props.description}</span>
            </div>
            <div>
                <span>Location</span>: <span>${this.props.location[0]}, ${this.props.location[1]}</span>
            </div>
            <div>
            </div>
        </div>
    }

}

export default Adventure;
