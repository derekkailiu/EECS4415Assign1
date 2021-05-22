import argparse



def main():
    #vars
    count_edge=0
    count_node=0
    node=[]
    node_degree=[]
    # read args
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    # Scan file
    with open(args.filename, "r") as f, open("p4_output.txt",'w') as w:
        lines=f.read().splitlines();
        for line in lines:
            count_edge+=1
            token=line.split(' ')
            
            if token[0] not in node and token[1] not in node:
                count_node+=2
                node.append(token[0])
                node.append(token[1])
                node_degree.append(1)
                node_degree.append(1)
            elif token[0] not in node:
                count_node+=1
                node.append(token[0])
                node_degree.append(1)
                node_degree[node.index(token[1])]+=1
            elif token[1] not in node:
                count_node+=1
                node.append(token[1])
                node_degree.append(1)
                node_degree[node.index(token[0])]+=1
            else:
                node_degree[node.index(token[0])]+=1
                node_degree[node.index(token[1])]+=1
    
        #print I
        print(str(count_node)+':|N| '+str(count_edge)+':|E|',file=w)
        print('\n',file=w)
        #print II
        print('nodeID:nodeDegree\n', file=w)
        for i in range(count_node):
            print(str(node[i])+':'+str(node_degree[i]), file=w)
        print('\n',file=w)
        #print III
        avg_node_degree = sum(node_degree)/count_node
        print('avgNodeDegree:{:2f}'.format(avg_node_degree), file=w)





# check main()
if __name__ == "__main__":
    main()
