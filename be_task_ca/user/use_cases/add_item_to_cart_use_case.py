from be_task_ca.user.domain.user import User, UserNotFound
from be_task_ca.user.domain.user_repository import UserRepository


def add_item_to_cart(
    user_id: int, cart_item: AddToCartRequest, user_repository: UserRepository
) -> AddToCartResponse:
    user: User = user_repository.find_user_by_id(user_id, user_repository)
    if user is None:
        raise UserNotFound("User does not exist")

    item: Item = find_item_by_id(cart_item.item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item does not exist")
    if item.quantity < cart_item.quantity:
        raise HTTPException(status_code=409, detail="Not enough items in stock")

    item_ids = [o.item_id for o in user.cart_items]
    if cart_item.item_id in item_ids:
        raise HTTPException(status_code=409, detail="Item already in cart")

    new_cart_item: CartItem = CartItem(
        user_id=user.id, item_id=cart_item.item_id, quantity=cart_item.quantity
    )

    user.cart_items.append(new_cart_item)

    save_user(user, user_repository)

    return list_items_in_cart(user.id, user_repository)


def list_items_in_cart(user_id, user_repository: UserRepository):
    cart_items = user_repository.find_cart_items_for_user_id(user_id, db)
    return AddToCartResponse(items=list(map(cart_item_model_to_schema, cart_items)))
