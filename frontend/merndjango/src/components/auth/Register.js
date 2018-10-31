import React, {Component} from 'react';
import axios from 'axios';

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
    else
      this.setState({[e.target.name]: e.target.files[0]});
  }

  onSubmit(e) {
    e.preventDefault();

    const newuser = {
      email: this.state.email,
      username: this.state.username,
      firstname: this.state.firstname,
      lastname: this.state.lastname,
      avatar: this.state.avatar,
      password: this.state.password,
      password2: this.state.password2
    }
    // console.log(newuser);
    // const fd = new FormData();
    // fd.append('image', this.state.avatar, this.state.avatar.name)
    // this.setState({'avatar': fd});
    axios.post('http://localhost:8000/api/users/register/', newuser)
    .then(res => console.log(res.data))
    .catch(err => console.log(err.response.data));
  }

  render() {
    return (
      <div className="register">
        <div className="container">
          <div className="row">
            <div className="col-md-8 m-auto">
              <h1 className="display-4 text-center">Sign Up</h1>
              <p className="lead text-center">Create your DevConnector account</p>
              <form onSubmit={this.onSubmit} encType="multipart/form-data">
                <div className="form-group">
                  <input type="email" className="form-control form-control-lg" placeholder="Email Address" name="email" value={this.state.email} onChange={this.onChange}/>
                </div>
                <div className="form-group">
                  <input type="text" className="form-control form-control-lg" placeholder="Username" name="username" value={this.state.username} onChange={this.onChange}/>
                </div>
                <div className="form-group">
                  <input type="text" className="form-control form-control-lg" placeholder="First Name" name="firstname" value={this.state.firstname} onChange={this.onChange}/>
                </div>
                <div className="form-group">
                  <input type="text" className="form-control form-control-lg" placeholder="Last Name" name="lastname" value={this.state.last} onChange={this.onChange}/>
                </div>
                <div class="form-group">
                  <label for="avatar">Profile Picture</label>
                  <input type="file" class="form-control-file" id="avatar" name="avatar" onChange={this.onChange}/>
                </div>
                <div className="form-group">
                  <input type="password" className="form-control form-control-lg" placeholder="Password" name="password" value={this.state.password} onChange={this.onChange}/>
                </div>
                <div class="form-group">
                  <input type="password" className="form-control form-control-lg" placeholder="Confirm Password" name="password2" value={this.state.password2} onChange={this.onChange}/>
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
