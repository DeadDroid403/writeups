we have a simple site which returns hello world.
there are three endpoints 
/flag
/jrl
/get-admin-cookie

we can't get the admin cookie cause for that we will need the secret.

the /jrl gives us old admin cookie where admin is set to true and uid is set to 1337

the /flag endpoint check if we have a cookie and if it is not in the jrl list. then it decodes the cookie with jwt.decode() and if admin is set to true it will give us the flag.

let's get the cookie from jrl.
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhZG1pbiI6dHJ1ZSwidWlkIjoiMTMzNyJ9.BnBYDobZVspWbxu4jL3cTfri_IxNoi33q-TRLbHV-ew

we can see it is base64_url_encoded cause there are - signs but base64 only contains + / signs.
we can change those - sign with + so it will be still the same cookie but in base64 format.
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhZG1pbiI6dHJ1ZSwidWlkIjoiMTMzNyJ9.BnBYDobZVspWbxu4jL3cTfri_IxNoi33q+TRLbHV+ew

now if the server check our cookie in jrl list, it won't find it and pass the check then it will be decoded with base64 or base64_url doesn't matter cause jwt.decode() will handle this scenerio.
our cookie will be decoded with admin = true and we will get the flag.

byuctf{idk_if_this_means_anything_but_maybe_its_useful_somewhere_97ba5a70d94d}
