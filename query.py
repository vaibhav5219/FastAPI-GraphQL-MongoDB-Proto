import strawberry
from db import user_collection


@strawberry.type
class User:
    id: str
    name: str
    phone: str


@strawberry.type
class Query:

    @strawberry.field
    def getUsers(self) -> list[User]:
        users = user_collection.find()
        # return [User(id=user["_id"], name=user["name"], phone=user["phone"]) for user in users]
        response = []
        for user in users:
            userObj = User(
                id=str(user["_id"]),
                name=user["name"],
                phone=user["phone"]
            )
            response.append(userObj)
        return response
    
