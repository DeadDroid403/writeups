web challenge : red_this

so we have site that gives us functionality to submit a famous person name and it will return a quote by them
it submits the famous person name by a post request to /get_quote endpoint.
by reading the source code we can see there are other values which we can submit in the famous_person parameter in post request like admin, admin_password,etc.
 i tried admin_password and i got the password of admin user.

there was no login endpoint given in the source code so i tried to guess it and got it in a single try. it was /login lol
after loggin in with the username admin and password "I_HopeYou4re8admin_iLoveTechn070g_9283910", i got redirected to / root page.
but this time we have admin access and admin cookies and we can send some more different types of values in the famous_person parameter.
there was a value "flag_7392ilj8i32" and as i submitted it, i got the flag.

byuctf{al1w4ys_s2n1tize_1nput-5ed1s_eik4oc85nxz}
