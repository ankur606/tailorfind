# from rest_framework import routers
from django.urls import path, include
from . import views

# router = routers.DefaultRouter()
# router.register()

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='api-login'),
    path('logout/', views.UserLogoutView.as_view(), name='api-logout'),
    path('profile/', views.UserProfileView.as_view(), name='api-profile'),
    path('tailors/', views.TailorListView.as_view(), name='api-tailors'),
    path('female-services/', views.FemaleServiceListView.as_view(), name='api-female-services'),
    path('male-services/', views.MaleServiceListView.as_view(), name='api-male-services'),
    path('orders/', views.OrderListView.as_view(), name='api-orders'),
    path('order-detail/<int:id>/', views.OrderDetailView.as_view(), name='api-order-detail'),
    path('measurement/', views.CustomerMeasurementView.as_view(), name='api-measurement'),
    path('customer-select-service/', views.CustomerSelectServiceView.as_view(), name='api-customer-select-service'),
    path('customer-selected-service/', views.CustomerSelectedServiceView.as_view(), name='api-customer-selected-service'),
    path('customer-delete-selected-service/<int:id>/', views.CustomerDeleteSelectedServiceView.as_view(), name='api-customer-delete-selected-service'),
    path('customer-service-detail/<int:id>/', views.CustomerServiceDetailView.as_view(), name='api-customer-service-detail'),
    path('customer-place-order-preview/', views.CustomerPlaceOrderPreviewView.as_view(), name='api-customer-place-order-preview'),
    path('customer-place-order/', views.CustomerPlaceOrderView.as_view(), name='api-customer-place-order'),
    path('customer-cancel-order/<int:id>/', views.CustomerCancelOrderView.as_view(), name='api-customer-cancel-order'),
    path('tailor-upcoming-orders/', views.TailorUpcomingOrderView.as_view(), name='api-tailor-upcoming-orders'),
    path('tailor-accept-order/<int:id>/', views.TailorAcceptOrderView.as_view(), name='api-tailor-accept-order'),
    path('tailor-reject-order/<int:id>/', views.TailorRejectOrderView.as_view(), name='api-tailor-reject-order'),
    path('tailor-complete-order/<int:id>/', views.TailorCompleteOrderView.as_view(), name='api-complete-order'),
    path('tailor-accepted-orders/', views.TailorAcceptedOrdersView.as_view(), name='api-tailor-accepted-orders'),
    path('tailor-earnings/', views.TailorEaringsView.as_view(), name='api-tailor-earnings'),
    # path('tailor-accepted-orders/', views.TailorAcceptOrderView.as_view(), name='api-tailor-accepted-orders'),
    path('tailor-request-earning/<int:id>/', views.TailorEaringRequestView.as_view(), name='api-tailor-request-earning'),
    # path('delivery-boy-picked-up-orders/', views.DeliveryBoyPickedUpOrdersView.as_view(), name='api-delivery-boy-picked-up-orders'),
    # path('delivery-boy-delevered-orders/', views.DeliveryBoyDeleverdOrdersView.as_view(), name='api-delivery-boy-delevered-orders'),
    # path('delivery-boy-update-order/<int:id>/', views.DeliveryBoyUpdateOrderView.as_view(), name='api-delivery-boy-update-order'),
    path("delivery-boy-upcoming-order/",views.DeliveryBoyIpcomingorder.as_view(),name='deliveryboyupcoming'),
    path("Tailor-Complete-Order-List/",views.TailorCompleteOrderViewList.as_view(),name='completeorderlisttailor'),
    path('Delivery-Boy-Accept-Order/<int:id>/',views.Delivery_boy_accept_order.as_view(),name='deliveryboyacceptorder'),
    # path('Delivery-Boy-Accept-Completed-Order/<int:id>/',views.Delivery_boy_accept_complete_order.as_view()),
    path('Delivery-Boy-Reject-Order/<int:id>/',views.Delivery_boy_reject_order.as_view(),name='deliveryboyrejectorder'),
    path('Delivery_Boy_Accepted_Order_List/',views.Delivery_boy_accpted_order_list.as_view()),
    path('Delivery-Boy-Picked-For-sevice/<int:id>/',views.Delivery_boy_picked_for_service.as_view()),
    path('Delivery-Boy-Delivered-sevice/<int:id>/',views.Delivery_boy_delivered_service.as_view()),
    path('Delivery-Boy-Complete-Delivered-List/',views.Delivery_boy_Compelete_Delivery_List.as_view()),
    path('Receive-Notification-List/',views.ReceiveNotification.as_view()),
    path('Delivery-Boy-Total-earning/',views.Delivery_Boy_Total_earning.as_view()),
    path('Near-by-tailor-list/',views.Near_By_Tailors.as_view()),
    path('Tailor-Toatal-Earning/',views.Tailor_Earning.as_view()),
    path('Customer-delete-selected-services/',views.CustomerSelectServicedeleted.as_view()),
    path('Delete-Single-Notification/<int:id>/',views.Delete_single_Notification.as_view()),
    path('Delete-All-Notification/',views.Delete_All_Notification.as_view()),
    path('Notification-Count/',views.Notification_count.as_view()),
    path('tailor-measurement-show/<int:id>/',views.Tailor_show_measurement.as_view()),
    path('tailor-get-measurement/',views.Tailor_get_measurement.as_view()),
    path('Term-And-Conditions/',views.TermandCondition.as_view()),
    path('Privacy-And-Policy/',views.PrivacyandPolicy.as_view()),
    path('Tailor-Earning-Request/',views.TailorEaringRequestView.as_view()),
    path('Earning-Withdrow-List/',views.EarningWithdrowlist.as_view()),
    path('Delivery-Boy-Earning-Request/',views.Delivery_boy_request_earning.as_view()),
    



    ###############################
    path('All-Categories/',views.AllCategories.as_view()),
    path('Service-provider-Details/<int:id>/',views.User_category_list.as_view()),
    path('Service-provider-services/<int:idd>/',views.User_service_list.as_view()),
    path('All-Service-provider/',views.User_category_lists.as_view()),
    
]