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
        var token = localStorage.token;
        var data = {
            description: this.state.description,
            title: this.state.title,
            location: [this.state.longitude, this.state.latitude]
        };
        var data = {
            method: 'POST',
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json',
                'Authorization': token
            }
        }
        fetch('/api/adventure/', data)
            .then((response) => response.json())
            .then((response) => {
                console.log('successfuly created');
            });
    }

    handleInputDesc(event) {
        this.setState({description: event.target.value});
    }

    handleInputTitle(event) {
        this.setState({title: event.target.value});
    }

    render() {
        return (
            <div className="col-md-12 float-right form-horizontal">
                <div className='col-xs-12 form-group'>
                    <label className='col-xs-3 control-label'>
                        Title
                    </label>
                    <div className='col-xs-9'>
                        <input value={this.state.title} onChange={this.handleInputTitle.bind(this)} type="text"
                               className="form-data form-control"/>
                    </div>
                </div>
                <div className='form-group'>
                    <label className='col-xs-3 control-label'>
                        Description
                    </label>
                    <div className='col-xs-9'>
                        <textarea value={this.state.description} onChange={this.handleInputDesc.bind(this)}
                                  className='form-control'></textarea>
                    </div>

                </div>
                <div className='form-group'>
                    <label className='col-xs-3 control-label'>
                        Longitude
                    </label>
                    <div className="col-xs-9">
                        <input value={this.state.longitude} type="number"
                               disabled='disabled' className="col-xs-9 form-control"/>
                    </div>
                </div>

                <div className='form-group'>
                    <label className="col-xs-3 control-label">
                        Latitude
                    </label>
                    <div className="col-xs-9">
                        <input value={this.state.latitude} type="number"
                               className="form-control" disabled='disabled'>
                        </input>
                    </div>
                </div>
                <div onClick={this.submit.bind(this)} className="btn btn-success">Create adventure</div>
            </div>
        );
    }
}
