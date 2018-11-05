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
      isReadyCreateUser: false,
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
    newuser.append('isReadyCreateUser', this.state.isReadyCreateUser);

    this.setState({errors: {}});

    axios.post('http://localhost:8000/api/users/register/', newuser)
    .then(res => console.log(res.data))
    .catch(err => this.setState({errors: err.response.data}));
  }

  onSubmit(e) {
    e.preventDefault();
    const newuser = new FormData();
    this.setState({'isReadyCreateUser': true});
    console.log(this.state.isReadyCreateUser);

    if(this.state.avatar !== '' && this.state.avatar !== null && typeof this.state.avatar !== "undefined") {
        newuser.append('avatar', this.state.avatar, this.state.avatar.name);
    }

    newuser.append('email', this.state.email);
    newuser.append('username', this.state.username);
    newuser.append('firstname', this.state.firstname);
    newuser.append('lastname', this.state.lastname);
    newuser.append('password', this.state.password);
    newuser.append('password2', this.state.password2);
    newuser.append('isReadyCreateUser', this.state.isReadyCreateUser);


    axios.post('http://localhost:8000/api/users/register/', newuser)
    .then(res => console.log(res.data))
    .catch(err => this.setState({errors: err.response.data}));
  }

  render() {
    const {errors} = this.state;

    return (
        <div className="registration__form">
            <form action="#" className="form" autoComplete="off" onSubmit={this.onSubmit} encType="application/json">
                <div className="container">
                  <div className="row">
                    <div className="col">
                        <div className="form__group">
                            <input type="text" className={classnames('form__input', {'form__input--is-invalid': errors.email})} placeholder="Email" id="email" name="email" value={this.state.email} onChange={this.onChange}/>
                            {errors.email ? (<label htmlFor="email" className={classnames('form__invalid', {'form__invalid-show': errors.email})}>{errors.email}</label>) : (<label htmlFor="email" className="form__label">What is your email?</label>)}
                        </div>
                    </div>
                  </div>
                  <div className="row">
                    <div className="col">
                        <div className="form__group">
                            <input type="text" className={classnames('form__input', {'form__input--is-invalid': errors.username})} placeholder="Username" id="username" name="username" maxLength="11" value={this.state.username} onChange={this.onChange}/>
                            {errors.username ? (<label htmlFor="email" className={classnames('form__invalid', {'form__invalid-show': errors.username})}>{errors.username}</label>) : (<label htmlFor="email" className="form__label">What you would like to be called?</label>)}
                        </div>
                    </div>
                  </div>
                  <div className="row">
                    <div className="col">
                        <div className="form__group">
                            <input type="text" className={classnames('form__input', {'form__input--is-invalid': errors.firstname})} placeholder="First Name" id="firstname" name="firstname" value={this.state.firstname} onChange={this.onChange}/>
                            {errors.firstname ? (<label htmlFor="email" className={classnames('form__invalid', {'form__invalid-show': errors.firstname})}>{errors.firstname}</label>) : (<label htmlFor="email" className="form__label">What is your name?</label>)}
                        </div>
                    </div>
                  </div>
                  <div className="row">
                    <div className="col">
                        <div className="form__group">
                            <input type="text" className={classnames('form__input', {'form__input--is-invalid': errors.lastname})} placeholder="Last Name" id="lastname" name="lastname" value={this.state.lastname} onChange={this.onChange}/>
                            {errors.lastname ? (<label htmlFor="email" className={classnames('form__invalid', {'form__invalid-show': errors.lastname})}>{errors.lastname}</label>) : (<label htmlFor="email" className="form__label">and your last name?</label>)}
                        </div>
                    </div>
                  </div>
                  <div className="row">
                    <div className="col">
                        <div className="form__group">
                            <input type="password" className={classnames('form__input', {'form__input--is-invalid': errors.password})} placeholder="Password" id="password" name="password" maxLength="11" value={this.state.password} onChange={this.onChange}/>
                            {errors.password ? (<label htmlFor="email" className={classnames('form__invalid', {'form__invalid-show': errors.password})}>{errors.password}</label>) : (<label htmlFor="email" className="form__label">Shhh..Don't tell anyone. It's a secret.</label>)}
                        </div>
                    </div>
                  </div>
                  <div className="row">
                    <div className="col">
                        <div className="form__group">
                            <input type="password" className={classnames('form__input', {'form__input--is-invalid': errors.password2})} placeholder="Confirm Password" id="password2" name="password2" maxLength="11" value={this.state.password2} onChange={this.onChange}/>
                            {errors.password2 ? (<label htmlFor="email" className={classnames('form__invalid', {'form__invalid-show': errors.password2})}>{errors.password2}</label>) : (<label htmlFor="email" className="form__label">Confirm your secret with us.</label>)}
                        </div>
                    </div>
                  </div>
                  <div className="row u-padding-top-lg">
                    <div className="col">
                        <div className="form__group">
                            <div className="u-text-align-center">
                                <button className="btn__ btn__submit" type="submit">Sign Up</button>
                            </div>
                        </div>
                    </div>
                  </div>
              </div>
            </form>
        </div>
    )
  }
}

export default Register;
