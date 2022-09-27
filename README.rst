==============
Org Model Logs
==============

Org model logs is a Django app created for DBCA to allow developers to collect action and communcation logs
for any model in their project without having to duplicate a lot of code.

Quick start
-----------

1. Add "org_model_logs" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'org_model_logs',
    ]

2. You can include the org_model_logs URLconf in your project urls.py like this:

    path('org-model-logs/', include('org_model_logs.urls')),

    however if you need to apply specific permissions to the org_model_logs api end-points,
    if it recommended to create subclasses of the viewsets within your own project and add urls
    for those to your own project also:

    i.e.

    from org_model_logs.api import (
        UserActionList,
    )   

    from yourproject.permissions import IsInternal, etc..

    class UserActionList(UserActionList):
        serializer_class = UserActionSerializer
        permission_classes = [IsInternal]

3. Run ``python manage.py migrate`` to create the org model logs models.

4. To add basic logging to a viewset simply extend from org_model_logs.utils.UserActionViewSet

    For custom api methods you must call the log_action method manually. I.e.

    user_action = UserAction.objects.log_action(
        object_id=object_id,
        content_type=content_type,
        who=request.user.id,
        what=user_action.format(Pass._meta.model.__name__, object_id),
        why=serializer.data["cancellation_reason"],
    )
