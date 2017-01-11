normalize <- function(df, cols) {
  result <- df # make a copy of the input data frame
  
  for (j in cols) { # each specified col
    m <- mean(df[,j]) # column mean
    std <- sd(df[,j]) # column (sample) sd
    
    for (i in 1:nrow(result)) { # each row of cur col
      result[i,j] <- (result[i,j] - m) / std
    }
  }
  return(result)
}

cols <- c(2, 3, 4, 9, 10, 11, 12, 13, 14, 15, 16, 25, 26, 29, 30, 31)

#import file/data
hg <- read.table("~/health_gender.csv", sep=",", header=TRUE)
hg <- normalize(hg, cols)

#year
year <- hg$Year

#sugar qty
n_sugar_comp <- hg$sugar_comp

#soft drinks
n_soft_drinks <- hg$soft_drinks

#soft drinks concentrated low calories
n_sd_con_lc <- hg$sd_con_lc

#soft drinks not concentrated low calories
n_sd_ncon_lc <- hg$sd_ncon_lc

#soft drinks sum low calories
n_sd_sum_lc <- hg$sd_sum_lc

#all and sugar qty
n_all <- hg$All_persons
plot(n_all, n_sugar_comp)
cov_all_sugar <- cov(n_all, n_sugar_comp)
cor_all_sugar <- cor(n_all, n_sugar_comp)

qdlm_all_sugar <- lm(n_all ~ poly(n_sugar_comp, 2))
plot(n_all ~ n_sugar_comp,
     xlab="Consumption of Sugar", 
     ylab="Obesity",
     lwd=5)
lines(sort(n_sugar_comp), fitted(qdlm_all_sugar)[order(n_sugar_comp)], col="red", lwd=5)

cov_all_sugar
cor_all_sugar

#all and soft drinks
plot(n_all, n_soft_drinks)
cov_all_soft <- cov(n_all, n_soft_drinks)
cor_all_soft <- cor(n_all, n_soft_drinks)

qdlm_all_soft <- lm(n_all ~ poly(n_soft_drinks, 2))
plot(n_all ~ n_soft_drinks,
     xlab="Consumption of Soft Drinks", 
     ylab="Obesity",
     lwd=5)
lines(sort(n_soft_drinks), fitted(qdlm_all_soft)[order(n_soft_drinks)], col="red", lwd=5)

cov_all_soft
cor_all_soft

#all and soft drinks concentrated low calories
plot(n_all, n_sd_con_lc)
cov_all_sd_con_lc <- cov(n_all, n_sd_con_lc)
cor_all_sd_con_lc <- cor(n_all, n_sd_con_lc)

qdlm_all_sd_con_lc <- lm(n_all ~ poly(n_sd_con_lc, 2))
plot(n_all ~ n_sd_ncon_lc,
     xlab="Consumption of Concentrated Low Calories Soft Drinks", 
     ylab="Obesity")
lines(sort(n_sd_con_lc), fitted(qdlm_all_sd_con_lc)[order(n_sd_con_lc)], col="red")

cov_all_sd_con_lc
cor_all_sd_con_lc

#all and soft drinks not concentrated low calories
plot(n_all, n_sd_ncon_lc)
cov_all_sd_ncon_lc <- cov(n_all, n_sd_ncon_lc)
cor_all_sd_ncon_lc <- cor(n_all, n_sd_ncon_lc)

qdlm_all_sd_ncon_lc <- lm(n_all ~ poly(n_sd_ncon_lc, 2))
plot(n_all ~ n_sd_ncon_lc,
     xlab="Consumption of Non Concentrated Low Calories Soft Drinks", 
     ylab="Obesity")
lines(sort(n_sd_ncon_lc), fitted(qdlm_all_sd_ncon_lc)[order(n_sd_ncon_lc)], col="red")

cov_all_sd_ncon_lc
cor_all_sd_ncon_lc

#all and soft drinks sum low calories
plot(n_all, n_sd_sum_lc)
cov_all_sd_sum_lc <- cov(n_all, n_sd_sum_lc)
cor_all_sd_sum_lc <- cor(n_all, n_sd_sum_lc)

qdlm_all_sd_sum_lc <- lm(n_all ~ poly(n_sd_sum_lc, 2))
plot(n_all ~ n_sd_sum_lc,
     xlab="Consumption of Low Calories Soft Drinks", 
     ylab="Obesity",
     lwd=5)
lines(sort(n_sd_sum_lc), fitted(qdlm_all_sd_sum_lc)[order(n_sd_sum_lc)], col="red", lwd=5)

cov_all_sd_sum_lc
cor_all_sd_sum_lc

#male and sugar qty
n_male <- hg$Male
plot(n_male, n_sugar_comp)
cov_male_sugar <- cov(n_male, n_sugar_comp)
cor_male_sugar <- cor(n_male, n_sugar_comp)

qdlm_male_sugar <- lm(n_male ~ poly(n_sugar_comp, 2))
plot(n_male ~ n_sugar_comp)
lines(predict(qdlm_male_sugar) ~ n_sugar_comp, col="red")

cov_male_sugar
cor_male_sugar

#male and soft drinks
plot(n_male, n_soft_drinks)
cov_male_soft <- cov(n_male, n_soft_drinks)
cor_male_soft <- cor(n_male, n_soft_drinks)

qdlm_male_soft <- lm(n_male ~ poly(n_soft_drinks, 2))
plot(n_male ~ n_soft_drinks)
lines(predict(qdlm_male_soft) ~ n_soft_drinks, col="red")

cov_male_soft
cor_male_soft

#female and sugar qty
n_female <- hg$Female
plot(n_female, n_sugar_comp)
cov_female_sugar <- cov(n_female, n_sugar_comp)
cor_female_sugar <- cor(n_female, n_sugar_comp)

qdlm_female_sugar <- lm(n_female ~ poly(n_sugar_comp, 2))
plot(n_female ~ n_sugar_comp)
lines(predict(qdlm_female_sugar) ~ n_sugar_comp, col="red")

cov_female_sugar
cor_female_sugar

#female and soft drinks
plot(n_female, n_soft_drinks)
cov_female_soft <- cov(n_female, n_soft_drinks)
cor_female_soft <- cor(n_female, n_soft_drinks)

qdlm_female_soft <- lm(n_female ~ poly(n_soft_drinks, 2))
plot(n_female ~ n_soft_drinks)
lines(predict(qdlm_female_soft) ~ n_soft_drinks, col="red")

cov_female_soft
cor_female_soft

#under16 and sugar qty
n_under_16 <- hg$Under_16
plot(n_under_16, n_sugar_comp)
cov_under16_sugar <- cov(n_under_16, n_sugar_comp)
cor_under16_sugar <- cor(n_under_16, n_sugar_comp)

cov_under16_sugar
cor_under16_sugar

#under16 and soft drinks
plot(n_under_16, n_soft_drinks)
cov_under16_soft <- cov(n_under_16, n_soft_drinks)
cor_under16_soft <- cor(n_under_16, n_soft_drinks)

cov_under16_soft
cor_under16_soft

#16-24 and sugar qty
n_16_24 <- hg$Age_16_24
plot(n_16_24, n_sugar_comp)
cov_16_24_sugar <- cov(n_16_24, n_sugar_comp)
cor_16_24_sugar <- cor(n_16_24, n_sugar_comp)

cov_16_24_sugar
cor_16_24_sugar

#16-24 and soft drinks
plot(n_16_24, n_soft_drinks)
cov_16_24_soft <- cov(n_16_24, n_soft_drinks)
cor_16_24_soft <- cor(n_16_24, n_soft_drinks)

cov_16_24_soft
cor_16_24_soft

#25-34 and sugar qty
n_25_34 <- hg$Age_25_34
plot(n_25_34, n_sugar_comp)
cov_25_34_sugar <- cov(n_25_34, n_sugar_comp)
cor_25_34_sugar <- cor(n_25_34, n_sugar_comp)

#25-34 and soft drinks
plot(n_25_34, n_soft_drinks)
cov_25_34_soft <- cov(n_25_34, n_soft_drinks)
cor_25_34_soft <- cor(n_25_34, n_soft_drinks)

#35-44 and sugar qty
n_35_44 <- hg$Age_35_44
plot(n_35_44, n_sugar_comp)
cov_35_44_sugar <- cov(n_35_44, n_sugar_comp)
cor_35_44_sugar <- cor(n_35_44, n_sugar_comp)

#35-44 and soft drinks
plot(n_35_44, n_soft_drinks)
cov_35_44_soft <- cov(n_35_44, n_soft_drinks)
cor_35_44_soft <- cor(n_35_44, n_soft_drinks)

#45_54 and sugar qty
n_45_54 <- hg$Age_45_54
plot(n_45_54, n_sugar_comp)
cov_45_54_sugar <- cov(n_45_54, n_sugar_comp)
cor_45_54_sugar <- cor(n_45_54, n_sugar_comp)

#45_54 and soft drinks
plot(n_45_54, n_soft_drinks)
cov_45_54_soft <- cov(n_45_54, n_soft_drinks)
cor_45_54_soft <- cor(n_45_54, n_soft_drinks)

#55_64 and sugar qty
n_55_64 <- hg$Age_55_64
plot(n_55_64, n_sugar_comp)
cov_55_64_sugar <- cov(n_55_64, n_sugar_comp)
cor_55_64_sugar <- cor(n_55_64, n_sugar_comp)

#55_64 and soft drinks
plot(n_55_64, n_soft_drinks)
cov_55_64_soft <- cov(n_55_64, n_soft_drinks)
cor_55_64_soft <- cor(n_55_64, n_soft_drinks)

#65_74 and sugar qty
n_65_74 <- hg$Age_65_74
plot(n_65_74, n_sugar_comp)
cov_65_74_sugar <- cov(n_65_74, n_sugar_comp)
cor_65_74_sugar <- cor(n_65_74, n_sugar_comp)

#65_74 and soft drinks
plot(n_65_74, n_soft_drinks)
cov_65_74_soft <- cov(n_65_74, n_soft_drinks)
cor_65_74_soft <- cor(n_65_74, n_soft_drinks)

#75_over and sugar qty
n_75_over <- hg$Age_75_over
plot(n_75_over, n_sugar_comp)
cov_75_over_sugar <- cov(n_75_over, n_sugar_comp)
cor_75_over_sugar <- cor(n_75_over, n_sugar_comp)

#75_over and soft drinks
plot(n_75_over, n_soft_drinks)
cov_75_over_soft <- cov(n_75_over, n_soft_drinks)
cor_75_over_soft <- cor(n_75_over, n_soft_drinks)

qdlm_75_soft <- lm(n_75_over ~ poly(n_soft_drinks, 2))
plot(n_75_over ~ n_soft_drinks)
lines(sort(n_soft_drinks), fitted(qdlm_75_soft)[order(n_soft_drinks)], col="red")

sum_cov_sugar <- c(cov_all_sugar, cov_male_sugar, cov_female_sugar, cov_under16_sugar, cov_16_24_sugar, cov_25_34_sugar, cov_35_44_sugar, cov_45_54_sugar, cov_55_64_sugar, cov_65_74_sugar, cov_75_over_sugar)
sum_cor_sugar <- c(cor_all_sugar, cor_male_sugar, cor_female_sugar, cor_under16_sugar, cor_16_24_sugar, cor_25_34_sugar, cor_35_44_sugar, cor_45_54_sugar, cor_55_64_sugar, cor_65_74_sugar, cor_75_over_sugar)
sum_cov_soft <- c(cov_all_soft, cov_male_soft, cov_female_soft, cov_under16_soft, cov_16_24_soft, cov_25_34_soft, cov_35_44_soft, cov_45_54_soft, cov_55_64_soft, cov_65_74_soft, cov_75_over_soft)
sum_cor_soft <- c(cor_under16_soft, cor_16_24_soft, cor_25_34_soft, cor_35_44_soft, cor_45_54_soft, cor_55_64_soft, cor_65_74_soft, cor_75_over_soft)

bar = barplot(sum_cor_sugar, ylim=c(-0.5,0.8))
lines(x = bar, y=sum_cov_sugar)

bar = barplot(sum_cor_soft, ylim=c(-0.5,0.6))
lines(x = bar, y=sum_cov_soft)
title(main = "Correlation of Soft Drinks Consumption and Obesity",
      xlab = "demography", ylab="obesity",
      cex.main = 2, font.main = 2, col.main = "black",
      cex.sub = 1.25, font.sub = 1, col.sub = "blue")

all_sum <- c(sum_cov_sugar, sum_cor_sugar, sum_cov_soft, sum_cor_soft)
write.table(all_sum, "all_sum_value", sep="\t", row.names=FALSE, col.names=FALSE)


