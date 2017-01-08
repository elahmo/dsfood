#import file/data
hg <- read.table("~/health_gender.csv", sep=",", header=TRUE)

#sugar qty
n_sugar_comp <- runif(hg$growth_sugar_comp)

#soft drinks
n_soft_drinks <- runif(hg$growth_soft_drinks)

#all and sugar qty
n_all <- runif(hg$growth_all)
plot(n_all, n_sugar_comp)
cov_all_sugar <- cov(n_all, n_sugar_comp)
cor_all_sugar <- cor(n_all, n_sugar_comp)

#all and soft drinks
plot(n_all, n_soft_drinks)
cov_all_soft <- cov(n_all, n_soft_drinks)
cor_all_soft <- cor(n_all, n_soft_drinks)

#male and sugar qty
n_male <- runif(hg$growth_male)
plot(n_male, n_sugar_comp)
cov_male_sugar <- cov(n_male, n_sugar_comp)
cor_male_sugar <- cor(n_male, n_sugar_comp)

#male and soft drinks
plot(n_male, n_soft_drinks)
cov_male_soft <- cov(n_male, n_soft_drinks)
cor_male_soft <- cor(n_male, n_soft_drinks)

#female and sugar qty
n_female <- runif(hg$growth_female)
plot(n_female, n_sugar_comp)
cov_female_sugar <- cov(n_female, n_sugar_comp)
cor_female_sugar <- cor(n_female, n_sugar_comp)

#female and soft drinks
plot(n_female, n_soft_drinks)
cov_female_soft <- cov(n_female, n_soft_drinks)
cor_female_soft <- cor(n_female, n_soft_drinks)

#under16 and sugar qty
n_under_16 <- runif(hg$growth_under_16)
plot(n_under_16, n_sugar_comp)
cov_under16_sugar <- cov(n_under_16, n_sugar_comp)
cor_under16_sugar <- cor(n_under_16, n_sugar_comp)

#under16 and soft drinks
plot(n_under_16, n_soft_drinks)
cov_under16_soft <- cov(n_under_16, n_soft_drinks)
cor_under16_soft <- cor(n_under_16, n_soft_drinks)

#16-24 and sugar qty
n_16_24 <- runif(hg$Growth_16_24)
plot(n_16_24, n_sugar_comp)
cov_16_24_sugar <- cov(n_16_24, n_sugar_comp)
cor_16_24_sugar <- cor(n_16_24, n_sugar_comp)

#16-24 and soft drinks
plot(n_16_24, n_soft_drinks)
cov_16_24_soft <- cov(n_16_24, n_soft_drinks)
cor_16_24_soft <- cor(n_16_24, n_soft_drinks)

#25-34 and sugar qty
n_25_34 <- runif(hg$Growth_25_34)
plot(n_25_34, n_sugar_comp)
cov_25_34_sugar <- cov(n_25_34, n_sugar_comp)
cor_25_34_sugar <- cor(n_25_34, n_sugar_comp)

#25-34 and soft drinks
plot(n_25_34, n_soft_drinks)
cov_25_34_soft <- cov(n_25_34, n_soft_drinks)
cor_25_34_soft <- cor(n_25_34, n_soft_drinks)

#35-44 and sugar qty
n_35_44 <- runif(hg$Growth_35_44)
plot(n_35_44, n_sugar_comp)
cov_35_44_sugar <- cov(n_35_44, n_sugar_comp)
cor_35_44_sugar <- cor(n_35_44, n_sugar_comp)

#35-44 and soft drinks
plot(n_35_44, n_soft_drinks)
cov_35_44_soft <- cov(n_35_44, n_soft_drinks)
cor_35_44_soft <- cor(n_35_44, n_soft_drinks)

#45_54 and sugar qty
n_45_54 <- runif(hg$Growth_45_54)
plot(n_45_54, n_sugar_comp)
cov_45_54_sugar <- cov(n_45_54, n_sugar_comp)
cor_45_54_sugar <- cor(n_45_54, n_sugar_comp)

#45_54 and soft drinks
plot(n_45_54, n_soft_drinks)
cov_45_54_soft <- cov(n_45_54, n_soft_drinks)
cor_45_54_soft <- cor(n_45_54, n_soft_drinks)

#55_64 and sugar qty
n_55_64 <- runif(hg$Growth_55_64)
plot(n_55_64, n_sugar_comp)
cov_55_64_sugar <- cov(n_55_64, n_sugar_comp)
cor_55_64_sugar <- cor(n_55_64, n_sugar_comp)

#55_64 and soft drinks
plot(n_55_64, n_soft_drinks)
cov_55_64_soft <- cov(n_55_64, n_soft_drinks)
cor_55_64_soft <- cor(n_55_64, n_soft_drinks)

#65_74 and sugar qty
n_65_74 <- runif(hg$Growth_65_74)
plot(n_65_74, n_sugar_comp)
cov_65_74_sugar <- cov(n_65_74, n_sugar_comp)
cor_65_74_sugar <- cor(n_65_74, n_sugar_comp)

#65_74 and soft drinks
plot(n_65_74, n_soft_drinks)
cov_65_74_soft <- cov(n_65_74, n_soft_drinks)
cor_65_74_soft <- cor(n_65_74, n_soft_drinks)

#75_over and sugar qty
n_75_over <- runif(hg$Growth_75_over)
plot(n_75_over, n_sugar_comp)
cov_75_over_sugar <- cov(n_75_over, n_sugar_comp)
cor_75_over_sugar <- cor(n_75_over, n_sugar_comp)

#75_over and soft drinks
plot(n_75_over, n_soft_drinks)
cov_75_over_soft <- cov(n_75_over, n_soft_drinks)
cor_75_over_soft <- cor(n_75_over, n_soft_drinks)

sum_cov_sugar <- c(cov_all_sugar, cov_male_sugar, cov_female_sugar, cov_under16_sugar, cov_16_24_sugar, cov_25_34_sugar, cov_35_44_sugar, cov_45_54_sugar, cov_55_64_sugar, cov_65_74_sugar, cov_75_over_sugar)
sum_cor_sugar <- c(cor_all_sugar, cor_male_sugar, cor_female_sugar, cor_under16_sugar, cor_16_24_sugar, cor_25_34_sugar, cor_35_44_sugar, cor_45_54_sugar, cor_55_64_sugar, cor_65_74_sugar, cor_75_over_sugar)
sum_cov_soft <- c(cov_all_soft, cov_male_soft, cov_female_soft, cov_under16_soft, cov_16_24_soft, cov_25_34_soft, cov_35_44_soft, cov_45_54_soft, cov_55_64_soft, cov_65_74_soft, cov_75_over_soft)
sum_cor_soft <- c(cor_all_soft, cor_male_soft, cor_female_soft, cor_under16_soft, cor_16_24_soft, cor_25_34_soft, cor_35_44_soft, cor_45_54_soft, cor_55_64_soft, cor_65_74_soft, cor_75_over_soft)

bar = barplot(sum_cor_sugar, ylim=c(-0.5,0.8))
lines(x = bar, y=sum_cov_sugar)

bar = barplot(sum_cor_soft, ylim=c(-0.5,0.8))
lines(x = bar, y=sum_cov_soft)

all_sum <- c(sum_cov_sugar, sum_cor_sugar, sum_cov_soft, sum_cor_soft)
write.table(all_sum, "all_sum_value", sep="\t", row.names=FALSE, col.names=FALSE)





