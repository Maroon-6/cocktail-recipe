import json

secure_paths = ["/recipes"]


def check_security(request, google, blueprint):
    path = request.path
    result_ok = False

    if path in secure_paths:
        user_info_endpoint = '/oauth2/v2/userinfo'

        if google.authorized:
            google_data = google.get(user_info_endpoint).json()
            print(json.dumps(google_data, indent=2))

            s = blueprint.session
            t = s.token

            print(json.dumps(t, indent=2))
            result_ok = True
    else:
        result_ok = True
    return result_ok
