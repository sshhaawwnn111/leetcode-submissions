class ListNode {
public:
    int val;
    ListNode* next;
    ListNode(int val) : val(val), next(nullptr) {}

    ListNode(int val, ListNode* next) : val(val), next(next) {}
};


class LinkedList {
private:
    ListNode* head;
    ListNode* tail;

public:
    LinkedList() {
        head = new ListNode(-1);
        tail = head;
    }

    int get(int index) {
        ListNode* curr = head->next;
        int i = 0;
        while(curr != nullptr){
            if(i == index){
                return curr->val;
            }
            curr = curr->next;
            i++;
        }

        return -1;
    }

    void insertHead(int val) {
        ListNode* newNode = new ListNode(val);
        newNode->next = head->next;
        head->next = newNode;
        if(newNode->next == nullptr){
            tail = tail->next;
        }
    }
    
    void insertTail(int val) {
        ListNode* newNode = new ListNode(val);
        tail->next = newNode;
        tail = tail->next;
    }

    bool remove(int index) {
        ListNode* curr = head->next;
        ListNode* prev = head;

        int i = 0;
        while(curr != nullptr){
            if(i == index){
                if(curr == tail){
                    tail = prev;
                }

                prev->next = curr->next;
                delete curr;
                return true;
            }
            i++;
            prev = curr;
            curr = curr->next;
        }

        return false;
    }

    vector<int> getValues() {
        vector<int> result;

        ListNode* curr = head->next;

        while(curr != nullptr){
            result.push_back(curr->val);
            curr = curr->next;
        }

        return result;
    }
};
