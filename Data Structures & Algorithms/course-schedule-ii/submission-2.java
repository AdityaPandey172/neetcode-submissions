class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int[] visited = new int[numCourses];
        List<List<Integer>> graph = new ArrayList<>();
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        ArrayDeque<Integer>  auxStack = new ArrayDeque<>();
        int[] order = new int[numCourses];

        for(int i = 0; i < numCourses; i++){
            graph.add(new ArrayList<Integer>());
        }
        for(int i = 0; i < prerequisites.length; i++){
            int course = prerequisites[i][0], prereq = prerequisites[i][1];
            graph.get(prereq).add(course);
        }
        for(int i = 0; i < numCourses; i++){
            if(visited[i] == 0){
                stack.push(i);
                while (!stack.isEmpty()){
                    Integer prereq = stack.peek();
                    if(visited[prereq] == 0){
                        visited[prereq] = -1;
                    }
                    else if (visited[prereq] == -1){
                        stack.pop();
                        visited[prereq] = 1;
                        auxStack.push(prereq);
                        continue;
                    }
                    else if (visited[prereq] == 1){
                        stack.pop();
                        continue;
                    }
                    for (Integer course: graph.get(prereq)){
                        if(visited[course] == 0){
                            stack.push(course);
                        }
                        else if (visited[course] == -1){
                            return new int[0];
                        }
                    }
                     
                }
            }
        }
        for (int i = 0; i < numCourses; i++){
            order[i] = auxStack.pop();
        }
        return order;    
    }
}
