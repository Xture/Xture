import React from 'react';
import Rx from 'rx';

export default class Login extends React.Component {

    constructor (props) {
        super(props);

        this.state = {
            login: '',
            password: '',
        };

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
        let login = this.state.login;
        let password = this.state.password;

        fetch('/auth/login', {  method: 'POST', 
                                headers: {'Content-Type': 'application/json'},
                                body: JSON.stringify({
                                    login: login, 
                                    password: password
                                })
                             })
            .then((response) => {
                localStorage.setItem('token', response.token);
            });
    }

    render() {
        return (
            <div className="xr-form">
                <div className="xr-form__group">
                    <input type="text"
                           value={this.state.login}
                           required
                           onChange={this.handleInputLogin}
                           className="xr-form__input xr-form__input_focus xr-form__input_active" ></input>
                    <span className="xr-form__bar"></span>
                    <label className="xr-form__label">
                        Login
                    </label>
                </div>

                <div className="xr-form__group">
                    <input type="password"
                           required
                           value={this.state.password}
                           onChange={this.handleInputPassword}
                           className="xr-form__input xr-form__input_focus xr-form__input_active"></input>
                    <span className="xr-form__bar"></span>
                    <label className="xr-form__label">
                        Password
                    </label>
                </div>
                <div className="xr-form__button">
                    <div className="xr-form__button-text" onClick={this.onSubmit}>Log In</div>
                </div>
            </div>
        );
    }
}
