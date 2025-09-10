there was three api endpoints.
two were for performing email verification and that is the biggest rabbit whole.
people will try for otp bypass there but those two are rabbit holes.

one more endpoint is /api/screen-token
it asks for a user id
i gave it 0 and 1 it said account deactivated then i gave it 2, 3, 4 and it said user not found and on 5,6 it said account deactivated.
but on the 7 i got the hash value.

now there is /screen/ endpoint which asks for a key. i gave it the hash i found and i got the flag.

i found all of these endpoints in the js file of the site.
