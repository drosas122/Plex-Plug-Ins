
                if type(res) is ListType:
                    res[idx : idx + 1] = [v]
                else:
                    res = res[:idx] + (v,) + res[idx + 1:]
        return res

    def dispatchObject(self, ob):
        '''
        Expected to return either ob or something that will take
        its place.
        '''
        if isinstance(ob, ast.Node):
            return self.dispatchNode(ob)
        elif type(ob) in SequenceTypes:
        
