install.packages("lubridate")
library(lubridate)

# NBA Business problem 

setwd("C:/Users/Vincent/Documents/0 - Stevens/random")

nba <- read.csv("training_set.csv")

# This is the range of engagements we are dealing with
max(nba[,1])
min(nba[,1])

nba <- data.frame(nba)

# Counts characters in the Description category
nchar(as.character(nba$Description[1]))

# This loop adds the Caption length from the Description
nba$Caption.length <- NA
for(i in 1:length(nba[,1])){
  nba$Caption.length[i] <- nchar(as.character(nba$Description[i]))
  
}
head(nba$Caption.length)

# Now have to adjust the times based on this 
# https://blog.hubspot.com/marketing/instagram-best-time-post

# This finds the day of the week given the time
nba$Day <- NA
for(i in 1:length(nba[,1])){
  nba$Day[i] <- weekdays(strptime(nba$Created[i], format = "%Y-%m-%d %H:%M:%S", tz = "America/New_York"))
}


# Assigns numbers for each day of the week. 1 is Sunday, 7 is Saturday
nba$Day.num <- NA
for(i in 1:length(nba[,1])){
  nba$Day.num[i] <- wday(nba$Created[i])
}

# This quantifies the category of post
nba$Type.num <- NA
for(i in 1:length(nba[,1])){
  if(nba$Type[i] == "Video")(nba$Type.num[i] = 1)
  if(nba$Type[i] == "Photo")(nba$Type.num[i] = 2)
  if(nba$Type[i] == "Album")(nba$Type.num[i] = 3)
}


summary(lm(nba$Engagements ~ nba$Followers.at.Posting + nba$Caption.length + nba$Day.num + nba$Type.num))

# TO DO: Quantify time of day when it is posted, create groups for morning, afternoon, night,
# late night. 

# Have to use strptime() to compare the times 
Sys.time() > (strptime(nba$Created[1], format = "%Y-%m-%d %H:%M:%S", tz = "America/New_York"))

"2019-06-16 16:31:45 EDT" > (strptime(nba$Created[1], format = "%Y-%m-%d %H:%M:%S", tz = "America/New_York"))
