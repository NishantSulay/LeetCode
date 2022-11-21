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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        
        if(p != null && q !=null ){
            if (p.val != q.val){
                return false;
                
            } else {
                return this.isSameTree(p.left, q.left) && this.isSameTree(p.right, q.right);
            }
        } 
        
        if(p !=null && q == null || p ==null && q!=null){
            return false;
        }
        

        return true;
        
    }
}