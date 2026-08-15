from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self,request,view,obj,):
        if request.user.is_staff:
            return True

        if hasattr(obj, "owner"):
            return obj.owner == request.user

        if hasattr(obj, "gallery"):
            return obj.gallery.owner == request.user

        return False