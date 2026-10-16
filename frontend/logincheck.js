async function loginCheck(event) {
    if (event) {
        event.preventDefault();
    }

    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('pass').value;
    if (!email || !password) {
        alert('Email and password are required');
        return;
    }

    try {
        const response = await fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });
        if (!response.ok) {
            throw new Error(`Sign-in request failed with status ${response.status}`);
        }

        const result = await response.json();
        if (result === 0) {
            alert('Sign-in successful!');
            window.location.replace("/Frontend/main.html");
        } else {
            alert('Invalid email or password.');
        }
    }
    catch (error) {
        console.error('Error:', error);
        alert('Unable to sign in. Please try again.');
    }
}

const signinForm = document.getElementById('signin-form');
if (signinForm) {
    signinForm.addEventListener('submit', loginCheck);
}

async function signup(event){
    if (event) {
        event.preventDefault();
    }
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('pass').value;
    const name=document.getElementById('name').value.trim();
    if (!email || !password || !name) {
        alert('All fields are required');
        return;
    }
    try {
        const response = await fetch('/signup', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password,name })
        });
        if (!response.ok) {
            throw new Error(`Sign-up request failed with status ${response.status}`);
        }

        const result = await response.json();
        if (result === 0) {
            alert('Sign-up successful!');
        } else {
            alert('User already exists.');
            window.location.replace("/Frontend/signin.html");
        }
    }
    catch (error) {
        console.error('Error:', error);
        alert('Unable to sign up. Please try again.');
    }
}

async function logout(){
    const response = await fetch('/book', {
        method: 'POST',
    });
    if(await response.json()==0){
        alert("logout Successfull");
    }
    window.location.replace("/Frontend/signin.html");
}

async function book(event) {
    event.preventDefault();
    const slotId = event.currentTarget.closest('.box').id;
    try {
    const proceed = confirm("Are you sure you want to book this event?");
    if (!proceed) {
        return;
    }
        const response = await fetch('/book', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({slotId})
        });

        if (!response.ok) {
            throw new Error(`Booking request failed with status ${response.status}`);
        }
        const result = await response.json();
        alert(`Booking successful!\nThe OTP is:\t${result.otp}`);
    } catch (error) {
        console.error('Error:', error);
        alert('Unable to send booking request. Please try again.');
    }
}
