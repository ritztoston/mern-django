export default Register;
import React, {Component} from 'react';
import axios from 'axios';
import classnames from 'classnames';

class Register extends Component {
  constructor() {
    super();
    this.state = {
      email: '',
      username: '',
      firstname: '',
      lastname: '',
      avatar: '',
      password: '',
      password2: '',
      errors: {}
    };

    this.onChange = this.onChange.bind(this);
    this.onSubmit = this.onSubmit.bind(this);
  }

  onChange(e) {
    if(e.target.name !== 'avatar')
      this.setState({[e.target.name]: e.target.value});
    else{
        this.setState({[e.target.name]: e.target.files[0]});
    }
  }

  onSubmit(e) {
    e.preventDefault();
    const newuser = new FormData();

    if(this.state.avatar !== '' && this.state.avatar !== null && typeof this.state.avatar !== "undefined") {
        newuser.append('avatar', this.state.avatar, this.state.avatar.name);
    }

    newuser.append('email', this.state.email);
    newuser.append('username', this.state.username);
    newuser.append('firstname', this.state.firstname);
    newuser.append('lastname', this.state.lastname);
    newuser.append('password', this.state.password);
    newuser.append('password2', this.state.password2);


    axios.post('http://localhost:8000/api/users/register/', newuser)
    .then(res => console.log(res.data))
    .catch(err => this.setState({errors: err.response.data}));
  }

  render() {
    const {errors} = this.state;

    return (
      <div className="register">
        <div className="container">
          <div className="row">
            <div className="col-md-8 m-auto">
              <h1 className="display-4 text-center">Sign Up</h1>
              <p className="lead text-center">Create your DevConnector account</p>
              <form onSubmit={this.onSubmit} encType="application/json">
                <div className="form-group">
                  <input type="email" className={classnames('form-control form-control-lg', {'is-invalid': errors.email})} placeholder="Email Address" name="email" value={this.state.email} onChange={this.onChange}/>
                  {errors.email && (<div className="invalid-feedback">{errors.email}</div>)}
                </div>
                <div className="form-group">
                  <input type="text" className={classnames('form-control form-control-lg', {'is-invalid': errors.username})} placeholder="Username" name="username" value={this.state.username} onChange={this.onChange}/>
                  {errors.username && (<div className="invalid-feedback">{errors.username}</div>)}
                </div>
                <div className="form-group">
                  <input type="text" className={classnames('form-control form-control-lg', {'is-invalid': errors.firstname})} placeholder="First Name" name="firstname" value={this.state.firstname} onChange={this.onChange}/>
                  {errors.firstname && (<div className="invalid-feedback">{errors.firstname}</div>)}
                </div>
                <div className="form-group">
                  <input type="text" className={classnames('form-control form-control-lg', {'is-invalid': errors.lastname})} placeholder="Last Name" name="lastname" value={this.state.lastname} onChange={this.onChange}/>
                  {errors.lastname && (<div className="invalid-feedback">{errors.lastname}</div>)}
                </div>
                <div className="form-group">
                  <input type="file" className={classnames('form-control-file', {'is-invalid': errors.email})} id="avatar" name="avatar" onChange={this.onChange}/>
                  {errors.avatar && (<div className="invalid-feedback">{errors.avatar}</div>)}
                </div>
                <div className="form-group">
                  <input type="password" className={classnames('form-control form-control-lg', {'is-invalid': errors.password})} placeholder="Password" name="password" value={this.state.password} onChange={this.onChange}/>
                  {errors.password && (<div className="invalid-feedback">{errors.password}</div>)}
                </div>
                <div className="form-group">
                  <input type="password" className={classnames('form-control form-control-lg', {'is-invalid': errors.password2})} placeholder="Confirm Password" name="password2" value={this.state.password2} onChange={this.onChange}/>
                  {errors.password2 && (<div className="invalid-feedback">{errors.password2}</div>)}
                </div>
                <input type="submit" className="btn btn-info btn-block mt-4" />
              </form>
            </div>
          </div>
        </div>
      </div>
    )
  }
}

export default Register;
