import React from 'react';
import { Subject, BehaviorSubject } from 'rx';

export const appBus = new Subject();

/**
 * Temporal implementation
 * TODO: move it into custom module
 */
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

        appBus.filter(
            ({ action }) => action === 'ACTION_RENDER'
        ).withLatestFrom(
            stateStream,
            (appData, streamData) => { currentView: appData.view }
        ).merge(stateStream);

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

