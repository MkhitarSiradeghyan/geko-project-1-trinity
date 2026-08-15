from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):

    def has_object_permission(self,request,view,obj):
        if request.user.is_staff:
            return True

        return obj.owner == request.user


class IsGalleryOwnerOrAdmin(BasePermission):

    def has_object_permission(self,request,view,obj):
        if request.user.is_staff:
            return True

        return obj.gallery.owner == request.user