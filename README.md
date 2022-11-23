# Business Data Microservice

A Python Django Rest Framework based microservice to hold data for businesses. This application is a
stateless application means this application doesn't have any User or user's state. It simply decode
JWT Tokens generated from [JWT-AUTH-MICROSERVICE](https://github.com/saanpritom/ekkbaz-jwt-auth) and
based on the successful decode this authenticate a request and an user.

## How to run the service

Simply follow the below commands sequentially.

- Create a **.env** file on the root directory. You can copy **.env.example** file and rename it to **.env** file. However, the value of those environment variables may change from machine to machine.

- Install application dependencies

```bash
 pip install -r requirements.txt
```

- Run the following command. This command will satisfy all the internal dependencies of the application.

```bash
bash setup.sh
```

- Run the application.

```bash
python app/manage.py runserver
```

## How to use the service

- This service has 4 base API endpoints. The endpoints are for all the `CRUD` operations.
- The pattern for the endpoints are like this

```link
https://{your-domain-name}/api/business/data/
```
- The operation is determined by the request method. The allowed methods are `Create`, `List`, `Detail`, `PUT`, `Patch` and `Delete`.

- You need to obtain an user `access_key` to get access to these APIs. To obtain an user key please go to
the **JWT Token** service and read the **README.md** there.

- After getting the `access_key` make the following requests to perform your desired operations.

    - To view the list of all business run the following command

    ```bash
    curl \
    -H "Authorization: Bearer {access_key}" \
    https://{your-domain-name}/api/business/data/
    ```
    - To view a single businesse's details run the following command

    ```bash
    curl \
    -H "Authorization: Bearer {access_key}" \
    https://{your-domain-name}/api/business/data/{id}
    ```
    - To create a new business run the following command

    ```bash
    curl \
    -X POST \
    -H "Authorization: Bearer {access_key}" \
    -d '{"name": "your-business-name", "location": "your-business-location"}' \
    https://{your-domain-name}/api/business/data/
    ```
    - To fully update a business run the following command

    ```bash
    curl \
    -X PUT \
    -H "Authorization: Bearer {access_key}" \
    -d '{"name": "your-business-name", "location": "your-business-location"}' \
    https://{your-domain-name}/api/business/data/{id}
    ```
    - To partially update a business run the following command

    ```bash
    curl \
    -X PATCH \
    -H "Authorization: Bearer {access_key}" \
    -d '{"name": "your-business-name"}' \
    https://{your-domain-name}/api/business/data/{id}
    ```
    - To delete a business run the following command

    ```bash
    curl \
    -X DELETE \
    -H "Authorization: Bearer {access_key}" \
    https://{your-domain-name}/api/business/data/{id}
    ```


<sup> [Pritom Borogoria](https://github.com/saanpritom) reserves all right.</sup>