function formValidation() {
	var username = document.registration.username;
	var password = document.registration.password;
	var lname = document.registration.lastname;
	var address = document.registration.address;
	var country = document.registration.country;
	var state = document.registration.state;
	var city = document.registration.city;
	var zipcode = document.registration.zipcode;
	var phone = document.registration.phone;
	var email = document.registration.email;
	var gender1 = document.registration.getElementByid('flexRadioDefault3');
	var gender2 = document.registration.getElementByid('flexRadioDefault3');
	var gender3 = document.registration.getElementByid('flexRadioDefault3');
	if (allLetter(username, 1, 8)) {
		if (
			passid_validation(password, 1, 8) &&
			alphanumeric(password) &&
			password.search[/a-z/i] > 0 &&
			password.search[/A-Z/i] > 0
		) {
			if (allLetter(lname, 1, 30)) {
				if (allLetter(address, 1, 60)) {
					if (allLetter(city, 1, 30)) {
						if (allLetter(state, 1, 30)) {
							if (allnumeric(zipcode)) {
								if (ValidateEmail(email, 1, 30)) {
									if (validsex(gender1, gender2, gender3)) {
										return true;
									}
								}
							}
						}
					}
				}
			}
			// if (allLetter(uname)) {
			// 	if (alphanumeric(uadd)) {
			// 		if (countryselect(ucountry)) {
			// 			if (allnumeric(uzip)) {
			// 				if (ValidateEmail(uemail)) {
			// 					if (validsex(umsex, ufsex)) {
			// 					}
			// 				}
			// 			}
			// 		}
			// 	}
			// }
		}
	}
	console.log('hello');

	return false;
}

function userid_validation(uid, mx, my) {
	var uid_len = uid.value.length;
	if (uid_len == 0 || uid_len >= my || uid_len < mx) {
		alert('User Id should not be empty / length be between ' + mx + ' to ' + my);
		uid.focus();
		return false;
	}
	return true;
}

function passid_validation(passid, mx, my) {
	var passid_len = passid.value.length;
	if (passid_len == 0 || passid_len >= my || passid_len < mx) {
		alert('Password should not be empty / length be between ' + mx + ' to ' + my);
		passid.focus();
		return false;
	}
	return true;
}

function allLetter(uname) {
	var letters = /^[A-Za-z]+$/;
	if (uname.value.match(letters)) {
		return true;
	} else {
		alert('Username must have alphabet characters only');
		uname.focus();
		return false;
	}
}

function alphanumeric(uadd) {
	var letters = /^[0-9a-zA-Z]+$/;
	if (uadd.value.match(letters)) {
		return true;
	} else {
		alert('User address must have alphanumeric characters only');
		uadd.focus();
		return false;
	}
}

function countryselect(ucountry) {
	if (ucountry.value == 'Default') {
		alert('Select your country from the list');
		ucountry.focus();
		return false;
	} else {
		return true;
	}
}

function allnumeric(uzip) {
	var numbers = /^[0-9]+$/;
	if (uzip.value.match(numbers)) {
		return true;
	} else {
		alert('ZIP code must have numeric characters only');
		uzip.focus();
		return false;
	}
}

function ValidateEmail(uemail) {
	var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
	if (uemail.value.match(mailformat)) {
		return true;
	} else {
		alert('You have entered an invalid email address!');
		uemail.focus();
		return false;
	}
}

function validsex(gender1, gender2, gender3) {
	x = 0;

	if (gender1.checked) {
		x++;
	}
	if (gender2.checked) {
		x++;
	}
	if (gender3.checked) {
		x++;
	}
	if (x == 0) {
		alert('Select Male/Female');
		umsex.focus();
		return false;
	} else {
		alert('Form Successfully Submitted');
		window.location.reload();
		return true;
	}
}