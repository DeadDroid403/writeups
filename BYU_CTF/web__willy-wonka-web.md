A http request smuggling challenge. willy wonka web.
i first started by looking the source code they provided and i found that there is a backend and a frontend. it must be HRS.
so i started digging in ! andddddddddd
it took a lot of my time cause there are so many ways to perform request smuggling. 
but in the end, none of those worked and i left this challenge but after some time, i started to look for versions and their related CVEs and i found this CVE...

CVE-2023-25690
mod_proxy configurations on Apache HTTP Server versions 2.4.0 through 2.4.55 allow a HTTP Request Smuggling attack.
fortunately, our response header contains the same version of apache and it is using mod_proxy.

there is POC dhmosfunk on this CVE that describes how we can take advantage of the HTTP request smuggling to access restricted endpoints.
https://github.com/dhmosfunk/CVE-2023-25690-POC

after reading the whole POC i ended up with this payload and it worked.
GET /name/kidda%20HTTP/1.1%0d%0aHost:%20wonka.chal.cyberjousting.com%0d%0aA:%20admin%0d%0a%0d%0aGET%20/name/test HTTP/1.1
Host: wonka.chal.cyberjousting.com

and i got the flag : byuctf{i_never_liked_w1lly_wonka}





