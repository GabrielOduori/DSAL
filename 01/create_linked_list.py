def create_linked_list_better(input_list):
    # """
    # Function to create a linked list
    # @param input_list: a list of integers
    # @return: head node of the linked list
    # """
    # head  = None
    # for vale in input_list:
    #     if head is None:
    #         head = Node(value)
    #     else:
    #         #Move to the tail ( The last Node)
    #         current_node = head
    #         while current_node.next:
    #             current_node = current_node.next
    #         current_node.next = Node(value)
    # return head
    head = None
    tail = None
    
    for value in input_list:
        
        if head is None:
            head = Node(value)
            tail = head # when we only have 1 node, head and tail refer to the same node
        else:
            tail.next = Node(value) # attach the new node to the `next` of tail
            tail = tail.next # update the tail
            
    return head


def test_function(input_list, head):
    try:
        if len(input_list)==0:
            if head is not None:
                print("Fail")
                return
        for value in input_list:
            if head.value!=value:
                print("Fail")
                return
            else:
                head = head.next
        print("Pass")
    except Exception as e:
        print("Fail:" + e)



input_list = [1, 2, 3, 4, 5, 6]
head = create_linked_list_better(input_list)
test_function(input_list, head)

input_list = [1]
head = create_linked_list_better(input_list)
test_function(input_list, head)

input_list = []
head = create_linked_list_better(input_list)
test_function(input_list, head)