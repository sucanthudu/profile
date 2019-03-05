from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""


        if request.method in permissions.SAFE_METHODS:  #GET(SAFE_METHODS) returns list of user profiles
            return True

        return obj.id == request.user.id                 

class PostOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Checks the user is trying to update their own status"""

        if request.method in permissions.SAFE_METHODS:     #get method(permission for viewing everybody's status)
            return True

        return obj.id == request.user.id # if the id matches user can perform the action(post status) otherwise no.
