Every time an app or platform has a Login With or Continue With option, that's the starting point of an
OAuth flow:

Example: Login to spotify with Facebook

Steps Flow:

1. The spotify app will ask the FB Api to start the authentication flow. To do this, the spotify app
will send its application ID(client_id) and a URL(redirect_uri) to redirect the user after success or
error

2. You will be redirected to Facebook website and asked to login with your credentials. The spotify app
won't see or have access to these credentials. This is the most important benefit of OAuth.

3. FB will show you all the data that the spotify app is requesting from your profile and ask you to
accept or reject sharing that data

4. If you accept giving spotify access to your data, then you will be redirected to Spotify app, already 
logged in.

When going through step4, FB will provide spotify with a special credential(access_token) that it can use
repeatedly to fetch your information. This specific FB token is valid for sixty days, but other apps might
have different expiration periods.

From tech stand point , here's what you need to know when consuming APIs using OAuth:

1. You need to create an application that will have an ID(app_id or client_id) and a secret(app_secret or client_secret)

2. You need to have a redirect URL(redirect_uri), which the API will use to send information to you.

3. You'll get a code as the result of the authentication, which you need to exchange for an access token.
