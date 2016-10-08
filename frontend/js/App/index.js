import React from 'react';
import { Subject, BehaviorSubject } from 'rx';

import Login from 'views/Login';

export const appBus = new Subject();

export default class Application extends React.Component {
    constructor(props) {
        super(props);

        this.availableViews = {
            Login, 
        };
        this.stateStream = new BehaviorSubject({
            currentView: 'Login',
        });

        appBus.filter(
            ({ action }) => action === 'ACTION_RENDER'
        ).subscribe(({ view }) => {
            this.stateStream.onNext({ currentView: view })
        });

        this.render = this.render.bind(this);
        this.state = { currentView: 'Login' };
    }

    componentDidMount () {
        this.updateStateSubscription = this.stateStream.subscribe(
            ({ currentView }) => {
                this.setState({ currentView });
            }
        );
    }

    componetWillUnmount() {
        if (this.updateStateSubscription) {
            this.updateStateSubscription.dispose();
        }
    }

    render() {
        return React.createElement(this.availableViews[this.state.currentView]);
    }
}

