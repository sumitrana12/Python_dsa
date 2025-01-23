#formula to Sum n natural numbers is sum=(n*(n+1))/2
#Time Complexity and space complexity will be o(1)


nth_number=int(input("Enter the Nth number till where you want the sum: "))
sum = nth_number*(nth_number+1)//2

print(sum)