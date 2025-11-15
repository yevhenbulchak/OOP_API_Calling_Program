from api_profanity import APIProfanity


def main():
    # Pass a plain string (message) that will be checked for profanity.
    params = "This is a test message to check for profanity shit"

    api = APIProfanity(params, 10)
    status, result = api.call_api()
    if status == 0:
        # On success result is the parsed JSON response from the profanity API
        print(api)
        return

    print('\nAn error occurred in the API call\n')
    print(result)


if __name__ == '__main__':
    main()