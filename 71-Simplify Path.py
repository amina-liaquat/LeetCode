class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        curr_dir=""

        for c in path+"/":
            if c=="/":
                if curr_dir=="..":
                    if stack:
                        stack.pop()
                elif curr_dir!="" and curr_dir!=".":
                    stack.append(curr_dir)
                curr_dir=""

            else:
                curr_dir+=c

        return "/"+"/".join(stack)
