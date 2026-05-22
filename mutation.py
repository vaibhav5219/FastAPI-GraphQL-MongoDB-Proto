import strawberry
from db import user_collection

@strawberry.type
class ResponseType:
    inserted_id: str

@strawberry.type
class Mutation:
    @strawberry.mutation
    def createUser(self, name: str, phone: str) -> ResponseType:
        # Here you would typically insert the new user into the database
        # and return the ID of the newly created user.
        # For demonstration purposes, we'll just return a success message.
        user = {"name": name, "phone": phone}
        result = user_collection.insert_one(user)
        return ResponseType(inserted_id=str(result.inserted_id))

    @strawberry.mutation
    def saveUser(self, id: str, name: str, phone: str) -> ResponseType:
        # Here you would typically update the existing user in the database
        # with the provided ID and return a success message.
        # For demonstration purposes, we'll just return a success message.
        user_collection.update_one({"_id": id}, {"$set": {"name": name, "phone": phone}})
        return ResponseType(inserted_id=str(id))