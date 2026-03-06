""" Reverse Linked List Exercise:

Given the head of a SINGLY linked list, reverse the list, and return the reversed list.

Example 1: *****************************************************************  SEE "reverseLinkedListExamples" in "prompt_images" folder

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

----------------------------------------------------------------------------

Example 2:

Input: head = [1,2]
Output: [2,1]

=========================== NOTES AFTER COMPLETION: ============================
So figuring out a way to make a singly linked list using python was pretty interesting, it was good to get some more practice with constructors and classes. Specifically, understanding how to create
all the necessary nodes using the same variables inside a single loop was a bit tricky at first. But once I remembered that each node is initialized as a brand new object every time Node() is called 
despite being assigned to the same variable, it cleared things up quickly. All that is happening is that the newN variable simply points to the new Node(), the previous Node() is not destroyed or 
overwritten, and it can still be accessed.

Then once I had all the nodes created and a proper headnode, all I needed to do was actually figure out how to reverse it. Initially, I did what felt easiest, and simply iterated over the linkedlist
node by node and added each node's int to a list, which I then .reversed() after finishing the list, and then sent to the convertToLinkList function I wrote from the first part to make a completely new
linkedlist using a now reversed regular list. This felt like it wasn't exactly what the example had in mind as a solution, so I decided to try updating the pointers of each Node as I iterated over them
in order to reverse the list instead. Now the first method is commented out at the end, and the current version updates the original list of nodes to point in a reverse order without creating a separate
list, which I believe is more in line with the point of the exercise. I needed to create a new prevNode var in order to be able to loop through the linked list and change each node to point at the node
before it, instead of after on each run of the loop. I also had to save the original .next of the currentN as nextNode, in order to be able to change the current node to point backwards using prevNode 
while still being able to check the original next node in the next iteration of the while loop. Only other thing was that when it gets to the last node, I needed to change the headNode to be that last 
node. 

I also then made a separate printLinkList() func in order to print the link list as a nice pretty list like how it is in the output examples, and all it does is iterate through each node of the linked 
list and add the data val to a new list which gets printed as a regular list after the list is done being iterated over. Its actually basically just the first solution I used thats commented out like
stated above, the only difference is that just prints the list to ther console, instead of going on to send the list to the convertToLinkList() func. and making a new list. 

After doing all that, I was able to get the same outputs as example 1 and 2's outputs, so I decided to make up a 3rd list to test what happens with a bigger list that isn't sorted lowest to highest like
the original 2 examples and also has two duplicate values in it. It changed nothing and still returned the desired output. After thinking about more things to check, I created a 4th example to check what 
happens if a copy of the 3rd list also contains a big string, as well as an int much bigger than the rest. It too didn't effect the functions, and they returned the desired output. I expected the string 
inside the list to break the convertToLinkList() func. because it expects a list of ints, but because Python is dynamically typed and Python's lists can hold mixed data types, it won't stop the list from
being recieved with a string in it. So this means nothing breaks unless the string is operated on as an integer, which doesn't ever happen anywhere else since the Node class doesn't specify anything 
about the type of data it recieves or initiallizes, and the other funcs. never do anything with each Node's data that doesn't work for either strings or ints.


=========================== FINAL THOUGHTS + NOTE ===============================
So I feel solid with calling this exercise solved for now, but I do want to note that I didn't bother putting saftey checks in place around the inputs or indexes since the exercise didn't specify any. 
That being said if an empty list is passed to the original convertToLinkList() func it would most likely break, if any of the func.s that receive a headNode get something other than a Node they will 
also most likely break. Additionally, I didn't place any limits on the size of the original list which could be an issue, for example if the list was gigantic, since I imagine there is a limit on how 
many Nodes can be saved into memory at once. Lastly, the actual type of data in the lists is never checked in the code (tho example 3 and 4 do check for duplicate ints, non-sorted lists, strings in 
the list, and different size ints in the list).


"""
#So linked lists are a data structure where each node contains its data, plus a pointer to the next node in the list. Python doesn't have a linked list library built-in like other languages...
#we will need to create a class for the nodes to use in the linked list in order actualy make a linked list then
class Node:
   def __init__(self, data):

      #need data
      self.data = data
      #and need reference to next node
      self.next = None #this means by default the node points at a null value, which is important since the last value in the list needs to point at null, since that is what indicates the end of the list

#now that the node class exists, we need to take the input list of just ints and convert the list into a linked list of the nodes to match it.
def convertToLinkList(startList: list[int]):

   #get length of original list for iterating over later
   listLength = len(startList)

   #set up first value in list passed to be the nead node of the entire list
   headN = Node(startList[0])

   #set up end Node as head node to start before we loop through everything else
   endN = headN

   #print(f"\n Head Node data: {headN.data}, next pointer: {headN.next}")

   #loop through every int in the list passed after the very first one - (start with index 1, stop before full length since the list index starts @0 resulting in index issue otherwise)
   for i in range(1, listLength):
      
      #need to create a Node for each entry in the startList, as well as asign the .next of each Node
      #create new node with list's data
      newN = Node(startList[i])

      #assign the end node's .next to point and this current new node (NOTE means the end node that is currently pointing at the previously added node as the end node, so its the headN to start, 
      #then newN every other time)
      endN.next = newN

      #print(f"\n New Node data: {newN.data}, Previous Node's next pointer: {endN.next}")

      #now update the endN to be this current new node after updating the previous end Node's pointer
      endN = newN

   #ONLY need to return the headnode since it will point to the next node, which points to the next until the last node points at null
   return headN



#now that we have a proper singly linked list to work with, we now need to actually attempt to reverse it
def reverseLinkList(headNode):

   #because it is singly linked, each node only points at the next one, whereas a doubly linked list also points at the previous node, which could have been useful

   #we need to loop through the whole list and reverse the vals, USING ONLY the head of the list, no idea the length of the list

   #need new varaible to track a node's previous node
   currentNode = headNode
   prevNode = None

   #print(f"\n Original HeadNode: {headNode.data}, Original PrevNode: {prevNode}") #for debugging

   while currentNode: #when the final node points at null, this will break

      nextNode = currentNode.next #asign the next node as the next one after the head to start, then the next node until the list is done

      #now we can change the currentN to point at null if needed, or in other words change it to point at the previous Node's value
      currentNode.next = prevNode

      if (nextNode != None): #if we are NOT on the LAST NODE, we need to look at the next one in the next loop

         #now we need to update previousNode to point at this current node, as well as update the currentNode to the original next node for the next iteration of the while loop
         prevNode = currentNode
         currentNode = nextNode #get next node in list for the next iteration of the while loop
         #print(f"\n New PrevNode: {prevNode.data}, Next CurrentNode: {currentNode.data}") #for debugging

      elif (nextNode == None): #if we ARE on the LAST NODE, we want to make the headNode point at the current node

         headNode = currentNode #change headNode to point at the last node instead of the original head
         currentNode = nextNode #still need to change currentNode to NextNode (which is null) in order for while loop to finish running properly

         #print(f"\n New HeadNode: {headNode.data}, Final CurrentNode: {currentNode}") #for debugging

   #once while loop breaks it means currentNode should be equal to null since the last item in the linkedlist should point at null, BUT we changed it to point it the prev node after the null was found

   #now that we have the linked list reversed and the headnode now points at the node that was originally the last node in the list, we need a way to print the list
   #print(f"\n The Linked List has been successfully reversed... New HeadNode: {headNode},\n sending new list to be printed...") #for debugging
   printLinkList(headNode)

   return headNode #still have it returning a headNode so the main prints a val, technically it doesn't need to for the requirements, but I'm not changing it

   """ 
   ========= FIRST REVERSE LOGIC by creating new list and then a new linked list as well (it felt like cheating since I made an entirely new list instead of changing the vals in place) =============

   tempList = [] #use a regular list to store values of each node as we go through it

   currentN = headNode #set up starting point as the headNode

   while currentN: #when the final node points at null, this will break

      tempList.append(currentN.data) #get value of current node and store it in the regular list as we go through

      currentN = currentN.next #get next node in list for the next iteration of the while loop

   print(f"\n Temp list after the while loop: {tempList}") #for debugging

   #reverse the list
   tempList.reverse()

   print(f"\n Temp list after reversing it: {tempList}") #for debugging

   #now that we have a regular list we can just send this new list to the original convertToLinkList func to make a new linked list using the reversed list
   revHeadNode = convertToLinkList(tempList)

   return revHeadNode

   ========= FIRST REVERSE LOGIC by creating new list and then a new linked list as well (it felt like cheating since I made an entirely new list instead of changing the vals in place) =============
   """ 
# ======================================================= END REVERSE FUNCTION ====================================================================


#this is just a function that takes a headNode, loops through it's connected linked list, and then compiles it all in a list in order to be printed nicely 
def printLinkList(hN):

   fullOutput = []
   currN = hN

   while currN:

      fullOutput.append(currN.data) #add current node's data to list

      currN = currN.next #point current Node to node for the next iteration of loop

   print(f"\n Output: {fullOutput}") #print full linked list after looping through entire list while just being given the head node




def main():
   print("=" * 50)
   print(" Reverse Linked List EXERCISE")
   print("=" * 50)

   #=========================================================== EX 1 ========================================
   head1 = [1,2,3,4,5]

   print(f"\n Input head 1: {head1}\n") #print head1 to console,
   print("-" * 50)

   #print("\n Print Head Node after head1 converted to a Linked List:",convertToLinkList(head1).data) 
   #print("-" * 50)
   print("\n Reverse Linked List 1 Head Node: ", reverseLinkList(convertToLinkList(head1) ).data ) 
   print("=" * 50)

   #=========================================================== EX 2 ========================================
   
   head2 = [1,2]

   print(f"\n Input head 2: {head2}\n") #print head2 to console,
   print("-" * 50)

   #print("\n Print Head Node after head2 converted to a Linked List:",convertToLinkList(head2).data) 
   #print("-" * 50)
   print("\n Reverse Linked List 2 Head Node: ", reverseLinkList(convertToLinkList(head2) ).data )
   print("=" * 50)

   #=========================================================== EX 3 ========================================
   
   head3 = [8,4,2,9,1,7,3,6,5,8]

   print(f"\n Input head 3: {head3}\n") #print head3 to console,
   print("-" * 50)

   #print("\n Print Head Node after head3 converted to a Linked List:",convertToLinkList(head3).data) 
   #print("-" * 50)
   print("\n Reverse Linked List 3 Head Node: ", reverseLinkList(convertToLinkList(head3) ).data )
   print("=" * 50)

   #=========================================================== EX 4 ========================================
   
   head4 = ["hey this a test of strings in the list",2,9,1,7,3,6,5,1000000]

   print(f"\n Input head 4: {head4}\n") #print head4 to console,
   print("-" * 50)

   #print("\n Print Head Node after head4 converted to a Linked List:",convertToLinkList(head4).data) 
   #print("-" * 50)
   print("\n Reverse Linked List 4 Head Node: ", reverseLinkList(convertToLinkList(head4) ).data )
   print("=" * 50)

if __name__ == "__main__":
   main()