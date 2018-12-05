# Wednesday Office Hours

## Our questions:

### Concerning the Third Uncertainty

- We know that Rain and Mold are two of the three uncertainties, but we're not sure what the third one is:
  - Our guess is that **the varying accuracy of the detector** is the third uncertainty.
  - If so, or whatever the third uncertainty is, how do we do sensitivity analysis on this third sensitivity?
  - Motivation: Information about this third uncertainty would change the tree

### Concerning "plot symmetrically around zero"
- What do the words **"plot symmetrically around zero"** mean? Refer to graph in book, *Figure 12.11*.
- Is the formula on 93/110 on "UtilityProbabilisticDominancetoWebsite" the one we want to use to calculate this sensitivity?


### If have time, xls tree

- Accuracy of rain / mold?




# Concerning the "Updated Probability"

**Caveat**: So although I'm a little lost here, Giovanni pointed me to specific things. Hopefully me sending this to you all will help the brains go to the right direction:

## Big takeaways

### Second visit, after DiDi's questions:

- So big high level concept is that the **prior probabilities** are *Jaeger beliefs*, and the **posterior probabilities** are *Abbey data (pdf)*.
  - Jaeger beliefs (prior) Alejandro gave on Friday problem session
  - Abbey data (posterior) on pdf

- **Main method to calculate P(rain) / P(mold)**: use *Abbey data (pdf)* and count the number of successes / failures to determine probability of each
  - **For example**: For P(mold | NO rain), only look at the rows that contain a *failure* (0) for Storm
  - **For example**: For P(rain | mold), only look at the rows that contain a *success* (yes) for Botrytis Mold
  - **Caveat**: NOT quite simple frequentist version, where you count the number of successes and divide by total number of data
    - this is only the posterior part, where we use this (new) data (Abbey) to update beliefs

- Calculating P(rain) and P(mold) are the same:
  - Success / failure = storm / no storm (0/1)
  - Success / failure = mold / no mold (yes / no)


### First visit, before DiDi's questions:

- So it seems like we're supposed to use equations on the slides, **Bayesian Updating to Website.pdf**.

- Giovanni specified that We want to update with the specific equation(s) on slide **"Your Posterior Is the Product"**.
   
- Giovanni also pointed me towards using the following:
  - **Steph Curry xls (excel spreadsheet that we looked at yesterday)**
  - **"Freemark Abbey Historical.pdf"**

- For "Freemark Abbey Historical.pdf", he said something specific: we want to use the "successes and failures" per each year to also update the probability.

## Misc. notes

### First visit

Maybe helpful. I wrote down

```
update with posterior

binomial
```

and next page

```
"prior distribution -> updating formula"

and

"use abbey historical to update distribution"
```

and earlier, about the Bayesian Updating,

```
xls

talk to interviewee for fancier updating

"we're giving the interviewee discretion for fancier extra credit stuff"
```

### Second visit

- Word for word notes:

```
P(rain)

    success / failure
    storm / no storm
```

```
P(mold|rain)
        |
        |
        |
       \ /
        .
        storm = 1
```

```

NOT frequentist

    not simple

```

```

use prior, then have new
   |           |
   |           |
   |          \ /
   |           .
   |             use to update beliefs
   |
  \ /
   .
   Jaeger beliefs <-- Alejandro gave on Friday P.S.

     beta 1 1
```



