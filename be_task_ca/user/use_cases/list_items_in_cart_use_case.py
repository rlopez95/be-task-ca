from be_task_ca.user.domain.user_repository import UserRepository


def list_items_in_cart(user_id, user_repository: UserRepository):
    cart_items = user_repository.find_cart_items_for_user_id(user_id, user_repository)
    return AddToCartResponse(items=list(map(cart_item_model_to_schema, cart_items)))


def cart_item_model_to_schema(model: CartItem):
    return AddToCartRequest(item_id=model.item_id, quantity=model.quantity)
