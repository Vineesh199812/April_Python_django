



results = [
    {"district":"tvm","win": 98, "A+": 45000},
    {"district":"ktm","win": 95, "A+": 44000},
    {"district":"apy","win": 97, "A+": 47000},
    {"district":"idk","win": 90 ,"A+": 38000},
    {"district":"ekm","win": 99, "A+": 56000},
    {"district":"pta","win": 99, "A+": 58000},
    {"district":"tsr","win": 98, "A+": 57000},
    {"district":"kzd","win": 99, "A+": 58000},
    {"district":"pkd","win" :95, "A+": 50000},
    {"district":"mpm","win": 90,"A+": 4500},

]

# win % of tvm
#for result in results:
    #if result["district"]=="tvm":
        #print(result["win"])

#tvm_win=[result["win"] for results if result["district"]=="tvm"]
tvm_win=[result for result in results if result["district"]=="tvm"]
print(tvm_win)

# district with highest win %
#def get_win(res):
   # return res["win"]

   #sort using *sorted() or *lst.sort

results.sort(key=lambda res:res["win"],reverse=True)
print(results)

results.sort(reverse=True,key=lambda result:result["win"])
print(results)

print(max(results,key=lambda res:res["win"]))
# district with lowest win %
print(min(results,key=lambda res:res["win"]))
# district with highest A+
print(max(results,key=lambda res:res["A+"]))
# district with lowest A+
print(min(results,key=lambda res:res["A+"]))
# total number of A+
#sum=0
#for res in results:
#    sum+=res["A+"]
#print(sum)
print(sum([res["A+"]for res in results]))
#aplus_total=sum(results,lambda res:res["A+"])

#total win percentge


