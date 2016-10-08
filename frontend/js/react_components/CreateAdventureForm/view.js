import React from 'react';
import Rx from 'rx';

export default class CreateAdventureForm extends React.Component {

	constructor() {
		super();
		this.state = {
			description: "",
			title: "",
			location: [0, 0]
		};
	}

	componentDidUpdate() {
		navigator.geolocation.getCurrentPosition((possition) => {
			// body...
			var cords = possition.coords;
			location = [cords.latitude, cords.longtitude];
			this.state.location = location;
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

	render() {
		return (
			<div>
				<label for="">Title:
					<input value={this.state.title} type="text"></input>
				</label>

				<label for="">Description:
					<input value={this.state.description} type="text"></input>
				</label>
				<h3>Coordinates:</h3>
				<hr />
				<label for="">Description:
					<input value={this.state.location[0]} type="number"></input>
				</label>

				<label for="">Description:
					<input value={this.state.location[1]} type="number"></input>
				</label>
				
				<button onClick={this.submit}>Create adventure</button>
			</div>
		);
	}
}
