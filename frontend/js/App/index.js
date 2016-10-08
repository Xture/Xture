import React from 'react';
import { Subject, BehaviorSubject } from 'rx';

export const appBus = new Subject();

function Login(props) {
    return <div>test</div>;
}

export default class Application extends React.Component {
    constructor(props) {
        super(props);

        this.availableViews = {
            Login, 
        };
        this.stateStream = new BehaviorSubject({
            currentView: 'Login',
        });
        this.allowUpdateState = false;

        this.stateStream.subscribe(({ currentView }) => {
            if (this.allowUpdateState)  // Workaround, but works
                this.setState({ currentView });
        });

        this.render = this.render.bind(this);
        this.state = { currentView: 'Login' };
    }

    componentDidMount () {
        this.allowUpdateState = true;
    }

    render() {
        return React.createElement(this.availableViews[this.state.currentView]);
    }
}

