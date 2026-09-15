data <- data.frame(
  name=c("a","b","c"),
  age=c(12,NA,24),
  score=c(10,12,12)
)
print("Printing the data")
print(data)

colSums(is.na(data))

cleaned_data<-na.omit(data)
print("Cleaned Data")
print(cleaned_data)

data$age[is.na(data$age)]<-mean(data$age, na.rm = TRUE)
print("Removed Null data")
print(data)

print("Sorted data Dcreasing")
sort<-data[order(data$age, decreasing = TRUE),]
print(sort)

print("Sorted data increasing")
sort<-data[order(data$age, decreasing = FALSE),]
print(sort)