/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode invertTree(TreeNode root) {
        
        Queue<TreeNode> queue = new LinkedList<>();
        
        if (root!= null){
            queue.add(root);
        }
        
        while(!queue.isEmpty()){
            
            TreeNode node = queue.remove();
            TreeNode left = node.left;
            TreeNode right = node.right;
            
            TreeNode tmp = left;
            node.left = right;
            node.right = tmp;
            
            if (node.left != null){
                queue.add(node.left);
            }
            
            if(node.right != null){
                queue.add(node.right);
            }
        }
        
        
        return root;

        
    }
}