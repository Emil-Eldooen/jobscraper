# jobscraper
A simlpe jobscraper that can look through applications from Arbeidsplassen.no

Simple to use, once you've downloaded the file simply edit the URL variable by copying the URL from Arbeidsplassen.no after you've applied your search conditions and insert, then run the script in the console.

The output format is as follows:

Company
Position title
Link to application

**Shortcomings**
1: It only fetches the first 100 results, I didn't see a reason to add a loop to the code going through each page in Arbeidsplassen as the amount of applications rarely exceeded 100 in my use-case.
2: For the sake of simplicity the password is stored in a variable, but ideally it should be an input or stored more securely. However, I made it an option to simply store it in a variable. If you would prefer doing so by other methods such as by fetching the password from a file, salting it etc doing so shouldn't be much of a challenge.
3: There's no UI, so this tool will not be as simple as allowing anyone to paste a URL into a text bar. Might consider adding this at a later date for fun
