help("state.x77")



cor.test.1 = function(x, y){
  n = length(x)
  
  r = cor(x, y, method="pearson")
  Sr = sqrt((1-r^2)/(n-2))
  t = abs(r)/Sr
  
  # t = round(t,3)
  # print(t)
  return(t)
}




states <- state.x77

# cov(states)
# cor(states)
# cor(states, method="spearman")

states = as.data.frame(states)
# names(states)
# [1] "Population" "Income"     "Illiteracy" "Life Exp"  
# [5] "Murder"     "HS Grad"    "Frost"      "Area"  


x = states$Income
y = states$Frost

# cor(x, y, method="pearson")

cor.test(x, y, method="pearson")$statistic
cor.test.1(x, y)




