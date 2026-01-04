# install.packages("RSQLite")

library(DBI)
library(RSQLite)
library(ggplot2)
library(dplyr)

# CONNECTING TO THE DATABASE
con_r <- dbConnect(RSQLite::SQLite(), dbname = "database.db")

# READING AND DISPLAYING DATA

df <- dbReadTable(con_r, "users") # df stands for data frame

print("--- User Data ---")
print(head(df))

# BASIC STATISTICAL ANALYSIS
grades_mean <- mean(df$grade)
cat("\nMean Grade of Users: ", grades_mean, "\n")

approved_users <- subset(df, grade >= 70)
cat("Number of Approved Users: ", nrow(approved_users), "\n")

# SIMPLE GRAPHICAL REPRESENTATION
hist(df$grade,
     main = "Grade Distribution",
     xlab = "Grades",
     col = "lightblue",
     border = "white")


# RUNNING SQL QUERIES
above_80 <- dbGetQuery(con_r, "SELECT name,
grade FROM users WHERE grade > 80 ORDER BY grade DESC")
print(above_80)

# CREATING A BOXPLOT
boxplot(df$grade,
        main = "Grades Summary",
        col = "orange",
        horizontal = TRUE)

abline(v = mean(df$grade), col = "red", lwd = 2) # Adding a red line for mean

# CREATING MULTIPLE COLUMNS WITH DPLYR
df <- df %>%
  mutate(
    status = ifelse(grade >= 70, "Approved", "Not Approved"),
    category = case_when(
      grade >= 90 ~ "Excellent",
      grade >= 70 ~ "Good",
      grade >= 50 ~ "Average",
      TRUE ~ "Needs Improvement"
    )
  )

# HISTOGRAM WITH GGLPOT2
p1 <- ggplot(df, aes(x=grade)) +
    geom_histogram(binwidth=5, fill = "#4e79a7", color = "white") +
    theme_minimal() +
    geom_vline(xintercept = mean(df$grade), color = "red", size = 1)

print(p1)

# SAVING AND EXPORTING RESULTS AS CSV
write.csv(df, "user_data.csv", row.names = FALSE)
print("File 'user_data.csv' has been succesfully created.")

# DISCONNECTING FROM THE DATABASE
dbDisconnect(con_r)