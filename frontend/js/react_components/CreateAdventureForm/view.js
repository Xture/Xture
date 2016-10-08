import React from 'react';
import Rx from 'rx';

// Then, render it:
export default class CreateAdventureForm extends React.Component {
	constructor() {
		super();
		this.state = {
			description: "",
			title: "",
			longitude: 0,
			latitude: 0
		};
	}

	componentDidMount() {
		navigator.geolocation.getCurrentPosition((possition) => {
			// body...
			let cords = possition.coords;
			this.setState({'latitude': cords.latitude});
			this.setState({'longitude': cords.longitude});
		});
	}

	submit() {
		var data = {
			method: 'POST',
			body: this.state,
			headers: {'Content-Type': 'application/json'}
		}
		fetch('/adventure/', data)
			.then((response) => response.json())
			.then((response) => {
				console.log('successfuly created');
			});
	}

    handleInputDesc(event) {
       this.setState({ description: event.target.value });
    }

    handleInputTitle(event) {
       this.setState({ title: event.target.value });
    }

	render() {
		return (
			<div className="xr-form">
				<div>
					<input value={this.state.title} onChange={this.handleInputDesc} type="text"
						className="xr-form__input xr-form__input_focus xr-form__input_active"></input>
				    <span className="xr-form__bar"></span>
                    <label className="xr-form__label">
                        Title
                    </label>
				</div>

				<div className="xr-form__group">
					<input value={this.state.description} onChange={this.handleInputDesc} type="text"
						className="xr-form__input xr-form__input_focus xr-form__input_active"></input>
				    <span className="xr-form__bar"></span>
                    <label className="xr-form__label">
                        Description
                    </label>
				</div>
				<div className="xr-form__group">
					<input value={this.state.longitude} type="number" 
						className="xr-form__input xr-form__input_focus xr-form__input_active" disabled='disabled'></input>
				    <span className="xr-form__bar"></span>
                    <label className="xr-form__label">
                        Longitude
                    </label>
				</div>

				<div className="xr-form__group">
					<input value={this.state.latitude} type="number"
						className="xr-form__input xr-form__input_focus xr-form__input_active" disabled='disabled'></input>
				    <span className="xr-form__bar"></span>
                    <label className="xr-form__label">
                        Latitude
                    </label>
				</div>
	            <div onClick={this.submit} className="xr-form__button">
					<div className="xr-form__button-text" >Create adventure</div>
                </div>
			</div>
		);
	}
}
