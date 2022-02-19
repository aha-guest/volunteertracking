The Volunteer Core project is a web app that assists in better management of Volunteer Core operations. It will track and provide matching suggestions of volunteer opportunities for volunteers, and volunteers. Later features could include communications to build out functionality similar to a CRM.

# API

## Authentication

#### Basic Auth

Basic authentication requires providing a valid user's username and password in an Authorization: Basic header. The username and password has to be Base64 encoded.

Header example:  
`headers: "Authorization": "Basic " + btoa({username} + ":" + {password})`

Return example:
`{ "token": "4nUD2mndArD4C0PJH8YQ/bg6NDnAZoEj" }`

#### Token Authentication

Token authentication requires providing a user's valid token in an Authorization: Bearer header. An expired token will return a 401 unauthorized error.

Header example:  
`headers: "Authorization": "Bearer {token}"`

## Resources

- Token
- User
- Opportunities
- Tags
- Tag Categories
- Import Data

### Token

#### Variables

| Name     | Datatype | Request/Return | Example            | Notes                                                                               |
| -------- | -------- | -------------- | ------------------ | ----------------------------------------------------------------------------------- |
| username | String   | Request        | See Authentication |
| password | String   | Request        | See Authentication |
| token    | String   | Return         | See Authentication | Returned from basic-auth and expires by configuration setting or default 60 minutes |

#### Endpoints

| Endpoint          | Method Type | Auth Required | Arguments | Description                                |
| ----------------- | ----------- | ------------- | --------- | ------------------------------------------ |
| /api/token/auth   | POST        | BasicAuth     |           | Requires basic auth and returns user token |
| /api/token/logout | POST        | Token         |           | Log out by revoking user token             |

---

### User

#### Request Variables

| Name     | Datatype | Request/Return | Example                        | Notes                                     |
| -------- | -------- | -------------- | ------------------------------ | ----------------------------------------- |
| id       | Integer  | Both           | id=345                         | Auto-generated if left blank at POST      |
| username | String   | Both           | username='johndoe'             | Required for POST                         |
| email    | String   | Both           | email='jane@example.com'       | Optional, GET requires include_email=True |
| roles    | List     | Both           | roles=['Admin','User']         | Optional                                  |
| password | String   | Request        | password='supersecretpassword' | Required for POST                         |

#### Endpoints

| Endpoint                      | Method Type | Auth Required        | Arguments     | Description                                           |
| ----------------------------- | ----------- | -------------------- | ------------- | ----------------------------------------------------- |
| /api/users/{id}               | GET         | Token and Admin role | include_email | Returns user data specified by id                     |
| /api/users                    | GET         | Token and Admin role | include_email | Returns all users data                                |
| /api/users/authenticated_user | GET         | Token                |               | Returns user data from given authenticated user token |
| /api/users                    | POST        | Token and Admin role |               | Create a new user                                     |
| /api/users/{id}               | PUT         | Token and Admin role |               | Update existing user specified by id                  |
| /api/users/{id}               | DELETE      | Token and Admin role |               | Delete user specified by id                           |

---

### Opportunities

#### Variables

| Name              | Datatype | Request/Return | Example                        | Notes                                                                                                     |
| ----------------- | -------- | -------------- | ------------------------------ | --------------------------------------------------------------------------------------------------------- |
| id                | Integer  | Both           | id=34                          | Auto-generated if left blank at POST                                                                      |
| active            | Boolean  | Both           | active=True                    |
| name              | String   | Both           | name='Make deliveries'         | Required for POST                                                                                         |
| description       | Text     | Both           | description='Long description' | Optional                                                                                                  |
| shift_hours       | Float    | Both           | shift_hours=1.5                | Optional                                                                                                  |
| start_date        | Date     | Both           | start_date=20190528            | Optional, requires YYYYMMDD format                                                                        |
| end_date          | Date     | Both           | end_date=20190528              | Optional, requires YYYYMMDD format                                                                        |
| volunteers_needed | Integer  | Both           | volunteers_needed=2            | Optional                                                                                                  |
| tag_count         | Integer  | Return         | "tag_count": 0                 |
| tags              | List     | Both           | tags=['Cooking','Bookkeeping'] | Optional, returns grouped by tag category                                                                 |
| tag_string        | String   | Return         |                                | Used to store tags in string for search indexing                                                          |
| page              | Integer  | Both           | page=2                         | Gives the 2nd page of paginated return                                                                    |
| per_page          | Integer  | Both           | per_page=25                    | When specified in the request, returns number of items per page.                                          |
| search            | String   | Request        | ?search='dining'               | Returns opportunties with name, location_city, location_zip, or tags_string matching the search variable. |

#### Endpoints

| Endpoint                | Method Type | Auth Required | Arguments                                                  | Description                                                                                        |
| ----------------------- | ----------- | ------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| /api/opportunities/{id} | GET         |               |                                                            | Returns opportunity data specified by id                                                           |
| /api/opportunities      | GET         |               | page, per_page, search, frequency_unit, frequency_modifier | Returns all opportunities paginated and filtered by search, frequency_unit, and frequency_modifier |
| /api/opportunities      | POST        | Token         |                                                            | Create a new opportunity                                                                           |
| /api/opportunities/{id} | PUT         | Token         |                                                            | Update existing opportunity specified by id                                                        |
| /api/opportunities/{id} | DELETE      | Token         |                                                            | Delete opportunity specified by id                                                                 |

---

### Tags

#### Variables

| Name         | Datatype | Request/Return | Example        | Notes                                |
| ------------ | -------- | -------------- | -------------- | ------------------------------------ |
| id           | Integer  | Both           | id=42          | Auto-generated if left blank at POST |
| name         | String   | Both           | name='Cooking' | Required for POST                    |
| tag_category | String   | Both           | name='Passion' | Required for POST                    |

#### Endpoints

| Endpoint       | Method Type | Auth Required        | Arguments      | Description                                       |
| -------------- | ----------- | -------------------- | -------------- | ------------------------------------------------- |
| /api/tags/{id} | GET         |                      |                | Returns tag data specified by id                  |
| /api/tags      | GET         |                      | page, per_page | Returns all tags paginated and filtered by search |
| /api/tags      | POST        | Token and Admin role |                | Create a new tag                                  |
| /api/tags/{id} | PUT         | Token and Admin role |                | Update existing tag specified by id               |
| /api/tags/{id} | DELETE      | Token and Admin role |                | Delete tag specified by id                        |

---

### Tag Categories

#### Variables

| Name          | Datatype | Request/Return | Example                         | Notes                                |
| ------------- | -------- | -------------- | ------------------------------- | ------------------------------------ |
| id            | Integer  | Both           | id=42                           | Auto-generated if left blank at POST |
| category_name | String   | Both           | category_name='Passions'        | Required for POST                    |
| tags          | List     | Both           | tags=['Cooking', 'Bookkeeping'] | Optional                             |

#### Endpoints

| Endpoint                 | Method Type | Auth Required        | Arguments      | Description                                                 |
| ------------------------ | ----------- | -------------------- | -------------- | ----------------------------------------------------------- |
| /api/tag_categories/{id} | GET         |                      |                | Returns tag category data specified by id                   |
| /api/tag_categories      | GET         |                      | page, per_page | Returns all tag categories paginated and filtered by search |
| /api/tag_categories      | POST        | Token and Admin role |                | Create a new tag category                                   |
| /api/tag_categories/{id} | PUT         | Token and Admin role |                | Update existing tag category specified by id                |
| /api/tag_categories/{id} | DELETE      | Token and Admin role |                | Delete tag category specified by id                         |

---

### Hours

#### Variables

Name | Datatype | Example | Notes
-----=----------=---------=------
id | Integer | id=1 | Auto generated
hours | Float | hours=1.5 | Hours for this particular volunteer period
description | Text | description="cleaned the floors" | A brief description of what was done

#### Endpoints

| Endpoint                      | Method Type | Auth Required | Arguments          | Description                                                                    |
| ----------------------------- | ----------- | ------------- | ------------------ | ------------------------------------------------------------------------------ |
| /api/admin/hours/total/{id}   | GET         | Admin         |                    | Returns and individuals hours by id                                            |
| /api/admin/hours/{month}/{id} | GET         | Admin         |                    | Returns and individuals hours by id and month                                  |
| /api/hours/month              | POST        |               | hours, description | Adds and entry to the current month, with hours and description passed as json |
| /api/hours/total              | GET         |               |                    | Returns an individuals total hours                                             |
| /api/hours/month              | GET         |               |                    | Returns the hours for the current month                                        |
| /api/hours/month/all          | GET         |               |                    | Returns the a paginated version of all of the users entries                    |

---

### Import Data

The import end point allows importing a csv file to bulk import opportunities, tags, and applying tags to opportunities. Each endpoint requires a specific set of columns with the first row labeled to identify the column. All endpoints expect a file form field named 'file'.

#### Opportunities

Endpoint: /api/import/opportunities

Column names:

- opportunity
- location_street1
- location_street2
- location_city
- location_state
- location_zip
- volunteers_needed

#### Tags

Endpoint: /api/import/tags

Column names:

- tag
- tag_category

#### Opportunity Tags

Endpoint: /api/import/opportunity_tags

Column names:

- opportunity
- tag
- tag_category

#### Endpoints

| Endpoint                     | Method Type | Auth Required        | Arguments | Description |
| ---------------------------- | ----------- | -------------------- | --------- | ----------- |
| /api/import/opportunities    | POST        | Token and Admin role |           | See above   |
| /api/import/tags             | POST        | Token and Admin role |           | See above   |
| /api/import/opportunity_tags | POST        | Token and Admin role |           | See above   |
