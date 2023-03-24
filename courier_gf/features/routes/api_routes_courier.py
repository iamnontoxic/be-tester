from features.common import constants

API_ROOT = "https://master-admin-review.growfood.pro"

# Смена статуса доставки
set_delivered = API_ROOT + f'/api/admin/app/deliveries' #/{context.delivery_id}/deliver
set_returned = API_ROOT + '/api/admin/app/deliveries/{}/set-returned'

driver_api_root = API_ROOT + "/api/admin/app"
login = driver_api_root + "/login"
user_info = driver_api_root + "/auth/get-user-info"
routed = driver_api_root + "/deliveries/{delivery}/deliver"
move_on_tomorrow = driver_api_root + "/deliveries/{delivery}/move-on-tomorrow"
called = driver_api_root + "/deliveries/{delivery}/set-called"
not_called = driver_api_root + "/deliveries/{delivery}/set-not-called"
clarify = driver_api_root + "/deliveries/{delivery}/clarify"
new_address = driver_api_root + "/deliveries/{delivery}/new-address"
set_time_window = driver_api_root + "/deliveries/{delivery}/set-time-window"

# Создание заказа
create_task = API_ROOT + f'/api/admin/v1/clients/{constants.client_id}/create-order-task'
create_order = API_ROOT + f'/api/admin/v1/tasks-v2/task' #f"/{context.task_id}/related-orders/create"
set_planned = API_ROOT + f'/api/deliveries' #f'/{context.delivery_id}/set-planned'
close_task = API_ROOT + f'/api/admin/v1/tasks' #f'/{context.task_id}/close'
get_delivery_info = API_ROOT + f'/api/admin/v1/deliveries/admin-delivery' #f'/{context.delivery_id}/info'
assign_courier = API_ROOT + f'/api/deliveries/group-driver-update'
give_box_to_courier = API_ROOT + f'/api/deliveries' #f'/{context.delivery_id}/force-ship-own-items'
change_delivery_date = API_ROOT + f'/api/admin/v1/deliveries' #/{context.delivery_id}/change-delivery-date
