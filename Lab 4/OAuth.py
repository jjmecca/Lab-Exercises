import requests # Necessary to access ".json()"s
CLIENT_ID = "79c2cf055d71fe6e1b6c" # Your GitHub app's client id
CLIENT_SECRET = "1e315c9090ee04371a7b83f69545c937c4445b90" # Your GitHub app's client secret
REDIRECT_URI = "https://httpbin.org/anything" # Your GitHub app's Authorization callback URL

# Function to create the OAuth authorization link
def create_oauth_link():
    # Define parameters for the authorization link
    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": "user",
        "response_type": "code",
    }
    # Define the authorization endpoint
    endpoint = "https://github.com/login/oauth/authorize"
    # Make a GET request to the authorization endpoint with parameters
    response = requests.get(endpoint, params=params)
    # Return the URL for user authorization
    return response.url

# Function to exchange the authorization code for an access token
def exchange_code_for_access_token(code=None):
    # Define parameters for exchanging code for access token
    params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "code": code,
    }
    # Define headers for the request (accepting JSON response)
    headers = {"Accept": "application/json"}
    # Define the endpoint for exchanging code for access token
    endpoint = "https://github.com/login/oauth/access_token"
    # Make a POST request to the token endpoint with parameters and headers
    response = requests.post(endpoint, params=params, headers=headers).json()
    # Return the obtained access token from the JSON response
    return response["access_token"]

# Function to print user information using the access token
def print_user_info(access_token=None):
    # Define headers for the request, including the access token for authorization
    headers = {"Authorization": f"token {access_token}"}
    # Define the endpoint for getting user information
    endpoint = "https://api.github.com/user"
    # Make a GET request to the user information endpoint with headers
    response = requests.get(endpoint, headers=headers).json()
    # Extract relevant user information from the JSON response
    name = response["name"]
    username = response["login"]
    private_repos_count = response["total_private_repos"]
    # Print user information
    print(
        f"{name} ({username}) | private repositories: {private_repos_count}"
    )

# Create the OAuth authorization link
link = create_oauth_link()
print(f"Follow the link to start the authentication with GitHub: {link}")

code = input("GitHub code: ") # Get the authorization code from the user

# Exchange the authorization code for an access token
access_token = exchange_code_for_access_token(code)
print(f"Exchanged code {code} with access token: {access_token}")

print_user_info(access_token=access_token) # Print user information using the obtained access token