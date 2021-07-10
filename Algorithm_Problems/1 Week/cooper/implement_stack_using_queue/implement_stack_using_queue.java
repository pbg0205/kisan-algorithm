import java.util.LinkedList;
import java.util.Queue;

class MyStack {

    private Queue<Integer> enQueue;
    private Queue<Integer> deQueue;

    public MyStack() {
        this.enQueue = new LinkedList<>();
        this.deQueue = new LinkedList<>();
    }

    public void push(int x) {
        if(enQueue.isEmpty()) {
            enQueue.add(x);
            while (!deQueue.isEmpty()) {
                enQueue.add(deQueue.poll());
            }
        } else if (deQueue.isEmpty()) {
            deQueue.add(x);
            while(!enQueue.isEmpty()) {
                deQueue.add(enQueue.poll());
            }
        }
    }

    public int pop() {
        if(enQueue.isEmpty()) {
            return deQueue.poll();
        }
        return enQueue.poll();
    }

    public int top() {
        if(enQueue.isEmpty()) {
            return deQueue.peek();
        }
        return enQueue.peek();
    }

    public boolean empty() {
        return enQueue.isEmpty() && deQueue.isEmpty();
    }
}

