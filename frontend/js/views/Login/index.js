import React from 'react';
import Rx from 'rx';

export default class Login extends React.Component {

    constructor (props) {
        super(props);

        this.state = {
            login: '',
            password: '',
        }

        this.onSubmit = this.onSubmit.bind(this);
        this.handleInputLogin = this.handleInputLogin.bind(this);
        this.handleInputPassword = this.handleInputPassword.bind(this);
    }

    handleInputLogin(event) {
       this.setState({ login: event.target.value });
    }

    handleInputPassword(event) {
       this.setState({ password: event.target.value });
    }

    onSubmit() {
        // TODO: add route, where to write
        console.log(`${this.state.login} ${this.state.password}`);
    }

    render() {
        return (
            <div style={{ marginTop: '200px' }}>
                <input
                    value={this.state.login}
                    type="text"
                    placeholder="Login"
                    onChange={this.handleInputLogin}
                />
                <input
                    value={this.state.password}
                    type="password"
                    placeholder="Password"
                    onChange={this.handleInputPassword}
                />
                <button onClick={this.onSubmit}>Some strange text</button>
            </div>
        );
    }
}
