from rest_framework import routers
from DjangoRESTapp.viewsets import AdmissionViewset

router=routers.DefaultRouter()
router.register('admission',AdmissionViewset)


urlpatterns = router.urls