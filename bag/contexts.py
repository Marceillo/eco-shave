# from bag.contexts import bag_contents

def bag_contents(request):
    """
    
    """
    shopping_bag = request.session.get('shopping_bag', {})
    context = {'items_in_bag_contents': sum(shopping_bag.values())}
    return context


